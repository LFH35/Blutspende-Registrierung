<style lang="scss">
    @import 'style.scss';
</style>

<svelte:head>
	<title>Blutspende | UNDEFINED</title> <!--TODO Titel?-->
</svelte:head>


<h2>Bitte wählen sie einen Termin</h2>
<div class="appointments">
    {#each appointments as appointment}
        <button class="freiePlaetze{appointment[1]} appointment" on:click={() => showSlot(appointment)}>{appointment[0]}</button>
    {/each}
</div>

<script>
    //TODO Hardcoded durch irgendeinen python datenbank shit ersetzen, bitte formatierung einhalten!

    let standartPlätze = 4;
    let termin1 = ['10:00', standartPlätze];
    let termin2 = ['10:15', 2];
    let termin3 = ['10:30', standartPlätze];
    let termin4 = ['10:45', standartPlätze];
    let termin5 = ['11:00', 0];
    let termin6 = ['11:15', standartPlätze];
    let termin7 = ['11:30', 3];
    let termin8 = ['11:45', standartPlätze];
    let termin9 = ['12:00', standartPlätze];
    let termin10 = ['12:15', standartPlätze];
    let termin11 = ['12:30', standartPlätze];
    let termin12 = ['12:45', 1];
    let termin13 = ['13:00', standartPlätze];
    let termin14 = ['13:15', 1];
    let termin15 = ['13:30', standartPlätze];
    let termin16 = ['13:45', 2];
    let termin17 = ['14:00', standartPlätze];
    let termin18 = ['14:15', standartPlätze];
    let termin19 = ['14:30', standartPlätze];
    let termin20 = ['14:45', standartPlätze];
    let termin21 = ['15:00', 0];

    let appointments = [termin1, termin2, termin3, termin4, termin5, termin6, termin7, termin8, termin9, termin10, termin11, termin12, termin13, termin14, termin15, termin16, termin17, termin18, termin19, termin20, termin21];

    function showSlot(slot) {
        //TODO slot darstellen
    }
</script>