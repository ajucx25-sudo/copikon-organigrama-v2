import { build as esbuild } from "esbuild";
import { build as viteBuild } from "vite";
import { rm, readFile, writeFile, access } from "fs/promises";

// server deps to bundle to reduce openat(2) syscalls
// which helps cold start times
const allowlist = [
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
  let htmlContent = await readFile(htmlPath, "utf-8");
  const injection = `<script>window.__EMPLOYEES_DATA__ = ${JSON.stringify(employeesData)};</script>`;
  htmlContent = htmlContent.replace('</head>', injection + '</head>');
  await writeFile(htmlPath, htmlContent, "utf-8");
  console.log(`injected ${Object.keys(employeesData).length} employee records`);

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
