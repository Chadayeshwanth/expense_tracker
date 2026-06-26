const userId = localStorage.getItem("user_id");

if (!userId) {
    window.location.href = "login.html";
}

function resetForm() {
    document.getElementById("title").value = "";
    document.getElementById("amount").value = "";
    document.getElementById("category").value = "";
    document.getElementById("expense_date").value = "";
    document.getElementById("description").value = "";
}

async function addExpense() {
    const title = document.getElementById("title").value.trim();
    const amount = document.getElementById("amount").value;
    const category = document.getElementById("category").value.trim();
    const expense_date = document.getElementById("expense_date").value;
    const description = document.getElementById("description").value.trim();

    if (!title || !amount || !category || !expense_date) {
        alert("Please complete the required fields before saving your expense.");
        return;
    }

    try {
        const response = await fetch(`${API_URL}/expenses`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                user_id: userId,
                title,
                amount,
                category,
                expense_date,
                description
            })
        });

        const data = await response.json();
        alert(data.message || "Expense saved.");

        if (response.ok) {
            resetForm();
            loadExpenses();
        }
    } catch (error) {
        alert("Could not save the expense right now.");
    }
}

async function loadExpenses() {
    try {
        const response = await fetch(`${API_URL}/expenses/${userId}`);
        const expenses = await response.json();

        const summary = document.getElementById("summary");
        const total = expenses.reduce((acc, expense) => acc + Number(expense.amount || 0), 0);
        summary.textContent = `Total ${expenses.length} expense${expenses.length === 1 ? "" : "s"} • ₹${total.toFixed(2)}`;

        if (!expenses.length) {
            document.getElementById("expenseTable").innerHTML = '<tr><td colspan="5" class="empty-state">No expenses yet. Add your first one above.</td></tr>';
            return;
        }

        document.getElementById("expenseTable").innerHTML = expenses.map(expense => `
            <tr>
                <td>${expense.title}</td>
                <td>₹${Number(expense.amount).toFixed(2)}</td>
                <td>${expense.category}</td>
                <td>${expense.expense_date}</td>
                <td><button class="delete-btn" onclick="deleteExpense(${expense.id})">Delete</button></td>
            </tr>
        `).join("");
    } catch (error) {
        document.getElementById("expenseTable").innerHTML = '<tr><td colspan="5" class="empty-state">Unable to load expenses from the server.</td></tr>';
    }
}

async function deleteExpense(id) {
    try {
        await fetch(`${API_URL}/expenses/${id}`, { method: "DELETE" });
        loadExpenses();
    } catch (error) {
        alert("Unable to delete this expense right now.");
    }
}

function logout() {
    localStorage.clear();
    window.location.href = "login.html";
}