import * as p1Module from "./A1_home_Module.js";

document.addEventListener('DOMContentLoaded', function() {
    console.log("Document 1 is ready!");


    p1Module.MainDfgFormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            console.log("main DFG button was changed!");
            p1Module.resetForm(p1Module.Dfg1DivContainer);
            p1Module.resetForm(p1Module.Dfg2DivContainer);
            p1Module.resetForm(p1Module.Dfg3DivContainer);
            p1Module.resetForm(p1Module.Dfg4DivContainer);
            p1Module.resetForm(p1Module.Dfg5DivContainer);
            p1Module.resetForm(p1Module.Dfg6ivContainer);
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainer);
        });
    });


    p1Module.MainDfgFormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("dfg1Mode");
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'block';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';


            }if (this.value === 'dfg2Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'block';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';


            }if (this.value === 'dfg3Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'block';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';


            }if (this.value === 'dfg4Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'block';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';


            }if (this.value === 'dfg5Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'block';
                p1Module.Dfg6ivContainer.style.display = 'none';


            }if (this.value === 'dfg6Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'block';


            }if (this.value !== 'dfg1Mode' && this.value !== 'dfg2Mode' && this.value !== 'dfg3Mode' && this.value !== 'dfg4Mode' && this.value !== 'dfg5Mode' && this.value !== 'dfg6Mode') {
                console.log("Document ewewewe is ready!");
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';

            }
        });
    });



});




