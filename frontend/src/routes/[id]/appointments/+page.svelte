<style lang="scss">
    @import 'style.scss';
</style>

<svelte:head>
	<title>Blutspende | Termine</title>
</svelte:head>


<h2>Bitte wählen sie einen Termin</h2>
<div class="appointments">
    {#each slots as slot}
        {#if slot[1] === 0}
            <button disabled class="freiePlaetze{slot[1]} appointment" on:click={() => showSlot(slot)}>{slot[0]}</button>
        {:else}
            <button class="freiePlaetze{slot[1]} appointment" on:click={() => showSlot(slot)}>{slot[0]}</button>
        {/if}
    {/each}
</div>
<div class="legend">
    <p class="dot dot-grey">Kein freier Platz</p>
    <p class="dot dot-red">1 freier Platz</p>
    <p class="dot dot-orange">2-3 freie Plätze</p>
    <p class="dot dot-green">4 freie Plätze</p>
</div>

<script>
    // TODO Hardcoded durch irgendeinen python datenbank shit ersetzen, bitte formatierung einhalten!
    import { goto } from '$app/navigation';
    import { onMount } from "svelte";

    let slots = [];

    onMount( async () => {
        const res = await fetch("https://localhost:5000/appointments", {
            method: "GET",
            mode: "no-cors",
            cache: "no-cache",
            credentials: "same-origin",
            headers: new Headers({
                "content-type": "application/json",
            }),
        });
        slots = await res.json();
    });

    function showSlot(slot) {
        console.log(slots);
        console.log(slot);
        let thisPage = window.location.pathname;
        goto(thisPage + '/' + slot[0] + '+' + slot[1]);
    }
</script>
