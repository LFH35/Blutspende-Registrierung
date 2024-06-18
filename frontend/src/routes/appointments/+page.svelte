<style lang="scss">
    @import 'style';
</style>

<svelte:head>
	<title>Blutspende | Termine</title>
</svelte:head>


<script>
    import { goto } from '$app/navigation';
    import { onMount } from "svelte";

    let slots = [];
    onMount(async () => {
        try {
            // process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
            const response = await fetch("https://localhost:5000/appointments", {
                method: "GET",
                cache: "no-cache",
                credentials: "same-origin",
                headers: new Headers({
                    "content-type": "application/json"
                })
            });

            slots = await response.json();
            console.log()
        } catch (error) {
            console.error("Fetch error:", error);
        }
    });

    function showSlot(slot) {
        let thisPage = window.location.pathname;
        goto(thisPage + '/' + slot[0] + '+' + slot[1] + '+' + slots[0]);
    }
</script>



<h2>Bitte wählen Sie einen Termin</h2>
<h3 class='date'>Datum: {slots[0]}</h3>
<div class="appointments">
    {#each slots.slice(1, -1) as slot}
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
