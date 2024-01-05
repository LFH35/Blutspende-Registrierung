<style lang="scss">
    @import 'layout.scss';
</style>

<svelte:head>
	<title>Blutspende</title>
</svelte:head>

<body>
    <img src="../../img/Blood-LeftBottom.svg" alt="Bloot Left Bottom" class="Blood-LeftBottom">
    <main>
        <slot />
    </main>
    <img src="../../img/Blood-RightTop.svg" alt="Blood Right Top" class="Blood-RightTop">
</body>