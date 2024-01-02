<style lang="scss">
    @import 'style.scss';
</style>

<svelte:head>
	<title>Blutspende | Login</title>
</svelte:head>

<div class="box">
    <form class="login-form" method="POST" action="https://127.0.0.1:5000/login">
        <h1>Registierung</h1>

        <input class="input-style1" type="text" name="name" placeholder="Maximilian Mustermann">

        <input class="input-style1" type="email" name="email" placeholder="max.mustermann@tls-giessen.eu">

        <button class="login-btn btn-style1">Fortfahren</button>

        <hr>

        <img class="iserv-logo" src="img/ISERV.svg" alt="IServ-Logo">

        <a class="btn-style1" href="https://127.0.0.1:5000/iservlogin">Daten über IServ importieren</a>
    </form>
</div>