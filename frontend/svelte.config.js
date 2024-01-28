import preprocess from 'svelte-preprocess';

export default {
	preprocess: preprocess({
		scss: {
			prependData: `@import './src/routes/global.scss';`
		}
	})
};