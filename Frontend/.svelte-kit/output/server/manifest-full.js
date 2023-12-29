export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["favicon.png","img/Blood-LeftBottom.svg","img/Blood-RightTop.svg","img/ISERV.svg"]),
	mimeTypes: {".png":"image/png",".svg":"image/svg+xml"},
	_: {
		client: {"start":"_app/immutable/entry/start.7hK6xNEA.js","app":"_app/immutable/entry/app.zDnLSTxg.js","imports":["_app/immutable/entry/start.7hK6xNEA.js","_app/immutable/chunks/scheduler.Smq_RA6i.js","_app/immutable/chunks/singletons.R8eMLXe1.js","_app/immutable/entry/app.zDnLSTxg.js","_app/immutable/chunks/scheduler.Smq_RA6i.js","_app/immutable/chunks/index.BamsqFJs.js"],"stylesheets":[],"fonts":[],"uses_env_dynamic_public":false},
		nodes: [
			__memo(() => import('./nodes/0.js')),
			__memo(() => import('./nodes/1.js')),
			__memo(() => import('./nodes/2.js')),
			__memo(() => import('./nodes/3.js')),
			__memo(() => import('./nodes/4.js'))
		],
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			},
			{
				id: "/appointments",
				pattern: /^\/appointments\/?$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 3 },
				endpoint: null
			},
			{
				id: "/question",
				pattern: /^\/question\/?$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 4 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		}
	}
}
})();
