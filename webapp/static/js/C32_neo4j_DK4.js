import * as c32Module from "./C32_neo4j_DK4_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";




document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C32 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c32Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c32Module.nextButtonFormSubmit, c32Module.formC32);


});
