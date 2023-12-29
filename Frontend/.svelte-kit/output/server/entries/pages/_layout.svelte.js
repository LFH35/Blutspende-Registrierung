import { c as create_ssr_component } from "../../chunks/ssr.js";
const css = {
  code: "@import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap');:root{margin:0;padding:0;font-family:'Ubuntu', sans-serif;--main-background-color:#D97E7E;--main-bloody-red-color:#A60F0F;--main-dark-red-color:#590202;--main-light-blue-color:#3DE0F2;--main-blue-color:#0CB1F2;--main-dark-blue-color:#0B508C;--main-white-color:white;--main-light-grey-color:#737373;--main-grey-color:#595959;--main-light-green-color:#94BF36;--main-green-color:#375915}body.svelte-tvq6f{margin:auto;width:100vw;height:100vh;background-color:var(--main-background-color);display:flex;justify-content:center;align-items:center}.Blood-LeftBottom.svelte-tvq6f{position:absolute;left:0;bottom:0}.Blood-RightTop.svelte-tvq6f{position:absolute;right:0;top:0}main.svelte-tvq6f{z-index:10;background-color:var(--main-white-color);display:flex;flex-direction:column;align-items:center;color:var(--main-bloody-red-color);width:375px;height:700px;border-radius:25px}@media(max-width: 768px){main.svelte-tvq6f{width:100vw;height:100vh;margin:auto}.Blood-LeftBottom.svelte-tvq6f,.Blood-RightTop.svelte-tvq6f{visibility:hidden}}",
  map: null
};
const Layout = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  $$result.css.add(css);
  return `<body class="svelte-tvq6f"><img src="/img/Blood-LeftBottom.svg" alt="Bloot Left Bottom" class="Blood-LeftBottom svelte-tvq6f"> <main class="svelte-tvq6f">${slots.default ? slots.default({}) : ``}</main> <img src="/img/Blood-RightTop.svg" alt="Blood Right Top" class="Blood-RightTop svelte-tvq6f"> </body>`;
});
export {
  Layout as default
};
