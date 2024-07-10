import * as c33Module from "./C33_neo4j_DK5_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";




document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C33 is ready!");


    const ws = progressBarModule.setupWebSocketProgressBar(c33Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c33Module.nextButtonFormSubmit, c33Module.formC33);


});
