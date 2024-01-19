<script>
    import { onMount } from "svelte";
    import { goto } from '$app/navigation';

    onMount( () => {
        let id = window.location.pathname.split('/')[1];
        goto('/' + id + '/questions')
    });
</script>