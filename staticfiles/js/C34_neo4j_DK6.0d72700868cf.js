import * as c34Module from "./C34_neo4j_DK6_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";



document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C34 is ready!");


    const ws = progressBarModule.setupWebSocketProgressBar(c34Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c34Module.nextButtonFormSubmit, c34Module.formC34);


});
