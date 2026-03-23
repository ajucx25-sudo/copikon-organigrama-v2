import express, { type Express } from "express";
import { createServer, type Server } from "http";
import fs from "fs";
import path from "path";
import crypto from "crypto";
import os from "os";
import { execFile } from "child_process";

const DATA_FILE = path.join(process.cwd(), "org-data.json");
const EMPLOYEES_FILE = path.join(process.cwd(), "employees.json");

// Employee record shape:
// { id: string, cargo: string, gerencia: string, nombre: string, cedula: string, fechaIngreso: string, telefono?: string, email?: string, notas?: string }

function loadEmployees(): Record<string, any> {
  if (!fs.existsSync(EMPLOYEES_FILE)) return {};
  try { return JSON.parse(fs.readFileSync(EMPLOYEES_FILE, "utf-8")); } catch { return {}; }
}

function saveEmployees(data: Record<string, any>) {
  fs.writeFileSync(EMPLOYEES_FILE, JSON.stringify(data, null, 2), "utf-8");
}

// Default org data
const DEFAULT_DATA = {
  name: "Junta Directiva",
  gerencia: "root",
  children: [
    {
      name: "CEO",
      gerencia: "root",
      children: [
        { name: "Auditor Externo", gerencia: "staff" },
        { name: "Asesor Externo", gerencia: "staff" },
        {
          name: "Gerencia de Comercialización",
          gerencia: "comercializacion",
          children: [
            {
              name: "Gerencia Comercial Mayor",
              gerencia: "comercializacion",
              children: [
                { name: "Coord. Comercial Mayor Lara-Port-Yar", gerencia: "comercializacion", children: [{ name: "Vendedor Mayor Lara-Port-Yar", gerencia: "comercializacion" }] },
                { name: "Coord. Comercial Mayor Aragua-Carabobo", gerencia: "comercializacion", children: [{ name: "Vendedor Mayor Aragua-Carabobo", gerencia: "comercializacion" }] },
                { name: "Coord. Comercial Caracas", gerencia: "comercializacion", children: [{ name: "Vendedor Mayor Caracas", gerencia: "comercializacion" }] }
              ]
            },
            {
              name: "Gerencia Comercial Proyectos",
              gerencia: "comercializacion",
              children: [
                { name: "Coord. Comercial Proy. Lara-Port-Yar", gerencia: "comercializacion", children: [{ name: "Vendedor Técnico Proy. Lara-Port-Yar", gerencia: "comercializacion" }] },
                { name: "Coord. Comercial Aragua-Carabobo", gerencia: "comercializacion", children: [{ name: "Vendedor Técnico Proy. Aragua-Carabobo", gerencia: "comercializacion" }] }
              ]
            },
            {
              name: "Gerencia Comercial E-commerce",
              gerencia: "comercializacion",
              children: [{ name: "Coord. MercadoLibre/Web/IG/TikTok", gerencia: "comercializacion" }]
            },
            {
              name: "Gerencia de Marketing",
              gerencia: "comercializacion",
              children: [
                { name: "Coordinador de Marketing", gerencia: "comercializacion", children: [
                    { name: "Analista Digital", gerencia: "comercializacion" },
                    { name: "Analista de Contenidos", gerencia: "comercializacion" },
                    { name: "Diseñador Gráfico", gerencia: "comercializacion" }
                  ]
                }
              ]
            },
            {
              name: "Gerencia de Branding",
              gerencia: "comercializacion",
              children: [
                { name: "Coord. Branding Lara-Port-Yar", gerencia: "comercializacion" },
                { name: "Coord. Branding Aragua-Carabobo", gerencia: "comercializacion" },
                { name: "Coord. Branding Caracas", gerencia: "comercializacion" }
              ]
            },
            {
              name: "Gerencia de Atención al Cliente",
              gerencia: "comercializacion",
              children: [
                { name: "Coord. ATC Lara-Port-Yar", gerencia: "comercializacion", children: [{ name: "Analista ATC Lara-Port-Yar", gerencia: "comercializacion" }] },
                { name: "Coord. ATC Aragua-Carabobo", gerencia: "comercializacion", children: [{ name: "Analista ATC Aragua-Carabobo", gerencia: "comercializacion" }] },
                { name: "Coord. ATC Caracas", gerencia: "comercializacion", children: [{ name: "Analista ATC Caracas", gerencia: "comercializacion" }] }
              ]
            }
          ]
        },
        {
          name: "Gerencia de Operaciones",
          gerencia: "operaciones",
          children: [
            { name: "Coordinador de Logística", gerencia: "operaciones", children: [
                { name: "Analista Logística Internacional", gerencia: "operaciones" },
                { name: "Analista Logística Nacional", gerencia: "operaciones" },
                { name: "Analista Logística Tiendas-Clientes", gerencia: "operaciones" },
                { name: "Analista Gestión de Flotas y Equipos", gerencia: "operaciones" }
              ]
            },
            { name: "Coord. Inventarios y Gestión de Almacén", gerencia: "operaciones", children: [
                { name: "Analista Inventarios y Almacén Central", gerencia: "operaciones" }
              ]
            },
            { name: "Coord. Estandarización y Gestión de Procesos", gerencia: "operaciones", children: [
                { name: "Analista Estandarización Lara-Port-Yar", gerencia: "operaciones" },
                { name: "Analista Estandarización Aragua-Carabobo", gerencia: "operaciones" },
                { name: "Analista Estandarización Caracas", gerencia: "operaciones" }
              ]
            },
            { name: "Coord. Infraestructura y Mantenimiento", gerencia: "operaciones", children: [
                { name: "Analista Infraestructura Aragua-Carabobo", gerencia: "operaciones" },
                { name: "Analista Infraestructura Lara-Port-Yar", gerencia: "operaciones" },
                { name: "Analista Infraestructura Caracas", gerencia: "operaciones" }
              ]
            }
          ]
        },
        {
          name: "Gerencia de Finanzas - CFO",
          gerencia: "finanzas",
          children: [
            { name: "Gerencia de Contabilidad", gerencia: "finanzas", children: [
                { name: "Coordinador de Contabilidad", gerencia: "finanzas", children: [
                    { name: "Analista de Tributos", gerencia: "finanzas" },
                    { name: "Analista de Cuentas por Cobrar", gerencia: "finanzas" },
                    { name: "Analista de Cuentas por Pagar", gerencia: "finanzas" },
                    { name: "Analista Nómina", gerencia: "finanzas" }
                  ]
                }
              ]
            },
            { name: "Coord. Análisis y Planificación Financiera", gerencia: "finanzas", children: [
                { name: "Analista Financiero", gerencia: "finanzas" }
              ]
            },
            { name: "Gerencia de Tesorería", gerencia: "finanzas", children: [
                { name: "Coordinador de Tesorería", gerencia: "finanzas", children: [
                    { name: "Analista de Tesorería", gerencia: "finanzas" },
                    { name: "Analista de Riesgo", gerencia: "finanzas" }
                  ]
                },
                { name: "Coord. Especialista de Deuda", gerencia: "finanzas" }
              ]
            },
          ]
        },
        {
          name: "Gerencia de Compras",
          gerencia: "compras",
          children: [
            { name: "Coord. de Compras Stock", gerencia: "compras", children: [
                { name: "Analista Compras Nacionales", gerencia: "compras" },
                { name: "Analista Compras Int. (Norte América)", gerencia: "compras" },
                { name: "Analista Compras Int. (Asia)", gerencia: "compras" }
              ]
            },
            { name: "Coord. Compras Proy/Serv/Mant", gerencia: "compras", children: [
                { name: "Analista PSM", gerencia: "compras" }
              ]
            }
          ]
        },
        {
          name: "Gerencia Tiendas Retail Copikon",
          gerencia: "retail",
          children: [
            { name: "Gerencia Tienda Región 1 (Lara-Port-Yar)", gerencia: "retail", children: [
                { name: "Gerente Tienda Copikon Zona 3 Lara", gerencia: "retail", children: [
                    { name: "Auxiliar Administrativo (Z3)", gerencia: "retail" },
                    { name: "Analista Caja (Z3)", gerencia: "retail" },
                    { name: "Mantenimiento-Infraestructura (Z3)", gerencia: "retail" },
                    { name: "Mensajero (Z3)", gerencia: "retail" },
                    { name: "Analista Inventario Almacén Retail (Z3)", gerencia: "retail" },
                    { name: "Coord. Comercial Tienda Retail (Z3)", gerencia: "retail" },
                    { name: "Vendedores Integrales (Z3)", gerencia: "retail" }
                  ]
                },
                { name: "Gerente Tienda Copikon Atrium Lara", gerencia: "retail", children: [
                    { name: "Auxiliar Administrativo (Atrium)", gerencia: "retail" },
                    { name: "Analista Caja (Atrium)", gerencia: "retail" },
                    { name: "Mantenimiento-Infraestructura (Atrium)", gerencia: "retail" },
                    { name: "Mensajero (Atrium)", gerencia: "retail" },
                    { name: "Analista Inventario Almacén Retail (Atrium)", gerencia: "retail" },
                    { name: "Coord. Comercial Tienda Retail (Atrium)", gerencia: "retail" },
                    { name: "Vendedores Integrales (Atrium)", gerencia: "retail" }
                  ]
                }
              ]
            },
            { name: "Gerente Tienda Copikon Av. Venezuela", gerencia: "retail", children: [
                { name: "Auxiliar Administrativo (Av.Vzla)", gerencia: "retail" },
                { name: "Analista Caja (Av.Vzla)", gerencia: "retail" },
                { name: "Mantenimiento-Infraestructura (Av.Vzla)", gerencia: "retail" },
                { name: "Mensajero (Av.Vzla)", gerencia: "retail" },
                { name: "Analista Inventario Almacén Retail (Av.Vzla)", gerencia: "retail" },
                { name: "Coord. Comercial Tienda Retail (Av.Vzla)", gerencia: "retail" },
                { name: "Vendedores Integrales (Av.Vzla)", gerencia: "retail" }
              ]
            },
            { name: "Gerencia Tienda Región 2 (Aragua-Carabobo)", gerencia: "retail", children: [
                { name: "Auxiliar Administrativo (Aragua-Cab)", gerencia: "retail" },
                { name: "Analista Caja (Aragua-Cab)", gerencia: "retail" },
                { name: "Mantenimiento-Infraestructura (Aragua-Cab)", gerencia: "retail" },
                { name: "Mensajero (Aragua-Cab)", gerencia: "retail" },
                { name: "Analista Inventario Almacén Retail (Aragua-Cab)", gerencia: "retail" },
                { name: "Coord. Comercial Tienda Retail (Aragua-Cab)", gerencia: "retail" },
                { name: "Vendedores Integrales (Aragua-Cab)", gerencia: "retail" }
              ]
            },
            { name: "Gerencia Tienda Región 3 (Caracas)", gerencia: "retail", children: [
                { name: "Auxiliar Administrativo (Caracas)", gerencia: "retail" },
                { name: "Analista Caja (Caracas)", gerencia: "retail" },
                { name: "Mantenimiento-Infraestructura (Caracas)", gerencia: "retail" },
                { name: "Mensajero (Caracas)", gerencia: "retail" },
                { name: "Analista Inventario Almacén Retail (Caracas)", gerencia: "retail" },
                { name: "Coord. Comercial Tienda Retail (Caracas)", gerencia: "retail" },
                { name: "Vendedores Integrales (Caracas)", gerencia: "retail" }
              ]
            }
          ]
        },
        {
          name: "Gerencia IT",
          gerencia: "it",
          children: [{ name: "Coordinador IT", gerencia: "it" }]
        },
        {
          name: "Gerencia Técnica de Proyectos",
          gerencia: "proyectos",
          children: [
            { name: "Coord. Técnico Proy. Generación Eléctrica", gerencia: "proyectos" },
            { name: "Coord. Técnico Proy. (Pantallas/CCTV/Seg/Remod)", gerencia: "proyectos", children: [
                { name: "INGENIERÍA", gerencia: "proyectos", children: [
                    { name: "Ingeniero de Diseño (Cálc/Pres/Planos/BOM)", gerencia: "proyectos" }
                  ]
                },
                { name: "Equipo de Campo", gerencia: "proyectos", children: [
                    { name: "Supervisor de Instalaciones", gerencia: "proyectos", children: [
                        { name: "Técnico Instaladores Senior", gerencia: "proyectos" },
                        { name: "Técnico Instaladores Junior", gerencia: "proyectos" }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
};

function loadData() {
  try {
    if (fs.existsSync(DATA_FILE)) {
      return JSON.parse(fs.readFileSync(DATA_FILE, "utf-8"));
    }
  } catch (e) {}
  return DEFAULT_DATA;
}

function saveData(data: any) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2), "utf-8");
}

export async function registerRoutes(server: Server, app: Express): Promise<Server> {
  // GET org data
  app.get("/api/org", (_req, res) => {
    res.json(loadData());
  });

  // POST save org data
  app.post("/api/org", (req, res) => {
    try {
      const data = req.body;
      if (!data || !data.name) {
        return res.status(400).json({ error: "Datos inválidos" });
      }
      saveData(data);
      res.json({ ok: true });
    } catch (e) {
      res.status(500).json({ error: "Error al guardar" });
    }
  });

  // ── Shared helper: build a standalone HTML file ──────────────────────────
  async function buildStandaloneHTML(): Promise<string> {
    try {
      // 1. Load current org data (from saved file or default)
      const orgData = loadData();

      // 2. Read the client HTML (use dist if built, else dev source)
      const distHtmlPath = path.join(process.cwd(), "dist", "public", "index.html");
      const clientHtmlPath = path.join(process.cwd(), "client", "index.html");
      const htmlPath = fs.existsSync(distHtmlPath) ? distHtmlPath : clientHtmlPath;
      let html = fs.readFileSync(htmlPath, "utf-8");

      // 3. Load pre-downloaded D3.js (279KB, no CDN needed)
      const d3Paths = [
        path.join(process.cwd(), "..", "d3.min.js"),
        path.join(process.cwd(), "d3.min.js"),
        "/home/user/workspace/d3.min.js"
      ];
      let d3Content = "";
      for (const p of d3Paths) {
        if (fs.existsSync(p)) {
          d3Content = fs.readFileSync(p, "utf-8");
          break;
        }
      }

      // 4. Replace D3 CDN script tag with inline D3 (base64 approach)
      // We encode D3 as base64 and decode it at runtime.
      // This completely avoids HTML parser issues with </script> inside JS strings.
      if (d3Content) {
        const D3_CDN_TAG = '<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>';
        if (html.includes(D3_CDN_TAG)) {
          const d3Base64 = Buffer.from(d3Content, 'utf-8').toString('base64');
          // The loader: decodes base64 at runtime and evals D3.
          // Using Function() instead of eval to avoid strict mode issues.
          const d3Loader = `<script id="d3-loader">
(function(){
  var b64 = "${d3Base64}";
  var src = typeof atob !== 'undefined' ? atob(b64) :
    Buffer.from(b64,'base64').toString('utf-8');
  var s = document.createElement('script');
  s.textContent = src;
  document.head.appendChild(s);
})();
</script>`;
          html = html.replace(D3_CDN_TAG, d3Loader);
        }
      }

      // 5. Replace the hardcoded orgData block with current saved data
      // The client HTML has: const orgData = { ... };
      // We find and replace that entire block
      const orgDataStart = html.indexOf("const orgData = {");
      if (orgDataStart !== -1) {
        // Find the matching closing };
        let depth = 0;
        let orgDataEnd = -1;
        for (let i = orgDataStart + "const orgData = ".length; i < html.length; i++) {
          if (html[i] === "{") depth++;
          else if (html[i] === "}") {
            depth--;
            if (depth === 0) {
              orgDataEnd = i + 1; // include the closing }
              // skip optional ;
              if (html[orgDataEnd] === ";") orgDataEnd++;
              break;
            }
          }
        }
        if (orgDataEnd !== -1) {
          const newOrgDataBlock = `const orgData = ${JSON.stringify(orgData, null, 2)};`;
          html = html.slice(0, orgDataStart) + newOrgDataBlock + html.slice(orgDataEnd);
        }
      }

      // 6. Remove __PORT_5000__ token (not needed in standalone)
      html = html.replace(/__PORT_5000__/g, "");

      // 6c. Re-inyectar employees actuales (con perfilRol, cursos, gamificacion)
      // Sobreescribir el window.__EMPLOYEES_DATA__ embebido en el build
      const currentEmployees = loadEmployees();
      const cargoDescPath = path.join(process.cwd(), 'cargo-descriptions.json');
      let cargoDescs = {};
      try { cargoDescs = JSON.parse(fs.readFileSync(cargoDescPath, 'utf-8')); } catch {}
      const freshInjection = `<script>window.__EMPLOYEES_DATA__ = ${JSON.stringify(currentEmployees)};window.__CARGO_DESCRIPTIONS__ = ${JSON.stringify(cargoDescs)};</script>`;
      // Eliminar inyección previa y añadir una nueva actualizada
      html = html.replace(/<script>window.__EMPLOYEES_DATA__[^<]*<\/script>/, freshInjection);

      // 6b. Remove external font <link> tags blocked by catbox.moe CSP
      // catbox CSP: default-src 'self' — blocks api.fontshare.com and fonts.googleapis.com
      // Fonts will fall back gracefully to system sans-serif
      html = html.replace(/<link[^>]*api\.fontshare\.com[^>]*>/g, '');
      html = html.replace(/<link[^>]*fonts\.googleapis\.com[^>]*>/g, '');
      html = html.replace(/<link[^>]*fonts\.gstatic\.com[^>]*>/g, '');

      // 7. Remove or neutralize the fetch('/api/org') init call
      // Since data is already embedded in orgData, just let the fetch fail silently
      // The .catch() fallback in the client already handles this gracefully
      // But to be cleaner, replace the fetch init block to skip the network call:
      html = html.replace(
        /\/\/ Cargar datos desde el servidor al iniciar, luego renderizar\nfetch\([^)]+\)\n\s*\.then\(r => r\.json\(\)\)\n\s*\.then\(data => \{[\s\S]*?\}\)\n\s*\.catch\([\s\S]*?\}\);/,
        `// Standalone export: data already embedded above, render directly
      root.x0 = 0; root.y0 = 0;
      update(root);
      setTimeout(centerTree, 600);`
      );

      return html;
    } catch (e: any) {
      throw e;
    }
  }

  // POST /api/share-gist — actualiza gh-pages con los datos actuales y retorna el link directo
  const GIST_ID = "6c4a55a7e9ced64234037f25b8b2aaad";
  const GIST_FILENAME = "organigrama-copikon.html";
  const PAGES_URL = "https://ajucx25-sudo.github.io/copikon-organigrama-v2/";

  app.post("/api/share-gist", async (_req, res) => {
    try {
      const html = await buildStandaloneHTML();

      // Actualizar el Gist via curl + Python para construir el JSON correctamente
      // Siempre usar process.env primero (token más fresco), fallback a github-config.json
      const host = process.env.GH_HOST || (() => {
        try { return JSON.parse(fs.readFileSync(path.join(process.cwd(), "github-config.json"), "utf-8")).host || ""; } catch { return ""; }
      })() || "agent-proxy.perplexity.ai";
      const token = process.env.GH_ENTERPRISE_TOKEN || (() => {
        try { return JSON.parse(fs.readFileSync(path.join(process.cwd(), "github-config.json"), "utf-8")).token || ""; } catch { return ""; }
      })();
      const apiUrl = `https://${host}/api/v3/gists/${GIST_ID}`;
      const tmpHtmlFile = path.join(os.tmpdir(), `gist-html-${Date.now()}.html`);
      const tmpBodyFile = path.join(os.tmpdir(), `gist-body-${Date.now()}.json`);

      fs.writeFileSync(tmpHtmlFile, html, "utf-8");

      // Paso 1: construir JSON con Python (maneja escaping de HTML correctamente)
      await new Promise<void>((resolve, reject) => {
        const pyScript = `
import json, sys
with open(${JSON.stringify(tmpHtmlFile)}, 'r', encoding='utf-8') as f:
    content = f.read()
body = json.dumps({'files': {${JSON.stringify(GIST_FILENAME)}: {'content': content}}})
with open(${JSON.stringify(tmpBodyFile)}, 'w', encoding='utf-8') as f:
    f.write(body)
print('ok')
`.trim();
        execFile("python3", ["-c", pyScript], (err, stdout, stderr) => {
          try { fs.unlinkSync(tmpHtmlFile); } catch {}
          if (err) return reject(new Error("Python JSON build error: " + (stderr || err.message)));
          resolve();
        });
      });

      // Paso 2: Actualizar rama gh-pages en GitHub vía API (Contents API)
      // Esto actualiza el index.html directamente en la rama gh-pages
      const REPO = "ajucx25-sudo/copikon-organigrama-v2";
      const ghPagesApiUrl = `https://${host}/api/v3/repos/${REPO}/contents/index.html`;

      // Obtener el SHA actual del archivo (necesario para actualizar)
      let fileSha = "";
      await new Promise<void>((resolve) => {
        execFile("curl", [
          "-s",
          "-H", `Authorization: Bearer ${token}`,
          "-H", "Accept: application/vnd.github.v3+json",
          "-G", "--data-urlencode", "ref=gh-pages",
          ghPagesApiUrl
        ], (err, stdout) => {
          try {
            const info = JSON.parse(stdout);
            fileSha = info.sha || "";
          } catch {}
          resolve();
        });
      });

      // Construir el body de actualización con Python (base64 del HTML)
      const tmpUpdateFile = path.join(os.tmpdir(), `ghpages-update-${Date.now()}.json`);
      await new Promise<void>((resolve, reject) => {
        const pyScript = `
import json, base64
with open(${JSON.stringify(tmpBodyFile.replace('gist-body', 'gist-html').replace('.json', '.html'))}, 'r', encoding='utf-8') as f:
    html_content = f.read()
encoded = base64.b64encode(html_content.encode('utf-8')).decode('ascii')
body = {
    'message': 'chore: actualizar organigrama',
    'content': encoded,
    'branch': 'gh-pages'
}
sha = ${JSON.stringify(fileSha)}
if sha:
    body['sha'] = sha
with open(${JSON.stringify(tmpUpdateFile)}, 'w') as f:
    json.dump(body, f)
print('ok')
`.trim();

        // Reconstruir el tmpHtmlFile para usarlo aquí
        const tmpHtmlFile2 = path.join(os.tmpdir(), `gist-html-${Date.now()}.html`);
        fs.writeFileSync(tmpHtmlFile2, html, "utf-8");

        const pyScript2 = `
import json, base64
with open(${JSON.stringify(tmpHtmlFile2)}, 'r', encoding='utf-8') as f:
    html_content = f.read()
encoded = base64.b64encode(html_content.encode('utf-8')).decode('ascii')
body = {
    'message': 'chore: actualizar organigrama',
    'content': encoded,
    'branch': 'gh-pages'
}
sha = ${JSON.stringify(fileSha)}
if sha:
    body['sha'] = sha
with open(${JSON.stringify(tmpUpdateFile)}, 'w') as f:
    json.dump(body, f)
print('ok')
`.trim();
        execFile("python3", ["-c", pyScript2], (err, stdout, stderr) => {
          try { fs.unlinkSync(tmpHtmlFile2); } catch {}
          try { fs.unlinkSync(tmpBodyFile); } catch {}
          if (err) return reject(new Error("Python base64 error: " + (stderr || err.message)));
          resolve();
        });
      });

      // Paso 3: PUT al archivo en gh-pages
      await new Promise<void>((resolve, reject) => {
        const args = [
          "-s", "-o", "/dev/null", "-w", "%{http_code}",
          "-X", "PUT",
          "-H", `Authorization: Bearer ${token}`,
          "-H", "Accept: application/vnd.github.v3+json",
          "-H", "Content-Type: application/json",
          "--data", `@${tmpUpdateFile}`,
          ghPagesApiUrl
        ];
        execFile("curl", args, (err, stdout, stderr) => {
          try { fs.unlinkSync(tmpUpdateFile); } catch {}
          if (err) return reject(new Error(stderr || err.message));
          const code = parseInt(stdout.trim(), 10);
          if (code < 200 || code >= 300) return reject(new Error(`GitHub Pages API HTTP ${code}`));
          resolve();
        });
      });

      res.json({ ok: true, url: PAGES_URL });
    } catch (e: any) {
      console.error("Share-gist error:", e);
      res.status(500).json({ error: "Error al actualizar el link: " + e.message });
    }
  });

  // GET /api/export-html — download as file
  app.get("/api/export-html", async (_req, res) => {
    try {
      const html = await buildStandaloneHTML();
      res.setHeader("Content-Type", "text/html; charset=utf-8");
      res.setHeader("Content-Disposition", 'attachment; filename="organigrama-copikon.html"');
      res.send(html);
    } catch (e: any) {
      console.error("Export error:", e);
      res.status(500).json({ error: "Error al exportar: " + e.message });
    }
  });

  // POST /api/share — save snapshot locally, return served URL
  // Snapshots are stored in <cwd>/shares/ and served via GET /api/share/:id
  const SHARES_DIR = path.join(process.cwd(), "shares");
  if (!fs.existsSync(SHARES_DIR)) fs.mkdirSync(SHARES_DIR, { recursive: true });

  app.post("/api/share", async (req, res) => {
    try {
      const html = await buildStandaloneHTML();
      const id = crypto.randomBytes(6).toString("hex");
      const shareFile = path.join(SHARES_DIR, `${id}.html`);
      fs.writeFileSync(shareFile, html, "utf-8");

      // Return a relative path — the frontend prepends API_BASE automatically
      // so the full URL becomes: https://.../port/5000/api/share/<id>
      // This works both locally and deployed.
      res.json({ ok: true, url: `/api/share/${id}` });
    } catch (e: any) {
      console.error("Share error:", e);
      res.status(500).json({ error: "Error al compartir: " + e.message });
    }
  });

  // ===== EMPLOYEES API =====

  // GET /api/employees — all employee records (keyed by cargo ID)
  app.get("/api/employees", (_req, res) => {
    res.json(loadEmployees());
  });

  // GET /api/employees/:id — single employee record
  app.get("/api/employees/:id", (req, res) => {
    const employees = loadEmployees();
    const record = employees[req.params.id];
    if (!record) return res.status(404).json({ error: "No encontrado" });
    res.json(record);
  });

  // PUT /api/employees/:id — create or update employee record
  app.put("/api/employees/:id", (req, res) => {
    const employees = loadEmployees();
    const id = req.params.id;
    const existing = employees[id] || {};
    employees[id] = { ...existing, ...req.body, id };
    saveEmployees(employees);
    res.json({ ok: true, record: employees[id] });
  });

  // DELETE /api/employees/:id — clear employee data for a cargo
  app.delete("/api/employees/:id", (req, res) => {
    const employees = loadEmployees();
    delete employees[req.params.id];
    saveEmployees(employees);
    res.json({ ok: true });
  });

  // GET /api/share/:id — serve saved snapshot HTML
  app.get("/api/share/:id", (req, res) => {
    const id = req.params.id.replace(/[^a-f0-9]/g, ""); // sanitize
    const shareFile = path.join(SHARES_DIR, `${id}.html`);
    if (!fs.existsSync(shareFile)) {
      return res.status(404).send("<html><body><h2>Link no encontrado o expirado.</h2></body></html>");
    }
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.setHeader("Cache-Control", "public, max-age=86400");
    res.send(fs.readFileSync(shareFile, "utf-8"));
  });


  // ── CHAT INTERNO (JSON storage) ──────────────────────
  (() => {
    const CHAT_USERS_FILE = path.join(__dirname, "..", "chat-users.json");
    const CHAT_MSGS_FILE  = path.join(__dirname, "..", "chat-messages.json");

    function loadCU(): any[] { try { return JSON.parse(fs.readFileSync(CHAT_USERS_FILE,"utf-8")); } catch { return []; } }
    function saveCU(d: any[]) { fs.writeFileSync(CHAT_USERS_FILE, JSON.stringify(d,null,2),"utf-8"); }
    function loadCM(): any[] { try { return JSON.parse(fs.readFileSync(CHAT_MSGS_FILE,"utf-8")); } catch { return []; } }
    function saveCM(d: any[]) { fs.writeFileSync(CHAT_MSGS_FILE, JSON.stringify(d,null,2),"utf-8"); }
    function nextId(arr: any[]): number { return arr.length ? Math.max(...arr.map((x:any)=>x.id||0))+1 : 1; }

    const sseClients: Map<number, any[]> = new Map();
    function broadcastChat(toId: number, data: object) {
      (sseClients.get(toId)||[]).forEach((res:any) => { try { res.write(`data: ${JSON.stringify(data)}\n\n`); } catch {} });
    }

    app.post("/api/chat/register", (req, res) => {
      const { username, password, nombre, cargo, gerencia, cargoId } = req.body;
      if (!username||!password||!nombre||!cargo||!gerencia) return res.status(400).json({error:"Faltan campos"});
      const users = loadCU();
      if (users.find((u:any)=>u.username===username)) return res.status(409).json({error:"El usuario ya existe"});
      const user = { id:nextId(users), username, password, nombre, cargo, gerencia, cargoId:cargoId||"", online:false, lastSeen:null, createdAt:new Date().toISOString() };
      users.push(user); saveCU(users);
      const { password:_, ...safe } = user;
      res.json(safe);
    });

    app.post("/api/chat/login", (req, res) => {
      const { username, password } = req.body;
      const users = loadCU();
      const user = users.find((u:any)=>u.username===username);
      if (!user||user.password!==password) return res.status(401).json({error:"Usuario o contraseña incorrectos"});
      user.online=true; user.lastSeen=new Date().toISOString(); saveCU(users);
      const { password:_, ...safe } = user;
      res.json(safe);
    });

    app.post("/api/chat/logout", (req, res) => {
      const { userId } = req.body;
      if (userId) { const users=loadCU(); const u=users.find((x:any)=>x.id===Number(userId)); if(u){u.online=false;u.lastSeen=new Date().toISOString();saveCU(users);} }
      res.json({ok:true});
    });

    app.get("/api/chat/users", (_req, res) => {
      res.json(loadCU().map(({password:_,...u}:any)=>u));
    });

    app.get("/api/chat/messages/:uid1/:uid2", (req, res) => {
      const u1=Number(req.params.uid1), u2=Number(req.params.uid2);
      const msgs = loadCM();
      const conv = msgs.filter((m:any)=>(m.fromId===u1&&m.toId===u2)||(m.fromId===u2&&m.toId===u1));
      // mark read
      let dirty=false;
      msgs.forEach((m:any)=>{ if(m.fromId===u2&&m.toId===u1&&!m.read){m.read=true;dirty=true;} });
      if(dirty) saveCM(msgs);
      res.json(conv);
    });

    app.post("/api/chat/messages", (req, res) => {
      const { fromId, toId, content } = req.body;
      if (!fromId||!toId||!content) return res.status(400).json({error:"Faltan campos"});
      const msgs = loadCM();
      const msg = { id:nextId(msgs), fromId:Number(fromId), toId:Number(toId), content, createdAt:new Date().toISOString(), read:false };
      msgs.push(msg); saveCM(msgs);
      broadcastChat(Number(toId), {type:"message",message:msg});
      broadcastChat(Number(fromId), {type:"message_sent",message:msg});
      res.json(msg);
    });

    app.get("/api/chat/unread/:userId", (req, res) => {
      const uid=Number(req.params.userId);
      const counts:Record<number,number>={};
      loadCM().filter((m:any)=>m.toId===uid&&!m.read).forEach((m:any)=>{ counts[m.fromId]=(counts[m.fromId]||0)+1; });
      res.json(counts);
    });

    app.post("/api/chat/read", (req, res) => {
      const { fromId, toId } = req.body;
      const msgs=loadCM(); let dirty=false;
      msgs.forEach((m:any)=>{ if(m.fromId===Number(fromId)&&m.toId===Number(toId)&&!m.read){m.read=true;dirty=true;} });
      if(dirty) saveCM(msgs);
      broadcastChat(Number(fromId),{type:"read",byId:toId});
      res.json({ok:true});
    });

    app.get("/api/chat/sse/:userId", (req, res) => {
      const userId=Number(req.params.userId);
      res.setHeader("Content-Type","text/event-stream");
      res.setHeader("Cache-Control","no-cache");
      res.setHeader("Connection","keep-alive");
      res.flushHeaders();
      if(!sseClients.has(userId)) sseClients.set(userId,[]);
      sseClients.get(userId)!.push(res);
      const users=loadCU(); const u=users.find((x:any)=>x.id===userId);
      if(u){u.online=true;u.lastSeen=new Date().toISOString();saveCU(users);}
      const hb=setInterval(()=>{ try{res.write(": hb\n\n");}catch{} },25000);
      req.on("close",()=>{
        clearInterval(hb);
        sseClients.set(userId,(sseClients.get(userId)||[]).filter((r:any)=>r!==res));
        if(!(sseClients.get(userId)||[]).length){
          const us=loadCU(); const uu=us.find((x:any)=>x.id===userId);
          if(uu){uu.online=false;uu.lastSeen=new Date().toISOString();saveCU(us);}
        }
      });
    });
  })();


  // ── Grupos de WhatsApp ────────────────────────────────
  const WA_GROUPS_FILE = path.join(__dirname, "..", "wa-groups.json");
  function loadWaGroups(): Record<string,string> {
    try { return JSON.parse(fs.readFileSync(WA_GROUPS_FILE,"utf-8")); } catch { return {}; }
  }
  app.get("/api/wa-groups", (_req, res) => res.json(loadWaGroups()));
  app.post("/api/wa-groups", (req, res) => {
    const data = req.body || {};
    fs.writeFileSync(WA_GROUPS_FILE, JSON.stringify(data, null, 2), "utf-8");
    res.json({ ok: true });
  });


  // ── AUTH PORTAL DEL EMPLEADO ──────────────────────
  // Usuarios hardcoded como base — siempre disponibles
  const HARDCODED_USERS: Record<string, any> = {
    admin: { username:"admin", password:"copikon2026", cargoId:"ceo", cargo:"CEO", gerencia:"root", nombre:"Administrador", role:"admin" }
  };
  const PORTAL_USERS_FILE = (() => {
    const candidates = [
      path.join(process.cwd(), "portal-users.json"),
      path.join(__dirname, "..", "portal-users.json"),
      path.join(__dirname, "..", "public", "portal-users.json"),
      path.join(__dirname, "portal-users.json"),
    ];
    for (const c of candidates) { if (fs.existsSync(c)) return c; }
    return candidates[0];
  })();
  function loadPortalUsers(): Record<string, any> {
    try {
      const data = JSON.parse(fs.readFileSync(PORTAL_USERS_FILE, "utf-8"));
      // Siempre fusionar con hardcoded para garantizar que admin exista
      return { ...HARDCODED_USERS, ...data };
    } catch {
      return { ...HARDCODED_USERS };
    }
  }
  function savePortalUsers(d: Record<string, any>) {
    try { fs.writeFileSync(PORTAL_USERS_FILE, JSON.stringify(d, null, 2), "utf-8"); } catch {}
  }

  // Login del portal
  app.post("/api/portal/login", (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) return res.status(400).json({ error: "Faltan credenciales" });
    const users = loadPortalUsers();
    const user = users[username];
    if (!user || user.password !== password) return res.status(401).json({ error: "Usuario o contraseña incorrectos" });
    const { password: _, ...safe } = user;
    res.json(safe);
  });

  // Crear/actualizar usuario del portal (solo admin)
  app.post("/api/portal/users", (req, res) => {
    const { adminKey, username, password, cargoId, cargo, gerencia, nombre } = req.body;
    if (adminKey !== "copikon2026admin") return res.status(403).json({ error: "No autorizado" });
    if (!username || !password || !cargoId) return res.status(400).json({ error: "Faltan campos" });
    const users = loadPortalUsers();
    users[username] = { username, password, cargoId, cargo: cargo || "", gerencia: gerencia || "", nombre: nombre || "", role: "empleado" };
    savePortalUsers(users);
    res.json({ ok: true });
  });

  // Listar usuarios del portal (solo admin)
  app.get("/api/portal/users", (req, res) => {
    const users = loadPortalUsers();
    const safe = Object.values(users).map(({ password: _, ...u }: any) => u);
    res.json(safe);
  });

  // Eliminar usuario del portal
  app.delete("/api/portal/users/:username", (req, res) => {
    const { adminKey } = req.body;
    if (adminKey !== "copikon2026admin") return res.status(403).json({ error: "No autorizado" });
    const users = loadPortalUsers();
    delete users[req.params.username];
    savePortalUsers(users);
    res.json({ ok: true });
  });


  // ══════════════════════════════════════════════════════
  // INTRANET — Chat 1a1, Canales, Project Manager
  // ══════════════════════════════════════════════════════
  {
    const INTRANET_MSGS_FILE  = path.join(process.cwd(), "intranet-messages.json");
    const INTRANET_CHAN_FILE   = path.join(process.cwd(), "intranet-channels.json");
    const INTRANET_PROJ_FILE  = path.join(process.cwd(), "intranet-projects.json");

    function readJSON(file: string, def: any = {}) {
      try { return JSON.parse(fs.readFileSync(file, "utf-8")); } catch { return def; }
    }
    function writeJSON(file: string, data: any) {
      fs.writeFileSync(file, JSON.stringify(data, null, 2), "utf-8");
    }

    // Init vacíos
    if (!fs.existsSync(INTRANET_MSGS_FILE))  writeJSON(INTRANET_MSGS_FILE, []);
    if (!fs.existsSync(INTRANET_PROJ_FILE))  writeJSON(INTRANET_PROJ_FILE, []);

    // SSE clients
    const sseClients: Map<string, any[]> = new Map();
    function sseNotify(userId: string, event: string, data: any) {
      const payload = `data: ${JSON.stringify({ event, data })}\n\n`;
      (sseClients.get(userId) || []).forEach(r => { try { r.write(payload); } catch {} });
    }
    function sseBroadcast(userIds: string[], event: string, data: any) {
      userIds.forEach(uid => sseNotify(uid, event, data));
    }

    let _seq = Date.now();
    function nextId() { return (++_seq).toString(36); }

    // ── Canales por defecto ───────────────────────────────
    const GER_COLORS: Record<string,string> = {
      root:"#1a3a6b", comercializacion:"#4a7fd4", operaciones:"#e8a020",
      finanzas:"#3cb371", retail:"#a06ad4", it:"#5b8ff9",
      proyectos:"#dd6874", compras:"#f0a050", staff:"#6b7a99", general:"#2bbfae"
    };
    function ensureChannels() {
      const ch: any[] = readJSON(INTRANET_CHAN_FILE, []);
      if (ch.length) return ch;
      const defaults = [
        { id:"general",         name:"General",         gerencia:"general",         desc:"Canal para toda la empresa" },
        { id:"comercializacion",name:"Comercialización", gerencia:"comercializacion", desc:"Equipo comercial" },
        { id:"operaciones",     name:"Operaciones",      gerencia:"operaciones",      desc:"Equipo de operaciones" },
        { id:"finanzas",        name:"Finanzas",         gerencia:"finanzas",         desc:"Equipo financiero" },
        { id:"compras",         name:"Compras",          gerencia:"compras",          desc:"Equipo de compras" },
        { id:"retail",          name:"Retail",           gerencia:"retail",           desc:"Tiendas Retail Copikon" },
        { id:"it",              name:"IT",               gerencia:"it",               desc:"Equipo de tecnología" },
        { id:"proyectos",       name:"Proyectos",        gerencia:"proyectos",        desc:"Gerencia técnica de proyectos" },
      ];
      writeJSON(INTRANET_CHAN_FILE, defaults);
      return defaults;
    }

    // ── Auth (reutiliza portal-users.json) ────────────────
    app.post("/api/intranet/auth/login", (req, res) => {
      const { username, password } = req.body;
      const users = loadPortalUsers();
      const user = users[username];
      if (!user || user.password !== password)
        return res.status(401).json({ error: "Usuario o contraseña incorrectos" });
      const { password: _, ...safe } = user;
      res.json(safe);
    });

    app.get("/api/intranet/auth/users", (_req, res) => {
      const users = loadPortalUsers();
      const list = Object.values(users).map(({ password: _, ...u }: any) => u);
      res.json(list);
    });

    // ── Chat 1a1 ──────────────────────────────────────────
    app.get("/api/intranet/chat/messages/:a/:b", (req, res) => {
      const { a, b } = req.params;
      const convId = [a, b].sort().join("__");
      const msgs: any[] = readJSON(INTRANET_MSGS_FILE, []);
      res.json(msgs.filter((m: any) => m.convId === convId));
    });

    app.post("/api/intranet/chat/messages", (req, res) => {
      const { from, to, text } = req.body;
      if (!from || !to || !text?.trim()) return res.status(400).json({ error: "Faltan campos" });
      const convId = [from, to].sort().join("__");
      const msg = { id: nextId(), convId, from, to, text: text.trim(), ts: Date.now(), read: false };
      const msgs: any[] = readJSON(INTRANET_MSGS_FILE, []);
      msgs.push(msg);
      writeJSON(INTRANET_MSGS_FILE, msgs);
      sseNotify(to,   "new_message", msg);
      sseNotify(from, "new_message", msg);
      res.json(msg);
    });

    app.post("/api/intranet/chat/read", (req, res) => {
      const { convId, userId } = req.body;
      const msgs: any[] = readJSON(INTRANET_MSGS_FILE, []);
      msgs.forEach((m: any) => { if (m.convId === convId && m.to === userId) m.read = true; });
      writeJSON(INTRANET_MSGS_FILE, msgs);
      res.json({ ok: true });
    });

    app.get("/api/intranet/chat/unread/:userId", (req, res) => {
      const msgs: any[] = readJSON(INTRANET_MSGS_FILE, []);
      const counts: Record<string, number> = {};
      msgs.filter((m: any) => m.to === req.params.userId && !m.read)
          .forEach((m: any) => { counts[m.from] = (counts[m.from] || 0) + 1; });
      res.json(counts);
    });

    // ── Canales ────────────────────────────────────────────
    app.get("/api/intranet/channels", (_req, res) => {
      res.json(ensureChannels().map((c: any) => ({ ...c, color: GER_COLORS[c.gerencia] || "#888" })));
    });

    app.get("/api/intranet/channels/:channelId/messages", (req, res) => {
      const msgs: any[] = readJSON(INTRANET_MSGS_FILE, []);
      res.json(msgs.filter((m: any) => m.channelId === req.params.channelId).slice(-200));
    });

    app.post("/api/intranet/channels/:channelId/messages", (req, res) => {
      const { from, text } = req.body;
      const { channelId } = req.params;
      if (!from || !text?.trim()) return res.status(400).json({ error: "Faltan campos" });
      const msg = { id: nextId(), channelId, from, text: text.trim(), ts: Date.now() };
      const msgs: any[] = readJSON(INTRANET_MSGS_FILE, []);
      msgs.push(msg);
      writeJSON(INTRANET_MSGS_FILE, msgs);
      const users = loadPortalUsers();
      sseBroadcast(Object.keys(users), "channel_message", msg);
      res.json(msg);
    });

    // ── SSE ────────────────────────────────────────────────
    app.get("/api/intranet/sse/:userId", (req, res) => {
      const { userId } = req.params;
      res.setHeader("Content-Type", "text/event-stream");
      res.setHeader("Cache-Control", "no-cache");
      res.setHeader("Connection", "keep-alive");
      res.setHeader("X-Accel-Buffering", "no");
      res.flushHeaders();
      res.write(`data: ${JSON.stringify({ event: "connected", data: { userId } })}\n\n`);
      const clients = sseClients.get(userId) || [];
      clients.push(res);
      sseClients.set(userId, clients);
      const ping = setInterval(() => { try { res.write(": ping\n\n"); } catch {} }, 25000);
      req.on("close", () => {
        clearInterval(ping);
        sseClients.set(userId, (sseClients.get(userId) || []).filter((r: any) => r !== res));
      });
    });

    // ── Projects ───────────────────────────────────────────
    app.get("/api/intranet/projects", (_req, res) => {
      res.json(readJSON(INTRANET_PROJ_FILE, []));
    });

    app.post("/api/intranet/projects", (req, res) => {
      const { name, desc, color, owner, members } = req.body;
      if (!name?.trim()) return res.status(400).json({ error: "Nombre requerido" });
      const projects: any[] = readJSON(INTRANET_PROJ_FILE, []);
      const proj = { id: nextId(), name: name.trim(), desc: desc || "", color: color || "#4a7fd4",
        owner, members: members || [], createdAt: Date.now(), tasks: [] };
      projects.push(proj);
      writeJSON(INTRANET_PROJ_FILE, projects);
      res.json(proj);
    });

    app.put("/api/intranet/projects/:id", (req, res) => {
      const projects: any[] = readJSON(INTRANET_PROJ_FILE, []);
      const idx = projects.findIndex((p: any) => p.id === req.params.id);
      if (idx === -1) return res.status(404).json({ error: "No encontrado" });
      projects[idx] = { ...projects[idx], ...req.body, id: req.params.id };
      writeJSON(INTRANET_PROJ_FILE, projects);
      res.json(projects[idx]);
    });

    app.delete("/api/intranet/projects/:id", (req, res) => {
      const projects: any[] = readJSON(INTRANET_PROJ_FILE, []).filter((p: any) => p.id !== req.params.id);
      writeJSON(INTRANET_PROJ_FILE, projects);
      res.json({ ok: true });
    });

    app.get("/api/intranet/projects/:id/tasks", (req, res) => {
      const proj = readJSON(INTRANET_PROJ_FILE, []).find((p: any) => p.id === req.params.id);
      if (!proj) return res.status(404).json({ error: "No encontrado" });
      res.json(proj.tasks || []);
    });

    app.post("/api/intranet/projects/:id/tasks", (req, res) => {
      const { title, desc, assignee, priority, dueDate, status } = req.body;
      if (!title?.trim()) return res.status(400).json({ error: "Título requerido" });
      const projects: any[] = readJSON(INTRANET_PROJ_FILE, []);
      const proj = projects.find((p: any) => p.id === req.params.id);
      if (!proj) return res.status(404).json({ error: "No encontrado" });
      const task = { id: nextId(), title: title.trim(), desc: desc || "",
        assignee: assignee || null, priority: priority || "media",
        dueDate: dueDate || null, status: status || "pendiente",
        createdAt: Date.now(), comments: [] };
      proj.tasks = [...(proj.tasks || []), task];
      writeJSON(INTRANET_PROJ_FILE, projects);
      if (assignee) sseNotify(assignee, "task_assigned", { task, projectId: req.params.id, projectName: proj.name });
      res.json(task);
    });

    app.put("/api/intranet/projects/:projId/tasks/:taskId", (req, res) => {
      const projects: any[] = readJSON(INTRANET_PROJ_FILE, []);
      const proj = projects.find((p: any) => p.id === req.params.projId);
      if (!proj) return res.status(404).json({ error: "No encontrado" });
      const ti = (proj.tasks || []).findIndex((t: any) => t.id === req.params.taskId);
      if (ti === -1) return res.status(404).json({ error: "No encontrado" });
      proj.tasks[ti] = { ...proj.tasks[ti], ...req.body, id: req.params.taskId };
      writeJSON(INTRANET_PROJ_FILE, projects);
      res.json(proj.tasks[ti]);
    });

    app.delete("/api/intranet/projects/:projId/tasks/:taskId", (req, res) => {
      const projects: any[] = readJSON(INTRANET_PROJ_FILE, []);
      const proj = projects.find((p: any) => p.id === req.params.projId);
      if (!proj) return res.status(404).json({ error: "No encontrado" });
      proj.tasks = (proj.tasks || []).filter((t: any) => t.id !== req.params.taskId);
      writeJSON(INTRANET_PROJ_FILE, projects);
      res.json({ ok: true });
    });

    app.post("/api/intranet/projects/:projId/tasks/:taskId/comments", (req, res) => {
      const { from, text } = req.body;
      if (!text?.trim()) return res.status(400).json({ error: "Texto requerido" });
      const projects: any[] = readJSON(INTRANET_PROJ_FILE, []);
      const proj = projects.find((p: any) => p.id === req.params.projId);
      if (!proj) return res.status(404).json({ error: "No encontrado" });
      const task = (proj.tasks || []).find((t: any) => t.id === req.params.taskId);
      if (!task) return res.status(404).json({ error: "No encontrado" });
      const comment = { id: nextId(), from, text: text.trim(), ts: Date.now() };
      task.comments = [...(task.comments || []), comment];
      writeJSON(INTRANET_PROJ_FILE, projects);
      res.json(comment);
    });

    // ── Servir frontend de la intranet en /intranet ────────
    app.use("/intranet", express.static(path.join(process.cwd(), "dist", "public", "intranet")));
    app.get("/intranet", (_req, res) => {
      res.sendFile(path.join(process.cwd(), "dist", "public", "intranet", "index.html"));
    });
    app.get("/intranet/{*path}", (_req, res) => {
      res.sendFile(path.join(process.cwd(), "dist", "public", "intranet", "index.html"));
    });
  }

  return server;
}

// ═══════════════════════════════════════════════════════
// CHAT INTERNO — rutas integradas en el mismo servidor
