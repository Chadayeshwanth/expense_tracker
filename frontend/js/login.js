async function loginUser() {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${API_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem("user_id", data.user_id);
            localStorage.setItem("username", data.username);
            window.location.href = "dashboard.html";
        } else {
            alert(data.message || "Unable to sign in.");
        }
    } catch (error) {
        alert("Could not connect to the server. Make sure the backend is running on port 5000.");
    }
}