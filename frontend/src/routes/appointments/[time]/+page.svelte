<style lang="scss">
    @import 'style';
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
    let date;

    onMount( () => {
        thisPage = window.location.pathname.split('/');
        id = document.cookie.split("=")[1];
        appointment = thisPage[2].split('+');
        time = appointment[0];
        freeSlots = appointment[1];
        date = appointment[2];
    });

    async function terminBuchen() {
        console.log(time);
        console.log(freeSlots);

        let data = {
            user_id: id,
            time: time,
            date: date
        }

        await fetch("https://localhost:5000/set_appointment", {
            method: "POST",
            mode: "no-cors",
            cache: "no-cache",
            credentials: "same-origin",
            headers: new Headers({
                "content-type": "application/json",
            }),
            body: JSON.stringify(data),
        })

        await goto('/success');
    }
</script>