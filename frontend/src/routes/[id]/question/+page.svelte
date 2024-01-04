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
    <p id="hinweisText"></p>
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

        index++; 

        if (index < questions.length) { 
            questions[index].style.display = 'block'; 
        } else {
            // document.getElementById('hinweisText').innerHTML = 'Vielen Dank für Ihre Teilnahme!';
        }
    }

</script>