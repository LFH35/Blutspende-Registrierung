

export const index = 4;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/question/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/4.ujTkdV4F.js","_app/immutable/chunks/scheduler.Smq_RA6i.js","_app/immutable/chunks/index.BamsqFJs.js"];
export const stylesheets = ["_app/immutable/assets/4.dstgCF7H.css"];
export const fonts = [];
