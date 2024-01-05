<style lang="scss">
    @import 'style.scss';
</style>

<div class="content">
    <h2>Buchung Bestätigen</h2>
    <p>Sind sie sicher das sie den Termin um <b>{time}Uhr</b> buchen möchten? <br> <br> Aktuell sind noch <b>{freeSlots} Plätze</b> frei.</p>
    <button class="buchungBestaetigen" on:click={() => terminBuchen()}>Termin Buchen</button>
    <img src="../../favicon.png" alt="Bluttropfen mit Checkliste">
</div>

<script>
    import { onMount } from "svelte";
    import { goto } from '$app/navigation';

        let thisPage = [];
        let id;
        let appointment= [];
        let time;
        let freeSlots;

    onMount( () => {
        thisPage = window.location.pathname.split('/');
        id = thisPage[0];
        appointment = thisPage[3].split('+');
        time = appointment[0];
        freeSlots = appointment[1];
    });

    function terminBuchen() {
        console.log(time);
        console.log(freeSlots);

        //#TODO termin mit id und time buchen
    }
</script>