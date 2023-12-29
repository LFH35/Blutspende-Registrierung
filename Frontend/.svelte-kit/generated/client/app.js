export { matchers } from './matchers.js';

export const nodes = [
	() => import('./nodes/0.js'),
	() => import('./nodes/1.js'),
	() => import('./nodes/2.js'),
	() => import('./nodes/3.js'),
	() => import('./nodes/4.js')
];

export const server_loads = [];

export const dictionary = {
		"/": [2],
		"/appointments": [3],
		"/question": [4]
	};

export const hooks = {
	handleError: (({ error }) => { console.error(error) }),
};

export { default as root } from '../root.svelte';