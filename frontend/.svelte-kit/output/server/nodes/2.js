

export const index = 2;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/2.sQlUwMgp.js","_app/immutable/chunks/scheduler.Smq_RA6i.js","_app/immutable/chunks/index.BamsqFJs.js"];
export const stylesheets = ["_app/immutable/assets/2.GRaVAQNM.css"];
export const fonts = [];
