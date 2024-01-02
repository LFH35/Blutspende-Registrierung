<style lang="scss">
    @import 'style.scss';
</style>

<svelte:head>
	<title>Blutspende | UNDEFINED</title> <!--#TODO -->
</svelte:head>

<form method="POST" action="/checkdonator">
    <div class="card">
        <b>Sind Sie im Alter zwischen 18 und 60 Jahre?</b>
        <div class="answer">
            <label class="custom-checkbox">
                <input type="checkbox" id="option1" name="adult" onchange="toggleCheck(this); checkButtons()" class="checkbox-ja">
                <span class="checkbox">JA</span>
            </label>
        
            <label class="custom-checkbox">
                <input type="checkbox" id="option2" name="group2" onchange="toggleCheck(this); checkButtons()" class="checkbox-nein">
                <span class="checkbox">NEIN</span>
            </label>
        </div>
    </div>

    <div class="card">
        <b>Wiegen Sie über 50kg?</b>
        <div class="answer">
            <label class="custom-checkbox">
                <input type="checkbox" id="option1" name="weight" onchange="toggleCheck(this); checkButtons()" class="checkbox-ja">
                <span class="checkbox">JA</span>
            </label>
        
            <label class="custom-checkbox">
                <input type="checkbox" id="option2" name="group3" onchange="toggleCheck(this); checkButtons()" class="checkbox-nein">
                <span class="checkbox">NEIN</span>
            </label>
        </div>
    </div>

    <div class="card">
        <b>Fühlen Sie sich gesund?</b>
        <div class="answer">
            <label class="custom-checkbox">
                <input type="checkbox" id="option1" name="healthy" onchange="toggleCheck(this); checkButtons()" class="checkbox-ja">
                <span class="checkbox">JA</span>
            </label>
        
            <label class="custom-checkbox">
                <input type="checkbox" id="option2" name="group4" onchange="toggleCheck(this); checkButtons()" class="checkbox-nein">
                <span class="checkbox">NEIN</span>
            </label>
        </div>
    </div>

    <div class="card">
        <b>Wurde Ihnen in den letzten vier Monaten Tattoos, Piercings oder Ohrringe gestochen?</b>
        <div class="answer">
            <label class="custom-checkbox">
                <input type="checkbox" id="option1" name="tattoos" onchange="toggleCheck(this); checkButtons()" class="checkbox-ja">
                <span class="checkbox">JA</span>
            </label>
        
            <label class="custom-checkbox">
                <input type="checkbox" id="option2" name="group5" onchange="toggleCheck(this); checkButtons()" class="checkbox-nein">
                <span class="checkbox">NEIN</span>
            </label>
        </div>
    </div>
    <button id="weiterbtn" class="btn-style1 weiterbtn" type="submit">Weiter</button>

    <p>Denken Sie bitte an Ihren gültigen Personalausweis oder einen gültigen Reisepass! <br>
        Vergessen Sie nicht vor und nach der Blutspende außreichend zu trinken!</p>
</form>

<!-- #TODO if ist bereits Svelte, python verknüpfung fehlt
    {#if current_user.admin}
        <a class="admin" href="/admin">admin</a>
{/if}-->

<script>
    // #TODO script not working
    function toggleCheck(checkbox) {
    // Suchen Sie das übergeordnete <div> des geänderten Kontrollkästchens
    let parentDiv = checkbox.closest('.card');

    // Durchlaufen Sie die Checkboxen innerhalb des übergeordneten <div>
    let checkboxes = parentDiv.querySelectorAll('input[type="checkbox"]');
    for (const element of checkboxes) {
        if (element !== checkbox) {
            element.checked = false; // Anderes Kontrollkästchen abwählen
        }
    }
}

function checkButtons() {
    let cards = document.querySelectorAll('.card');
    let button = document.getElementById('weiterbtn');
    let allCardsHaveCheckboxChecked = true;

    // Überprüfen, ob in jedem .card-Div mindestens eine Checkbox ausgewählt ist
    for (const element of cards) {
        let checkboxes = element.querySelectorAll('input[type="checkbox"]');
        let atLeastOneChecked = false;

        // Überprüfen, ob mindestens eine Checkbox in diesem .card-Div ausgewählt ist
        for (let j of checkboxes.length) {
            if (checkboxes[j].checked) {
                atLeastOneChecked = true;
                break; // Wenn mindestens eine Checkbox ausgewählt ist, abbrechen
            }
        }

        if (!atLeastOneChecked) {
            allCardsHaveCheckboxChecked = false;
            break; // Wenn mindestens ein .card-Div keine ausgewählte Checkbox hat, abbrechen
        }
    }

    // Button aktivieren oder deaktivieren und Design ändern
    button.disabled = !allCardsHaveCheckboxChecked;
}
</script>