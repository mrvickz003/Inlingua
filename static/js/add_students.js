function showSection(sectionId, completedStep) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(function (section) {
        section.classList.remove('activate');
    });
    // Show the selected section
    document.getElementById(sectionId).classList.add('activate');

    // Mark the step as completed
    if (completedStep) {
        document.getElementById(completedStep).classList.remove('text-muted', 'text-secondary');
        document.getElementById(completedStep).classList.add('text-primary');
    }
}

function validateAndSubmitForm() {
    let isValid = true;

    // Validate each field
    const studentname = document.getElementById('studentname').value.trim();
    const studentmobilenumber = document.getElementById('studentmobilenumber').value.trim();
    const email = document.getElementById('email').value.trim();
    const studentdob = document.getElementById('studentdob').value.trim();
    const studentaadharcard = document.getElementById('studentaadharcard').value.trim();
    const language = document.getElementById('language-select').value.trim();
    const level = document.getElementById('level-select').value.trim();
    const courseType = document.getElementById('Course-type').value.trim();
    const counselor = document.getElementById('nameOfCounselor').value.trim();
    const paymentType = document.getElementById('Payment-type').value.trim();
    const transactionId = document.getElementById('transactionid').value.trim();
    const accountHolderName = document.getElementById('account-holder-name').value.trim();
    const accountNumber = document.getElementById('account-number').value.trim();
    const balanceAmount = document.getElementById('balanceamount').value.trim();

    // Check if any required field is empty
    if (studentname === '') {
        document.getElementById('studentname-error').textContent = 'Student Name is required';
        isValid = false;
    } else {
        document.getElementById('studentname-error').textContent = '';
    }
    if (studentmobilenumber === '') {
        document.getElementById('studentmobilenumber-error').textContent = 'Student Mobile number is required';
        isValid = false;
    } else {
        document.getElementById('studentmobilenumber-error').textContent = '';
    }
    if (email === '') {
        document.getElementById('email-error').textContent = 'Sudent Mail is required';
        isValid = false;
    } else {
        document.getElementById('email-error').textContent = '';
    }
    if (studentdob === '') {
        document.getElementById('studentdob-error').textContent = 'Student DOB is required';
        isValid = false;
    } else {
        document.getElementById('studentdob-error').textContent = '';
    }
    if (studentaadharcard === '') {
        document.getElementById('studentaadharcard-error').textContent = 'Student Aadhar is required';
        isValid = false;
    } else {
        document.getElementById('studentaadharcard-error').textContent = '';
    }
    if (language === '') {
        document.getElementById('language-error').textContent = 'Language is required';
        isValid = false;
    } else {
        document.getElementById('language-error').textContent = '';
    }
    if (level === '') {
        document.getElementById('level-error').textContent = 'Level and Hours is required';
        isValid = false;
    } else {
        document.getElementById('level-error').textContent = '';
    }
    if (courseType === '') {
        document.getElementById('course-type-error').textContent = 'Course Type is required';
        isValid = false;
    } else {
        document.getElementById('course-type-error').textContent = '';
    }
    if (counselor === '') {
        document.getElementById('counselor-error').textContent = 'Counselor is required';
        isValid = false;
    } else {
        document.getElementById('counselor-error').textContent = '';
    }
    if (paymentType === '') {
        document.getElementById('payment-type-error').textContent = 'Payment Type is required';
        isValid = false;
    } else {
        document.getElementById('payment-type-error').textContent = '';
    }
    if (transactionId === '') {
        document.getElementById('transactionid-error').textContent = 'Transaction ID is required';
        isValid = false;
    } else {
        document.getElementById('transactionid-error').textContent = '';
    }
    if (accountHolderName === '') {
        document.getElementById('account-holder-name-error').textContent = 'Account Holder Name is required';
        isValid = false;
    } else {
        document.getElementById('account-holder-name-error').textContent = '';
    }
    if (accountNumber === '') {
        document.getElementById('account-number-error').textContent = 'Account Paide is required';
        isValid = false;
    } else {
        document.getElementById('account-number-error').textContent = '';
    }
    if (balanceAmount === '') {
        document.getElementById('balanceamount-error').textContent = 'Balance Amount is required';
        isValid = false;
    } else {
        document.getElementById('balanceamount-error').textContent = '';
    }

    if (!isValid) {
        alert('Please fill in all This field is required fields.');
        return false; // Prevent form submission
    }

    // If all validations pass, submit the form
    document.getElementById('student-form').submit();
}

function updateLevels() {
    const languageId = document.getElementById('language-select').value;
    const levelSelect = document.getElementById('level-select');
    levelSelect.innerHTML = '<option value="">Select Language Level</option>'; // Reset options

    if (languageId) {
        fetch(`/get_levels/${languageId}/`)
            .then(response => response.json())
            .then(data => {
                data.levels.forEach(level => {
                    const option = document.createElement('option');
                    option.value = level.id;
                    option.textContent = `${level.Level} -- ${level.Hours} -- ${level.Help_Text}`;
                    levelSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching levels:', error));
    }
}