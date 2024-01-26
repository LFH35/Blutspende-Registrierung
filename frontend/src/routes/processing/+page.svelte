<svelte:head>
	<title>processing...</title>
</svelte:head>

<script>
    import { onMount } from "svelte";
    import { goto } from '$app/navigation';

    onMount( () => {
        document.cookie = `user_id=${window.location.search.split('=')[1]}`;
				goto("/questions")
    });

</script>