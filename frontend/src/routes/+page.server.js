import { goto } from '$app/navigation';

export const actions = {
	default: async ({ request }) => {
		console.log('in');
		const formData = await request.formData();
		const name = formData.get('input-name');
		const mail = formData.get('input-mail');

		let data = {
			name: name,
			email: mail
		};

		// TODO finish the Login here
		try {
			await fetch('https://localhost:5000/login', {
				method: 'GET',
				cache: 'no-cache',
				credentials: 'same-origin',
				headers: new Headers({
					'content-type': 'application/json'
				}),
				data: JSON.stringify(data)
			});
		} catch (error) {
			console.error('Fetch error:', error);
		}
		goto('/id/questions');
	}
};
