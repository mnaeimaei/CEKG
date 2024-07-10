import * as c35Module from "./C35_neo4j_DK7_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";



document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C35 is ready!");




    const ws = progressBarModule.setupWebSocketProgressBar(c35Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c35Module.nextButtonFormSubmit, c35Module.formC35);


});
