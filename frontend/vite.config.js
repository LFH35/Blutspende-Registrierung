import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import fs from 'fs';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
				port:5173,
        // https: {
        //     key: fs.readFileSync(`${__dirname}/cert/key.pem`),
        //     cert: fs.readFileSync(`${__dirname}/cert/cert.pem`)
        // },
				hmr: {
					overlay: false,
				}
    },
	preview: {
		host:"0.0.0.0",
		port:5173,
        // https: {
        //     key: fs.readFileSync(`${__dirname}/cert/key.pem`),
        //     cert: fs.readFileSync(`${__dirname}/cert/cert.pem`)
        // },
				hmr: {
					overlay: false,
				}
	}
});
