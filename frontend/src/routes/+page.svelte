<style lang="scss">
    @import 'style.scss';
</style>

<svelte:head>
	<title>Blutspende | Login</title>
</svelte:head>

<script>
    process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = "0"; // TODO DELETE THIS LINE IF YOU GO IN PRODUCTION USE!!!

    async function login(event) {
        event.preventDefault(); // prevent the default behave of the form

        const nameInput = event.target.querySelector("#input-name");
        const mailInput = event.target.querySelector("#input-mail");

        const name = nameInput.value;
        const mail = mailInput.value;

        let data = {
            name: name,
            email: mail
        };

        // TODO finish the Login here

        await fetch("https://localhost:5000/login", {
            method: "POST",
            mode: "no-cors",
            cache: "no-cache",
            credentials: "same-origin",
            headers: new Headers({
                "content-type": "application/json",
            }),
            body: JSON.stringify(data),
        })
        // No Navigator needed, because the API redirects you to the questions page
    }
</script>

<div class="box">
    <form class="login-form" on:submit|preventDefault="{login}" method="POST" action="https://127.0.0.1:5000/login">
        <h1>Registierung</h1>

        <input class="input-style1" id="input-name" type="text" name="name" placeholder="Maximilian Mustermann" required>

        <input class="input-style1" id="input-mail" type="email" name="email" placeholder="max.mustermann@tls-giessen.eu" required>

        <button class="login-btn btn-style1" type="submit">Fortfahren</button>

        <hr>

        <img class="iserv-logo" src="img/ISERV.svg" alt="IServ-Logo">

        <a class="btn-style1" href="https://127.0.0.1:5000/iservlogin">Daten über IServ importieren</a>
    </form>
</div>
