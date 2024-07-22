
function student_details(nextSection, currentStepIcon) {
    const studentname = document.getElementById('studentname').value.trim();
    const studentmobilenumber = document.getElementById('studentmobilenumber').value.trim();
    const email = document.getElementById('email').value.trim();
    const studentdob = document.getElementById('studentdob').value.trim();
    const studentaadharcard = document.getElementById('studentaadharcard').value.trim();

    const nameRegex = /^[a-zA-Z\s]+$/;
    const numberRegex = /^\d{10}$/;
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    let isValid = true;

    if (studentname === '' ) {
        document.getElementById('studentname').style.border = '1px solid red';
        document.getElementById('studentname-error').textContent = 'Student Name is required';
        isValid = false;
    } else if(!nameRegex.test(studentname)){
        document.getElementById('studentname').style.border = '1px solid red';
        document.getElementById('studentname-error').textContent = 'Should not have special charecter';
        isValid = false;
    } else {
        document.getElementById('studentname').style.border = '';
        document.getElementById('studentname-error').textContent = '';
    }
    
    if (studentmobilenumber === '') {
        document.getElementById('studentmobilenumber').style.border = '1px solid red';
        document.getElementById('studentmobilenumber-error').textContent = 'Student Mobile number is required';
        isValid = false;
    } else if (!numberRegex.test(studentmobilenumber)){
        document.getElementById('studentmobilenumber').style.border = '1px solid red';
        document.getElementById('studentmobilenumber-error').textContent = 'Number should be Exactly 10 Digits';
        isValid = false;
    } 
    else {
        document.getElementById('studentmobilenumber').style.border = '';
        document.getElementById('studentmobilenumber-error').textContent = '';
    }
    
    if (email === '') {
        document.getElementById('email').style.border = '1px solid red';
        document.getElementById('email-error').textContent = 'Student Mail is required';
        isValid = false;
    } else if (!emailRegex.test(email)){
        document.getElementById('email').style.border = '1px solid red';
        document.getElementById('email-error').textContent = 'Mail should be Valid Mail Address';
        isValid = false;
    }
    else {
        document.getElementById('email').style.border = '';
        document.getElementById('email-error').textContent = '';
    }
    
    if (studentdob === '') {
        document.getElementById('studentdob').style.border = '1px solid red';
        document.getElementById('studentdob-error').textContent = 'Student DOB is required';
        isValid = false;
    } else {
        document.getElementById('studentdob').style.border = '';
        document.getElementById('studentdob-error').textContent = '';
    }
    
    if (studentaadharcard === '') {
        document.getElementById('studentaadharcard').style.border = '1px solid red';
        document.getElementById('studentaadharcard-error').textContent = 'Student Aadhar is required';
        isValid = false;
    } else {
        document.getElementById('studentaadharcard').style.border = '';
        document.getElementById('studentaadharcard-error').textContent = '';
    }

    if (isValid) {
        document.getElementById('step1-icon').classList.remove('text-muted');
        document.getElementById('step1-icon').classList.add('text-primary', 'step-completed');
        document.getElementById('student-details').classList.remove('activate');
        document.getElementById(nextSection).classList.add('activate');
    }
}

function go_studentdetails(){
    document.getElementById('step1-icon').classList.remove('text-primary','step-completed');
    document.getElementById('step1-icon').classList.add('text-muted');
    document.getElementById('student-details').classList.add('activate');
    document.getElementById('language-details').classList.remove('activate');
    document.getElementById('payment-details').classList.remove('activate');
}

function goto_payment(nextSection, currentStepIcon) {
    const language = document.getElementById('language-select').value.trim();
    const level = document.getElementById('level-select').value.trim();
    const courseType = document.getElementById('Course-type').value.trim();
    const counselor = document.getElementById('nameOfCounselor').value.trim();

    let isValid = true;

    if (language === '') {
        document.getElementById('language-select').style.border = '1px solid red';
        document.getElementById('language-error').textContent = 'Language is required';
        isValid = false;
    } else {
        document.getElementById('language-select').style.border = '';
        document.getElementById('language-error').textContent = '';
    }
    if (level === '') {
        document.getElementById('level-select').style.border = '1px solid red';
        document.getElementById('level-error').textContent = 'Level is required';
        isValid = false;
    } else {
        document.getElementById('level-select').style.border = '';
        document.getElementById('level-error').textContent = '';
    }
    if (courseType === '') {
        document.getElementById('Course-type').style.border = '1px solid red';
        document.getElementById('course-type-error').textContent = 'Course-type is required';
        isValid = false;
    } else {
        document.getElementById('Course-type').style.border = '';
        document.getElementById('course-type-error').textContent = '';
    }
    if (counselor === '') {
        document.getElementById('nameOfCounselor').style.border = '1px solid red';
        document.getElementById('counselor-error').textContent = 'Counselor is required';
        isValid = false;
    } else {
        document.getElementById('nameOfCounselor').style.border = '';
        document.getElementById('counselor-error').textContent = '';
    }
    
    if (isValid) {
        document.getElementById('step2-icon').classList.remove('text-secondary');
        document.getElementById('step2-icon').classList.add('text-primary', 'step-completed');
        document.getElementById('language-details').classList.remove('activate');
        document.getElementById(nextSection).classList.add('activate');
    }
}
function go_language(){
    document.getElementById('step2-icon').classList.remove('text-primary', 'step-completed');
    document.getElementById('step2-icon').classList.add('text-secondary');
    document.getElementById('language-details').classList.add('activate');
    document.getElementById('payment-details').classList.remove('activate');
}

function validateAndSubmitForm() {
    const paymentType = document.getElementById('Payment-type').value.trim();
    const transactionId = document.getElementById('transactionid').value.trim();
    const accountHolderName = document.getElementById('account-holder-name').value.trim();
    const accountNumber = document.getElementById('account-number').value.trim();
    const balanceAmount = document.getElementById('balanceamount').value.trim();

    let isValid = true;
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
        document.getElementById('account-number-error').textContent = 'Account Paid is required';
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
        alert('Please fill in all required fields.');
        return false; // Prevent form submission
    }

    document.getElementById('step3-icon').classList.remove('text-muted');
    document.getElementById('step3-icon').classList.add('text-primary');
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
                    option.textContent = `${level.level} -- ${level.hours}`;
                    levelSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching levels:', error));
    }
}