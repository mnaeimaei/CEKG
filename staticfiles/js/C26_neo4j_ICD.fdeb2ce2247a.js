import * as c26Module from "./C26_neo4j_ICD_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";


document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C26 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c26Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c26Module.nextButtonFormSubmit, c26Module.formC26);


});
