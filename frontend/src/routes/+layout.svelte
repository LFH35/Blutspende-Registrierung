<style lang="scss">
    @import 'layout.scss';
</style>

<svelte:head>
	<title>Blutspende</title>
    <!--TODO<link rel="shortcut icon" href="favicon.png" type="image/x-icon">-->
</svelte:head>

<body>
    <img src="../favicon.png" alt="Bluttropfen mit Checkliste in der Hand." class="favicon">
    <img src="../img/Blood-LeftBottom.svg" alt="Bloot Left Bottom" class="Blood-LeftBottom">
    <main>
        <slot />
    </main>
    <img src="../img/Blood-RightTop.svg" alt="Blood Right Top" class="Blood-RightTop">
</body>