import { readFile } from "node:fs/promises";

const projects = JSON.parse(await readFile(new URL("../data/projects.json", import.meta.url), "utf8"));
if (!Array.isArray(projects) || projects.length === 0) throw new Error("projects.json must contain at least one project");

const required = ["slug", "name", "repo", "github_url", "website_url", "category", "summary_zh", "source_url", "signal", "stars_snapshot", "language", "license", "checked_at"];
const slugs = new Set();
const repos = new Set();

for (const [index, project] of projects.entries()) {
  for (const key of required) if (!(key in project)) throw new Error(`Entry ${index + 1} is missing ${key}`);
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(project.slug)) throw new Error(`Invalid slug: ${project.slug}`);
  if (!/^https:\/\/github\.com\//.test(project.github_url)) throw new Error(`Invalid GitHub URL: ${project.github_url}`);
  if (!/^https:\/\/jianailab\.com\/projects\//.test(project.website_url)) throw new Error(`Invalid site URL: ${project.website_url}`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(project.checked_at)) throw new Error(`Invalid checked_at: ${project.checked_at}`);
  if (!Number.isInteger(project.stars_snapshot) || project.stars_snapshot < 0) throw new Error(`Invalid stars snapshot: ${project.repo}`);
  const repoKey = project.repo.toLowerCase();
  if (slugs.has(project.slug)) throw new Error(`Duplicate slug: ${project.slug}`);
  if (repos.has(repoKey)) throw new Error(`Duplicate repo: ${project.repo}`);
  slugs.add(project.slug);
  repos.add(repoKey);
}

console.log(`Validated ${projects.length} projects.`);
