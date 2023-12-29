

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.CeB0Dgh0.js","_app/immutable/chunks/scheduler.Smq_RA6i.js","_app/immutable/chunks/index.BamsqFJs.js","_app/immutable/chunks/singletons.R8eMLXe1.js"];
export const stylesheets = [];
export const fonts = [];
