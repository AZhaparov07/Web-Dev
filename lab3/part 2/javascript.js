const addBtn = document.getElementById('addBtn');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');

addBtn.addEventListener('click', () => {
    const taskText = taskInput.value.trim();
    if (taskText === '') return;

    const li = document.createElement('li');
    li.innerHTML = `
      <input type="checkbox" onchange="toggleComplete(this)">
      <span>${taskText}</span>
      <span class="delete-btn" onclick="deleteTask(this)">&#128465;</span>
    `;
    taskList.appendChild(li);
    taskInput.value = '';
  });


function toggleComplete(checkbox){
    const li = checkbox.parentElement;
    li.classList.toggle('completed');
}
function deleteTask(deleteBtn){
    const li = deleteBtn.parentElement;
    li.remove();
}