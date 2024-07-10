
import * as p2Module from "./A2_downloading_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";
import {progressBarContainerDiv} from "./A2_downloading_Module.js";





document.addEventListener('DOMContentLoaded', function() {
    console.log("Document 2.1 is ready!");


    p2Module.fileSourceForm.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            console.log("file source selection was changed!");
            p2Module.resetTextBoxes(p2Module.fileNameDivContainer);
            p2Module.resetForm(p2Module.fileLocationDivContainer);
            p2Module.resetForm(p2Module.fileKeyDivContainer);

        });
    });






    p2Module.fileSourceForm.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            if (this.value === '1' ) {
            p2Module.fileNameDivContainer.style.display = 'block';
            p2Module.fileLocationDivContainer.style.display = 'none';
            p2Module.fileKeyDivContainer.style.display = 'block';
            p2Module.fileNameForm.value=p2Module.gDefaultFileName;
            p2Module.fileKeyForm.value=p2Module.gDefaultKey;
            p2Module.fileLocationForm.required=false;
            p2Module.fileKeyForm.required=true;
            p2Module.nextButton2DivContainer.style.display = 'block';
            p2Module.progressBarContainerDiv.style.display = 'block';





            }if (this.value === '2' ) {
            p2Module.fileNameDivContainer.style.display = 'block';
            p2Module.fileLocationDivContainer.style.display = 'block';
            p2Module.fileKeyDivContainer.style.display = 'none';
            p2Module.fileNameForm.value=p2Module.lDefaultFileName;
            p2Module.fileLocationForm.value=p2Module.lDefaultLocation;

            p2Module.fileLocationForm.required=true;
            p2Module.fileKeyForm.required=false;
            p2Module.nextButton2DivContainer.style.display = 'block';
            p2Module.progressBarContainerDiv.style.display = 'block';



            }if (this.value !== '1' && this.value !== '2' ) {
            p2Module.fileNameDivContainer.style.display = 'none';
            p2Module.fileLocationDivContainer.style.display = 'none';
            p2Module.fileKeyDivContainer.style.display = 'none';
            p2Module.nextButton2DivContainer.style.display = 'none';
            p2Module.progressBarContainerDiv.style.display = 'none';
            p2Module.fileLocationForm.required=false;
            p2Module.fileKeyForm.required=false;
            }
        });
    });


const ws = progressBarModule.setupWebSocketProgressBar(p2Module.progressBar);
console.log("ws created");

progressBarModule.handleFormSubmission(ws, p2Module.nextButton2FormSubmit, p2Module.form2);




});




