export const nextButton2FormSubmit = document.querySelector('#nextButton3Div input[name="nextButton1Mode"]');


export const mainDropDownButton = document.getElementById('id_dynamic_choice_B4_1');


export const optionsContainerB41 = document.getElementById('optionsContainer1');
export const optionsToShowB41 = JSON.parse(optionsContainerB41.getAttribute('data-options-b41'));


export const optionsContainerB42 = document.getElementById('optionsContainer2');
export const optionsToShowB42 = JSON.parse(optionsContainerB42.getAttribute('data-options-b42'));

export const buttonContainerB41 = document.getElementById('buttonContainer1');
export const buttonToShowB41 = JSON.parse(buttonContainerB41.getAttribute('data-options-b43'));


export const buttonContainerB42 = document.getElementById('buttonContainer2');
export const buttonToShowB42 = JSON.parse(buttonContainerB42.getAttribute('data-options-b44'));


export const defaultMainDropValue = document.querySelector('#id_dynamic_choice_B4_1').value;


function updateDropdownVisibility(buttonToShow, optionsToShowDefault, buttonToShowList, optionsToShowDefaultList) {
    document.getElementById('id_dynamic_choice_B4_1').addEventListener('change', function () {
        console.log("Dropdown changed to: " + this.value);

        const buttonToShow_2 = buttonToShowList[buttonToShowList.length - 1];
        const mergedButtonToShow = [...buttonToShow, ...buttonToShow_2];
        console.log("mergedButtonToShow:", mergedButtonToShow);

        mergedButtonToShow.forEach((option) => {
            const dropdownElement = document.getElementById(option);
            if (dropdownElement) {
                dropdownElement.style.display = 'none'; // Hide the dropdown
                const selectElement = dropdownElement.querySelector('select');
                if (selectElement) {
                    console.log("YesYesYesYesYes");
                    selectElement.disabled = true; // Disable the select element
                }
            }
        });


        // Additional logic based on the selected value
        if (this.value !== '0') {
            console.log("Selected " + this.value + " entities");
            const indexLoL = parseInt(this.value) - 1;

            const buttonToShow_2 = buttonToShowList[indexLoL];
            const mergedButtonToShow = [...buttonToShow, ...buttonToShow_2];
            console.log("mergedButtonToShow:", mergedButtonToShow);


            const optionsToShowDefault_2 = optionsToShowDefaultList[indexLoL];
            const mergedOptionsToShowDefault = [...optionsToShowDefault, ...optionsToShowDefault_2];
            console.log("mergedOptionsToShowDefault:", mergedOptionsToShowDefault);


            mergedButtonToShow.forEach((option, index) => {
                const dropdownElement = document.getElementById(option);
                if (dropdownElement) {
                    dropdownElement.style.display = 'block'; // Show the dropdown
                    const selectElement = dropdownElement.querySelector('select');
                    if (selectElement) {
                        selectElement.disabled = false; // Enable the select element for submission
                        // Set the value based on optionsToShowDefault
                        const defaultValue = mergedOptionsToShowDefault[index];
                        // Assuming you have the text values as options in your select
                        for (let option of selectElement.options) {
                            if (option.text === defaultValue) {
                                console.log("mergedOptionsToShowDefault:", option.text);
                                option.selected = true;
                                break;

                            }
                        }
                    }
                }
            });


        }
    });
}

export {updateDropdownVisibility};




