function addTask() {
    var newTask = document.getElementById("newTask").value;
    if (newTask.trim() === "") {
        alert("Please enter a task!");
        return;
    }

    var taskList = document.getElementById("taskList");
    var li = document.createElement("li");
    li.innerHTML = `
        <span>${newTask}</span>
        <button onclick="completeTask(this)">Complete</button>
        <button onclick="deleteTask(this)">Delete</button>
    `;
    taskList.appendChild(li);
    document.getElementById("newTask").value = "";
}

function completeTask(button) {
    var li = button.parentElement;
    li.classList.toggle("completed");
}

function deleteTask(button) {
    var li = button.parentElement;
    li.remove();
}
