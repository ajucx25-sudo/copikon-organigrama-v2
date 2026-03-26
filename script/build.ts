import { build as esbuild } from "esbuild";
import { build as viteBuild } from "vite";
import { rm, readFile, writeFile, access } from "fs/promises";

// server deps to bundle to reduce openat(2) syscalls
// which helps cold start times
const allowlist = [
  "better-sqlite3",
  "@google/generative-ai",
  "axios",
  "connect-pg-simple",
  "cors",
  "date-fns",
  "drizzle-orm",
  "drizzle-zod",
  "express",
  "express-rate-limit",
  "express-session",
  "jsonwebtoken",
  "memorystore",
  "multer",
  "nanoid",
  "nodemailer",
  "openai",
  "passport",
  "passport-local",
  "pg",
  "stripe",
  "uuid",
  "ws",
  "xlsx",
  "zod",
  "zod-validation-error",
];

async function buildAll() {
  await rm("dist", { recursive: true, force: true });

  console.log("building client...");
  await viteBuild();

  // Inyectar datos de empleados en el HTML generado
  console.log("injecting employees data...");
  const htmlPath = "dist/public/index.html";
  let employeesData = {};
  try {
    await access("employees.json");
    employeesData = JSON.parse(await readFile("employees.json", "utf-8"));
  } catch(e) {
    employeesData = {};
  }
  let cargoDescriptions = {};
  try {
    await access("cargo-descriptions.json");
    cargoDescriptions = JSON.parse(await readFile("cargo-descriptions.json", "utf-8"));
  } catch(e) {
    cargoDescriptions = {};
  }
  let htmlContent = await readFile(htmlPath, "utf-8");
  // Leer portal-users.json para inyectar en el organigrama (login offline)
  let portalUsers: any = {};
  try { portalUsers = JSON.parse(await readFile("portal-users.json", "utf-8")); } catch {}
  const injection = `<script>window.__EMPLOYEES_DATA__ = ${JSON.stringify(employeesData)};window.__CARGO_DESCRIPTIONS__ = ${JSON.stringify(cargoDescriptions)};window.__PORTAL_USERS__ = ${JSON.stringify(portalUsers)};</script>`;
  htmlContent = htmlContent.replace('</head>', injection + '</head>');
  await writeFile(htmlPath, htmlContent, "utf-8");
  console.log(`injected ${Object.keys(employeesData).length} employee records, ${Object.keys(portalUsers).length} portal users`);

  // Inyectar proyectos en el HTML de la intranet
  const intranetHtmlPath = "dist/public/intranet/index.html";
  try {
    let intranetHtml = await readFile(intranetHtmlPath, "utf-8");
    // Leer proyectos del org-data.json
    let intranetProjects: any[] = [];
    try {
      const orgData = JSON.parse(await readFile("org-data.json", "utf-8"));
      intranetProjects = orgData.__intranetProjects || [];
    } catch {}
    const intranetInjection = `<script>window.__INTRANET_PROJECTS__ = ${JSON.stringify(intranetProjects)};</script>`;
    intranetHtml = intranetHtml.replace('</head>', intranetInjection + '</head>');
    await writeFile(intranetHtmlPath, intranetHtml, "utf-8");
    console.log(`injected ${intranetProjects.length} intranet projects into intranet/index.html`);
  } catch(e) { console.warn("No se pudo inyectar proyectos en intranet:", e); }

  console.log("building server...");
  const pkg = JSON.parse(await readFile("package.json", "utf-8"));
  const allDeps = [
    ...Object.keys(pkg.dependencies || {}),
    ...Object.keys(pkg.devDependencies || {}),
  ];
  const externals = allDeps.filter((dep) => !allowlist.includes(dep));

  await esbuild({
    entryPoints: ["server/index.ts"],
    platform: "node",
    bundle: true,
    format: "cjs",
    outfile: "dist/index.cjs",
    define: {
      "process.env.NODE_ENV": '"production"',
    },
    minify: true,
    external: externals,
    logLevel: "info",
  });
}

buildAll().catch((err) => {
  console.error(err);
  process.exit(1);
});
