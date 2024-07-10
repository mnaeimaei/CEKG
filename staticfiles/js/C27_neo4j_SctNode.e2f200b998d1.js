import * as c27Module from "./C27_neo4j_SctNode_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";


document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C27 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c27Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c27Module.nextButtonFormSubmit, c27Module.formC27);


});
