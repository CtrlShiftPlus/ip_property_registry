async function connectWallet() {
    try {
        // Check if Freighter is installed
        if (!window.freighterApi) {
            alert("Install Freighter Wallet");
            return null;
        }

        // Request permission
        const access = await window.freighterApi.requestAccess();

        if (access.error) {
            alert("Access denied");
            return null;
        }

        // Get public key
        const address = await window.freighterApi.getPublicKey();

        // IMPORTANT: set value (not innerText)
        document.getElementById("wallet").value = address;

        return address;

    } catch (err) {
        console.error(err);
        alert("Error connecting wallet");
        return null;
    }
}


async function registerIP() {
    const title = document.getElementById("title").value;
    const desc = document.getElementById("desc").value;

    let address = document.getElementById("wallet").value;

    // If wallet not connected, connect now
    if (!address) {
        address = await connectWallet();
        if (!address) return;
    }

    // Submit form to Flask
    document.querySelector("form").submit();
}