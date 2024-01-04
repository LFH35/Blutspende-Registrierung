import adapter from '@sveltejs/adapter-cloudflare';
import preprocess from 'svelte-preprocess';

export default {
	kit: {
		adapter: adapter({
			// See below for an explanation of these options
			routes: {
				include: ['/*'],
				exclude: ['<all>']
			}
		})
	},
	preprocess: preprocess({
		scss: {
			prependData: `@import './src/routes/global.scss';`
		}
	})
};