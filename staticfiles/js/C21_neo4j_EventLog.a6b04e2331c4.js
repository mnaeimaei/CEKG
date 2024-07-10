import * as c21Module from "./C21_neo4j_EventLog_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";

document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C21 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c21Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c21Module.nextButtonFormSubmit, c21Module.formC21);


});
