

//export const progressBar = document.getElementById('progressBar');
//export const form2 = document.getElementById('allForm2');


//import * as p2Module from "./A2_Module_downloading";

function setupWebSocketProgressBar(targetProgressBar) {

    const ws = new WebSocket('ws://' + window.location.host + '/ws/progress/');
    ws.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const progress = data.progress;
        console.log("Progress: " + progress);
        targetProgressBar.style.width = progress + '%';
        targetProgressBar.innerText = progress + '% Complete';
    };
    return ws;
}

export { setupWebSocketProgressBar };

//import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";
//const ws = progressBarModule.setupWebSocketProgressBar(p2Module.progressBar);

function handleFormSubmission(ws,nextButtonFormSubmit, formName) {
    nextButtonFormSubmit.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // WebSocket connection must be established and listening before the form is submitted
        if (ws.readyState === WebSocket.OPEN) {
            console.log("WebSocket.OPEN");
            formName.submit(); // Submit the form
        } else {
            console.log("WebSocket.else");
            ws.onopen = function () {
            formName.submit(); // Submit the form
            };
        }
    });
}

export { handleFormSubmission };

//progressBarModule.handleFormSubmission(ws, p2Module.nextButton2FormSubmit, p2Module.form2);