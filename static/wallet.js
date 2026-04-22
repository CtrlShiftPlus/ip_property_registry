async function connectWallet() {
    if (!window.freighter) {
        alert("Install Freighter Wallet");
        return;
    }

    const isAllowed = await window.freighter.isAllowed();
    if (!isAllowed) {
        await window.freighter.setAllowed();
    }

    const address = await window.freighter.getPublicKey();

    document.getElementById("wallet").innerText = address;

    return address;
}

async function registerIP() {
    const title = document.getElementById("title").value;
    const desc = document.getElementById("desc").value;

    const address = await connectWallet();

    alert("Simulated: IP registered by " + address);

    // Real transaction integration can be added later
}