<style lang="scss">
    @import 'style.scss';
</style>

<svelte:head>
	<title>Blutspende | Fragebogen</title>
</svelte:head>

<form>
    <div class="card">
        <b>Sind Sie im Alter zwischen 18 und 60 Jahre?</b>
        <div class="answer">
            <button class="btn-ja" on:click={() => nextQuestion('1')}>JA</button> <br>
            <button class="btn-nein" on:click={() => nextQuestion('0')}>NEIN</button>
        </div>
    </div>

    <div class="card">
        <b>Wiegen Sie über 50kg?</b>
        <div class="answer">
            <button class="btn-ja" on:click={() => nextQuestion('1')}>JA</button> <br>
            <button class="btn-nein" on:click={() => nextQuestion('0')}>NEIN</button>
        </div>
    </div>

    <div class="card">
        <b>Fühlen Sie sich gesund?</b>
        <div class="answer">
            <button class="btn-ja" on:click={() => nextQuestion('1')}>JA</button> <br>
            <button class="btn-nein" on:click={() => nextQuestion('0')}>NEIN</button>
        </div>
    </div>

    <div class="card">
        <b>Wurde Ihnen in den letzten vier Monaten Tattoos, Piercings oder Ohrringe gestochen?</b>
        <div class="answer">
            <button class="btn-ja" on:click={() => nextQuestion('1')}>JA</button> <br>
            <button class="btn-nein" on:click={() => nextQuestion('0')}>NEIN</button>
        </div>
    </div>

    <div class="card">
        <b>{@html solution}</b>
        <button class="btn-ja" id="terminBuchen" on:click={() => nextPage()}>Jetzt Termin Buchen</button> <br>
    </div>
</form>

<!-- #TODO if ist bereits Svelte, python verknüpfung fehlt
    {#if current_user.admin}
        <a class="admin" href="/admin">admin</a>
{/if}-->

<script>
    import { onMount } from "svelte";

    let questions = [];
    let solution = "";
    let index = 0;

    onMount( () => {
        questions = document.querySelectorAll('.card');

        questions[index].style.display = 'block';
    });

    function nextQuestion(answer) {
        solution += answer;

        questions[index].style.display = 'none';

        if (solution.length == 4) {
            if(solution == "1110") {
                solution = 'Denken Sie an Ihren gültigen Personalausweis oder einen gültigen Reisepass! Vergessen Sie nicht vor und nach der Blutspende außreichend zu trinken!';
                document.getElementById('terminBuchen').style.visibility="visible";
            } else {
                solution = "<h2>Leider sind Sie nicht passend für eine Blutspende, weil Sie nicht die eben abgefragten Voraussetzungen nich erfüllen!</h2> <h3>Wir bedauern dies und hoffen, dass Sie spenden, sobald Sie alle Voraussetzungen erfüllen.</h3> <h3>Mit freundlichen Grüßen <br> Ihr Blutspende Team der Theodor-Litt-Schule Gießen</h3> <p>Email: </p> <a href='mailto://blutspende@tls-giessen.eu'>blutspende@tls-giessen.eu</a> <h4>Falls Sie denken, dass dies ein Fehler ist, dann überprüfen Sie nochmal, ob alle Optionen richtig ausgewählt sind.</h4> <a href='/questions'>Zu den Fragen</a>";
            }
        }

        index++; 

        if (index < questions.length) { 
            questions[index].style.display = 'block'; 
        }
    }

    function nextPage() {

    }

</script>