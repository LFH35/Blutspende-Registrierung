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

<script>
    // TODO Hardcoded durch irgendeinen python datenbank shit ersetzen, bitte formatierung einhalten!

    let defaultSlots = 4;
    let slot1 = ['10:00', defaultSlots];
    let slot2 = ['10:15', 2];
    let slot3 = ['10:30', defaultSlots];
    let slot4 = ['10:45', defaultSlots];
    let slot5 = ['11:00', 0];
    let slot6 = ['11:15', defaultSlots];
    let slot7 = ['11:30', 3];
    let slot8 = ['11:45', defaultSlots];
    let slot9 = ['12:00', defaultSlots];
    let slot10 = ['12:15', defaultSlots];
    let slot11 = ['12:30', defaultSlots];
    let slot12 = ['12:45', 1];
    let slot13 = ['13:00', defaultSlots];
    let slot14 = ['13:15', 1];
    let slot15 = ['13:30', defaultSlots];
    let slot16 = ['13:45', 2];
    let slot17 = ['14:00', defaultSlots];
    let slot18 = ['14:15', defaultSlots];
    let slot19 = ['14:30', defaultSlots];
    let slot20 = ['14:45', defaultSlots];
    let slot21 = ['15:00', 0];

    let slots = [slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14,
        slot15, slot16, slot17, slot18, slot19, slot20, slot21];

    function showSlot(slot) {
        // TODO slot darstellen
    }
</script>
