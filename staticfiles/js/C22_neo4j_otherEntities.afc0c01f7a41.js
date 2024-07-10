import * as c22Module from "./C22_neo4j_otherEntities_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";


document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C22 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c22Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c22Module.nextButtonFormSubmit, c22Module.formC22);


});
