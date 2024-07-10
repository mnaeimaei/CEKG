import * as c28Module from "./C28_neo4j_SctRel_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";


document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C28 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c28Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c28Module.nextButtonFormSubmit, c28Module.formC28);


});
