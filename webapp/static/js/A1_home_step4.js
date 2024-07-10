import * as p1Module  from "./A1_home_Module.js";
import {ActivityDivContainerDFG6, InputDivDfg6Container} from "./A1_home_Module.js";

document.addEventListener('DOMContentLoaded', function() {
    console.log("Document 4 is ready!");


    const checkAndDisplaynextButton1DivContainer = function() {
        let selectedMainDFGOption = null;
        p1Module.MainDfgFormRadioButtons.forEach(function(radioButton) {
            if (radioButton.checked) {
                selectedMainDFGOption = radioButton.value;
            }
        });

        let isDFGFormSelected = false;
        switch (selectedMainDFGOption) {
            case 'dfg1Mode':
                isDFGFormSelected = p1Module.isAnyRadioButtonSelected(p1Module.Dfg1DivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.InputDivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.ActivityDivContainer);
                break;
            case 'dfg2Mode':
                isDFGFormSelected = p1Module.isAnyRadioButtonSelected(p1Module.Dfg2DivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.InputDivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.ActivityDivContainer);
                break;
            case 'dfg3Mode':
                isDFGFormSelected = p1Module.isAnyRadioButtonSelected(p1Module.Dfg3DivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.InputDivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.ActivityDivContainer);
                break;
            case 'dfg4Mode':
                isDFGFormSelected = p1Module.isAnyRadioButtonSelected(p1Module.Dfg4DivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.InputDivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.ActivityDivContainer);
                break;
            case 'dfg5Mode':
                isDFGFormSelected = p1Module.isAnyRadioButtonSelected(p1Module.Dfg5DivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.InputDivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.ActivityDivContainer) ;
                break;
            case 'dfg6Mode':
                isDFGFormSelected = p1Module.isAnyRadioButtonSelected(p1Module.Dfg6ivContainer) && p1Module.isAnyRadioButtonSelected(p1Module.InputDivDfg6Container) && p1Module.isAnyRadioButtonSelected(p1Module.ActivityDivContainerDFG6);
                break;
            default:
                isDFGFormSelected = false;
        }

        console.log("isDFGFormSelected");
        if (isDFGFormSelected) {
            p1Module.nextButton1DivContainer.style.display = 'block';}
        else {
            p1Module.nextButton1DivContainer.style.display = 'none';
        }
    };




    // Attach change event listener to all radio buttons in mainDFG and DFG forms
    p1Module.MainDfgFormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', checkAndDisplaynextButton1DivContainer);
    });


    [p1Module.Dfg1DivContainer, p1Module.Dfg2DivContainer, p1Module.Dfg3DivContainer, p1Module.Dfg4DivContainer, p1Module.Dfg5DivContainer, p1Module.Dfg6ivContainer, p1Module.InputDivContainer,p1Module.InputDivDfg6Container, p1Module.ActivityDivContainer, p1Module.ActivityDivContainerDFG6].forEach(function(formContainer) {
        const radioButtons = formContainer.querySelectorAll('input[type="radio"]');
        radioButtons.forEach(function(radioButton) {
            radioButton.addEventListener('change', checkAndDisplaynextButton1DivContainer);
        });
    });






document.addEventListener('DOMContentLoaded', function() {

    p1Module.nextButton1FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allForm').submit(); // Submit the form


        });

});
});




