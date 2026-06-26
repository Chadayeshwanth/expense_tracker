async function registerUser() {
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${API_URL}/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, email, password })
        });

        const data = await response.json();
        alert(data.message || "Registration complete.");

        if (response.ok) {
            window.location.href = "login.html";
        }
    } catch (error) {
        alert("Could not connect to the server. Make sure the backend is running on port 5000.");
    }
}