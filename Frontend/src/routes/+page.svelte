<div class="box">
    <form class="login-form" method="POST" action="/login">
        <h1>Registierung</h1>

        <input class="input-style1" type="text" name="name" placeholder="Maximilian Mustermann">

        <input class="input-style1" type="email" name="email" placeholder="max.mustermann@tls-giessen.eu">

        <button class="login-btn btn-style1">Fortfahren</button>

        <hr>

        <img class="iserv-logo" src="../../../static/img/ISERV.svg" alt="IServ-Logo">

        <a class="btn-style1" href="/iservlogin">Daten über IServ importieren</a>
    </form>
</div>

<style>
.input-style1 {
    width: 100%;
    color: var(--main-bloody-red-color);
    font-size: large;
    font-weight: 500;
    border: none;
    border-bottom: 3px solid var(--main-bloody-red-color);
}

.input-style1:focus {
    outline: none;
}

.btn-style1 {
    border: none;
    text-align: center;
    color: white;
    background-color: var(--main-bloody-red-color);
    border: 4px solid var(--main-bloody-red-color);
    padding: 20px;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
    font-size: large;
    transition: background-color 0.5s ease;
    cursor: pointer;
}

.btn-style1:hover {
    background-color: var(--main-white-color);
    color: var(--main-bloody-red-color);
}

.box {
    width: 80%;
    height: 100%;
    padding: 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.box .login-form {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    justify-content: space-between;
    text-align: center;
}

hr {
    width: 110%;
    margin-left: -5% ;
    background-color: var(--main-background-color);
    height: 2.5px;
    border: none;
}

.login-btn {
    margin: 0 20% 0 20%;
}

.iserv-logo {
    margin: 0 10% 0 10%;
}

@media (max-width: 1024px) {
    
}
</style>