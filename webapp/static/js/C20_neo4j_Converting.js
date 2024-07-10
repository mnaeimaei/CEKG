import * as c20Module from "./C20_neo4j_Converting_Mdule.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";

document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C20 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c20Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c20Module.nextButtonFormSubmit, c20Module.formC20);


});
