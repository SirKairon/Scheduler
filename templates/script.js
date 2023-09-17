// import * as fs from 'fs';

var dict = {"userName": "Guest", "primaryTasks": {}, "secondaryTasks": {}};
var checkFile = document.querySelectorAll('input[name="check"]');
const submit_btn = document.querySelector('#p-next');

const hide = function(event){
    event.style.display = "none";
}

const show = function(event){
    event.style.display = "block";
}

document.getElementById("nameForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get the user's input from the form
    if (document.getElementById("name").value != ""){
        dict["userName"] = document.getElementById("name").value;
    }       
    // Display the extracted name
    hide(document.getElementById('form'));
    document.getElementById("hello").innerHTML = "Hello " + dict["userName"] + "!"
    show(document.getElementById('hello'));

    setTimeout(function(){
        hide(document.getElementById("hello"))}, 3000);

    setTimeout(function(){
        schedule()}, 3000);
});

const schedule = function(){
    show(document.getElementById('schedule'));
}

checkFile.forEach(function(radio) {
    radio.addEventListener('change', function() {
        var selectedFile = document.querySelector('input[name="check"]:checked');
        console.log(selectedFile)
        if (selectedFile.value == "no") {
            document.getElementById("container").style.display = "none";
        } else {
            document.getElementById("container").style.display = "flex";
        }
    });
});

document.getElementById("schedule").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    hide(document.getElementById('schedule'))   
    show(document.getElementById('primaryTask'))
    
    const primary_task_form = document.querySelector("#p-task-form");

    const input_text = document.querySelector("#p-task-input");
    const input_day = document.querySelector("#p-day")
    const input_start_time = document.querySelector("#p-start-time")
    const input_end_time = document.querySelector("#p-end-time")
    const input_task_desc = document.querySelector("#p-task-desc");

    const list_el = document.querySelector("#p-tasks");

    primary_task_form.addEventListener('submit', (e) => {
        e.preventDefault();

        if (!input_text.value){
            alert("Please fill out the text");
            return;
        } else if (input_day.value == "choose_day") {
            alert("Please input the day");
            return;
        } else if (input_start_time.value == "choose_start_time"){
            alert("Please input the start time field");
            return;
        } else if (input_end_time.value == "choose_end_time"){
            alert("Please input the end time field");
            return;
        } else if (input_start_time.value >= input_end_time.value ){
            alert("Please enter a different start and end time");
            return;
        }else if (!input_task_desc.value){
            alert("Please input the task description field or input N/A");
            return;
        } else if (input_text.value in dict['primaryTasks']){
            alert("Please enter another event")
            return;
        } else {
            console.log("Success");
        }

        const task_el = document.createElement("div");
        task_el.classList.add("task");

        const task_content_el = document.createElement("div");
        task_content_el.classList.add("content"); 

        const task_card = document.createElement("div");
        task_card.classList.add("task-card");
        
        task_el.appendChild(task_content_el);
        task_content_el.appendChild(task_card);

        task_card.innerHTML = `
        <input type="text" class="task-card-1 text" value="${input_text.value}" readonly>
        <input type="text" class="task-card-1 day" value="${input_day.value}" readonly>
        <input type="text" class="task-card-1 time" value="${input_start_time.value} - ${input_end_time.value}" readonly>
        <input type="text" class="task-card-1 desc" value="${input_task_desc.value}" readonly>`;

        const task_actions_el = document.createElement("div");
        task_actions_el.classList.add("actions");

        const task_delete_el = document.createElement("button");
        task_delete_el.classList.add('btn');
        task_delete_el.innerHTML = "Delete"

        task_actions_el.appendChild(task_delete_el);
        task_el.appendChild(task_actions_el);
        
        list_el.appendChild(task_el);
        dict['primaryTasks'][input_text.value] = 
            {"day": input_day.value, 
             "start_time": input_start_time.value,
             "end_time": input_end_time.value,
             "task_desc": input_task_desc.value
            }

        task_delete_el.addEventListener('click', () => {
            const htmlString = task_el.innerHTML;
            const tempElement = document.createElement('div');
            tempElement.innerHTML = htmlString;
            const textElement = tempElement.querySelector('.task-card-1.text');
            const extractedText = textElement ? textElement.value : null;

            delete dict['primaryTasks'][extractedText];
            list_el.removeChild(task_el);
        });
    });
});  

