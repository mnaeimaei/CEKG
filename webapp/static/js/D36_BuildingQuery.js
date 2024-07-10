import * as c20Module from "./D36_BuildingQuery_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";





document.addEventListener('DOMContentLoaded', function () {
    console.log('Page loaded, setting up WebSocket');

    const ws = progressBarModule.setupWebSocketProgressBar(c20Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c20Module.nextButton2FormSubmit, c20Module.formC20);


});
