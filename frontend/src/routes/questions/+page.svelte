<style lang="scss">
    @import 'style';
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
        <div id="accepted">
            <h2>Denken Sie an Ihren gültigen Personalausweis oder Reisepass! Vergessen Sie nicht vor und nach der Blutspende außreichend zu trinken!</h2>
            <h4>Bitte vermerken Sie, dass Sie vor Ort noch einmal genauer auf verschiedene Aspekte untersucht werden und dieses Ergebniss keine Garantie ist, dass Sie Blutspenden dürfen.</h4>
            <div id="donatable">
                <button class="btn-donatable" on:click={() => nextPage()}>Jetzt Termin Buchen</button>
                <img src="../favicon.png" alt="Bluttropfen mit Checkliste">
            </div>
        </div>
        <div id="not-accepted">
            <h2>Leider sind Sie nicht passend für eine Blutspende, da Sie die Voraussetzungen nicht erfüllen!</h2>
            <h3>Wir bedauern dies und hoffen, dass Sie spenden, sobald Sie alle Voraussetzungen erfüllen.
            <br>Mit freundlichen Grüßen <br> Ihr Blutspende Team der TLS Gießen</h3>
            <h5>Falls Sie denken, dass dies ein Fehler ist, dann überprüfen Sie nochmal, ob alle Optionen richtig ausgewählt sind.</h5>
            <button on:click='{() => reloadPage()}' class="btn-nein">Zu den Fragen</button>
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
                document.getElementById("accepted").style.display = 'flex';
            } else {
                document.getElementById("not-accepted").style.display = 'flex';
            }
        }

        index++;

        if (index < questions.length) {
            questions[index].style.display = 'flex';
        }
    }

    function nextPage() {
        goto('/appointments');
    }

    function reloadPage() {
        goto('/question');
    }

</script>