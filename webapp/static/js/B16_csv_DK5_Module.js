export const nextButton2FormSubmit = document.querySelector('#nextButton3Div input[name="nextButton1Mode"]');





 export  const optionsContainer = document.getElementById('optionsContainer');
 export    const optionsToShow = JSON.parse(optionsContainer.getAttribute('data-options-b16'));


 export     const optionsContainerDefault = document.getElementById('optionsContainerDefault');
 export    const optionsToShowDefault = JSON.parse(optionsContainerDefault.getAttribute('data-options-default-b16'));


function updateDropdownVisibility(optionsToShow,optionsToShowDefault) {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach((dropdown) => {
        dropdown.querySelector('select').disabled = true; // Disable them
    });

    optionsToShow.forEach((option, index) => {
        const dropdownElement = document.getElementById(option);
        if (dropdownElement) {
            const selectElement = dropdownElement.querySelector('select');
            if (selectElement) {
                selectElement.disabled = false; // Enable the select element for submission
                // Set the value based on optionsToShowDefault
                const defaultValue = optionsToShowDefault[index];
                // Assuming you have the text values as options in your select
                for (let option of selectElement.options) {
                    if (option.text === defaultValue) {
                        option.selected = true;
                        break;
                    }
                }
            }
        }
    });
}

export { updateDropdownVisibility };