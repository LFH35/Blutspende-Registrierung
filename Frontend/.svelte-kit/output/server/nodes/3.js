

export const index = 3;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/appointments/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/3.RLIk4Yrn.js","_app/immutable/chunks/scheduler.Smq_RA6i.js","_app/immutable/chunks/index.BamsqFJs.js"];
export const stylesheets = [];
export const fonts = [];
