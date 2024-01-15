<style lang="scss">
    @import 'style.scss';
</style>

<svelte:head>
	<title>Blutspende | Fragebogen</title>
</svelte:head>


    <div class="card">
        <h2>Sind Sie im Alter zwischen 18 und 60 Jahre?</h2>
        <div class="btns">
            <button class="btn-ja" on:click={() => nextQuestion('1')}>JA</button>
            <button class="btn-nein" on:click={() => nextQuestion('0')}>NEIN</button>
        </div>
        <img src="../favicon.png" alt="Bluttropfen mit Checkliste">
    </div>

    <div class="card">
        <h2>Wiegen Sie über 50kg?</h2>
         <div class="btns">
            <button class="btn-ja" on:click={() => nextQuestion('1')}>JA</button>
            <button class="btn-nein" on:click={() => nextQuestion('0')}>NEIN</button>
        </div>
        <img src="../favicon.png" alt="Bluttropfen mit Checkliste">
    </div>

    <div class="card">
        <h2>Fühlen Sie sich gesund?</h2>
        <div class="btns">
            <button class="btn-ja" on:click={() => nextQuestion('1')}>JA</button>
            <button class="btn-nein" on:click={() => nextQuestion('0')}>NEIN</button>
        </div>
        <img src="../favicon.png" alt="Bluttropfen mit Checkliste">
    </div>

    <div class="card">
        <h2>Wurde Ihnen in den letzten vier Monaten Tattoos, Piercings oder Ohrringe gestochen?</h2>
        <div class="btns">
            <button class="btn-ja" on:click={() => nextQuestion('1')}>JA</button>
            <button class="btn-nein" on:click={() => nextQuestion('0')}>NEIN</button>
        </div>
        <img src="../favicon.png" alt="Bluttropfen mit Checkliste">
    </div>

    <div class="card">
        {@html solution}
        <div id="donatable">
            <button class="btn-donatable" on:click={() => nextPage()}>Jetzt Termin Buchen</button>
            <img src="../favicon.png" alt="Bluttropfen mit Checkliste">
        </div>
    </div>

<script>
    import { onMount } from "svelte";
    import { goto } from '$app/navigation';


    let questions = [];
    let solution = "";
    let index = 0;

    onMount( () => {
        questions = document.querySelectorAll('.card');

        questions[index].style.display = 'flex';
    });

    function nextQuestion(answer) {
        solution += answer;
 
        questions[index].style.display = 'none';

        if (solution.length === 4) {
            if (solution === "1110") {
                solution = "<h2>Denken Sie an Ihren gültigen Personalausweis oder Reisepass! Vergessen " +
                  "Sie nicht vor und nach der Blutspende außreichend zu trinken!</h2>" +
                  "<h4>Bitte vermerken Sie, dass Sie vor Ort noch einmal genauer auf verschiedene Aspekte untersucht " +
                  "werden und dieses Ergebniss keine Garantie ist, dass Sie Blutspenden dürfen.</h4>";
                document.getElementById("donatable").style.visibility = "visible";
            } else {
                solution = "<div class='notDonatable'>" +
                  "<h2>Leider sind Sie nicht passend für eine Blutspende, weil Sie nicht die eben abgefragten Voraussetzungen erfüllen!</h2>" +
                  "<h3>Wir bedauern dies und hoffen, dass Sie spenden, sobald Sie alle Voraussetzungen erfüllen.</h3>" +
                  "<h3>Mit freundlichen Grüßen <br> Ihr Blutspende Team der Theodor-Litt-Schule Gießen</h3>" +
                  "<p>Email: </p> <a href='mailto://blutspende@tls-giessen.eu'>blutspende@tls-giessen.eu</a>" +
                  "<h4>Falls Sie denken, dass dies ein Fehler ist, dann überprüfen Sie nochmal, ob alle Optionen richtig ausgewählt sind.</h4>" +
                  "<button on:click='{() => reloadPage()}' class='btn-donatable'>Zu den Fragen</button></div>";
            }
        }

        index++;

        if (index < questions.length) { 
            questions[index].style.display = 'flex'; 
        }
    }

    function nextPage() {
        let thisPage = window.location.pathname.split('/');
        const id = thisPage[1];
        goto('/' + id + '/appointments');
    }



    function reloadPage() {
        const thisPage = window.location.pathname;
        goto(thisPage);
    }

</script>