import * as c31Module from "./C31_neo4j_DK3_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";




document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C31 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c31Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c31Module.nextButtonFormSubmit, c31Module.formC31);


});
