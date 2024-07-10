import * as p2Module from "./A02_downloading_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";
import {passDivContainer, userDivContainer} from "./A02_downloading_Module.js";



document.addEventListener('DOMContentLoaded', function () {
    console.log("Document 2.1 is ready!");



        p2Module.userForm.value = p2Module.deafaultUser;
    p2Module.passForm.value = p2Module.defaultPass;

        p2Module.userForm.required = true;
    p2Module.passForm.required = true;


p2Module.formUpload.addEventListener('submit', function(event) {
    if (!p2Module.userForm.checkValidity() || !p2Module.passForm.checkValidity()) {
        event.preventDefault();  // This stops the form from submitting if it's not valid
        console.log("Form validation failed");
    } else {
        console.log("Form is valid, submitting");
    }
});


});




