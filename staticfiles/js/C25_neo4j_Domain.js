import * as c25Module from "./C25_neo4j_Domain_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";



document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C25 is ready!");


    const ws = progressBarModule.setupWebSocketProgressBar(c25Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c25Module.nextButtonFormSubmit, c25Module.formC25);


});
