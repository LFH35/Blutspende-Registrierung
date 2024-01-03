<style lang="scss">
    @import 'style.scss';
</style>

<svelte:head>
	<title>Blutspende | UNDEFINED</title> <!--#TODO Titel hinzufügen-->
</svelte:head>

<form>
    <div class="card">
        <b>Sind Sie im Alter zwischen 18 und 60 Jahre?</b>
        <div class="answer">
            <button class="btn-ja">JA</button> <br>
            <button class="btn-nein">NEIN</button>
        </div>
    </div>

    <div class="card">
        <b>Wiegen Sie über 50kg?</b>
        <div class="answer">
            <button class="btn-ja">JA</button> <br>
            <button class="btn-nein">NEIN</button>
        </div>
    </div>

    <div class="card">
        <b>Fühlen Sie sich gesund?</b>
        <div class="answer">
            <button class="btn-ja">JA</button> <br>
            <button class="btn-nein">NEIN</button>
        </div>
    </div>

    <div class="card">
        <b>Wurde Ihnen in den letzten vier Monaten Tattoos, Piercings oder Ohrringe gestochen?</b>
        <div class="answer">
            <button class="btn-ja">JA</button> <br>
            <button class="btn-nein">NEIN</button>
        </div>
    </div>

    <p id="hinweisText"></p>
</form>

<!-- #TODO if ist bereits Svelte, python verknüpfung fehlt
    {#if current_user.admin}
        <a class="admin" href="/admin">admin</a>
{/if}-->

<script>
    document.addEventListener("DOMContentLoaded", function() {
        var questions = document.querySelectorAll('.card');
        var index = 0;
        var solution = "";

        questions[index].style.display = 'block';
    });

    function nextQuestion(answer) {
        solution += answer; 

        questions[index].style.display = 'none';

        if (index < questions.length - 1) {
            index++; // Gehe zur nächsten Frage
            questions[index].style.display = 'block'; // Zeige die nächste Frage an
        } else {
            document.getElementById('hinweisText').innerHTML = 'Denken Sie bitte an Ihren gültigen Personalausweis oder einen gültigen Reisepass! Vergessen Sie nicht vor und nach der Blutspende außreichend zu trinken!';
        }
    }
</script>