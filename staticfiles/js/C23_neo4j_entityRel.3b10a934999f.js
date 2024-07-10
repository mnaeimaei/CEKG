import * as c23Module from "./C23_neo4j_entityRel_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";


document.addEventListener('DOMContentLoaded', function () {

    console.log("Document C23 is ready!");



    const ws = progressBarModule.setupWebSocketProgressBar(c23Module.progressBar);

    progressBarModule.handleFormSubmission(ws, c23Module.nextButtonFormSubmit, c23Module.formC23);


});