submit_btn.addEventListener("submit", function(event){
    event.preventDefault();
    console.log(dict);
    hide(document.getElementById('primaryTask'));   
    show(document.getElementById('secondaryTask'));

    const new_task_form = document.querySelector("#s-task-form");

    const input_text = document.querySelector("#s-task-input");
    const input_day = document.querySelector("#s-day");
    const input_time = document.querySelector("#s-time");
    const input_hours = document.querySelector("#s-hours");
    const input_task_desc = document.querySelector("#s-task-desc");

    const list_el = document.querySelector("#s-tasks");

    new_task_form.addEventListener('submit', (e) => {
        e.preventDefault();

        if (!input_text.value){
            alert("Please fill out the text");
            return;
        } else if (input_day.value == "choose_day") {
            alert("Please input by which day is the task due.");
            return;
        } else if (input_time.value == "choose_time"){
            alert("Please input any specific time for the task to be due.");
            return;
        } else if (input_hours.value == "select_hours"){
            alert("Please input the number of hours");
            return;
        } else if (!input_task_desc.value){
            alert("Please input the task description field or input N/A");
            return;
        } else if (input_text.value in dict['secondaryTasks']){
            alert("Please enter another event")
            return;
        } else {
            console.log("Success");
        }

        const task_el = document.createElement("div");
        task_el.classList.add("task");

        const task_content_el = document.createElement("div");
        task_content_el.classList.add("content"); 

        const task_card = document.createElement("div");
        task_card.classList.add("task-card");
        
        task_el.appendChild(task_content_el);
        task_content_el.appendChild(task_card);

        task_card.innerHTML = `
        <input type="text" class="task-card-1 text" value="${input_text.value}" readonly>
        <input type="text" class="task-card-1 day-time" value="Due by ${input_day.value} day, ${input_time.value}" readonly>
        <input type="text" class="task-card-1 hours" value="Allocated ${input_hours.value} to complete the task" readonly>
        <input type="text" class="task-card-1 desc" value="${input_task_desc.value}" readonly>`;

        const task_actions_el = document.createElement("div");
        task_actions_el.classList.add("actions");

        const task_delete_el = document.createElement("button");
        task_delete_el.classList.add('btn');
        task_delete_el.innerHTML = "Delete"

        task_actions_el.appendChild(task_delete_el);
        task_el.appendChild(task_actions_el);
        
        list_el.appendChild(task_el);
        dict['secondaryTasks'][input_text.value] = 
            {"day": input_day.value, 
             "time": input_time.value,
             "hours": input_hours.value,
             "task_desc": input_task_desc.value
            }

        task_delete_el.addEventListener('click', () => {
            const htmlString = task_el.innerHTML;
            const tempElement = document.createElement('div');
            tempElement.innerHTML = htmlString;
            const textElement = tempElement.querySelector('.task-card-1.text');
            const extractedText = textElement ? textElement.value : null;

            delete dict['secondaryTasks'][extractedText];
            list_el.removeChild(task_el);
        });
    });
})

function generateSchedule() {
    // const jsonString = JSON.stringify(dict, null, 2);

    // // Specify the file path where you want to save the JSON file
    // const filePath = 'data.json';

    // // Write the JSON data to the file
    // fs.writeFile(filePath, jsonString, (err) => {
    //     if (err) {
    //         console.error('Error writing JSON file:', err);
    //     } else {
    //         console.log('JSON file has been saved.');
    //     }
    // });
    console.log(dict);
}
   
// Add a click event listener to the download button
document.querySelector("#s-next").addEventListener("submit", generateSchedule);

