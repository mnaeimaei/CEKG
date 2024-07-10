import * as c24Module from "./C24_neo4j_activityProperties_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";


document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C24 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c24Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c24Module.nextButtonFormSubmit, c24Module.formC24);


});
