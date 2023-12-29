import { c as create_ssr_component } from "../../chunks/ssr.js";
const css = {
  code: ".input-style1.svelte-1ky3pnk.svelte-1ky3pnk{width:100%;color:var(--main-bloody-red-color);font-size:large;font-weight:500;border:none;border-bottom:3px solid var(--main-bloody-red-color)}.input-style1.svelte-1ky3pnk.svelte-1ky3pnk:focus{outline:none}.btn-style1.svelte-1ky3pnk.svelte-1ky3pnk{border:none;text-align:center;color:white;background-color:var(--main-bloody-red-color);border:4px solid var(--main-bloody-red-color);padding:20px;border-radius:5px;text-decoration:none;font-weight:bold;font-size:large;transition:background-color 0.5s ease;cursor:pointer}.btn-style1.svelte-1ky3pnk.svelte-1ky3pnk:hover{background-color:var(--main-white-color);color:var(--main-bloody-red-color)}.box.svelte-1ky3pnk.svelte-1ky3pnk{width:80%;height:100%;padding:50px;display:flex;flex-direction:column;justify-content:center}.box.svelte-1ky3pnk .login-form.svelte-1ky3pnk{width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;justify-content:space-between;text-align:center}hr.svelte-1ky3pnk.svelte-1ky3pnk{width:110%;margin-left:-5% ;background-color:var(--main-background-color);height:2.5px;border:none}.login-btn.svelte-1ky3pnk.svelte-1ky3pnk{margin:0 20% 0 20%}.iserv-logo.svelte-1ky3pnk.svelte-1ky3pnk{margin:0 10% 0 10%}@media(max-width: 1024px){}",
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  $$result.css.add(css);
  return `<div class="box svelte-1ky3pnk" data-svelte-h="svelte-gb7cw0"><form class="login-form svelte-1ky3pnk" method="POST" action="/login"><h1>Registierung</h1> <input class="input-style1 svelte-1ky3pnk" type="text" name="name" placeholder="Maximilian Mustermann"> <input class="input-style1 svelte-1ky3pnk" type="email" name="email" placeholder="max.mustermann@tls-giessen.eu"> <button class="login-btn btn-style1 svelte-1ky3pnk">Fortfahren</button> <hr class="svelte-1ky3pnk"> <img class="iserv-logo svelte-1ky3pnk" src="/img/ISERV.svg" alt="IServ-Logo"> <a class="btn-style1 svelte-1ky3pnk" href="/iservlogin">Daten über IServ importieren</a></form> </div>`;
});
export {
  Page as default
};
