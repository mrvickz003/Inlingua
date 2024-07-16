function validateFormTrainer() {
    // Retrieve form input values
    var name = document.getElementById('trainer_name').value.trim();
    var dob = document.getElementById('trainer_dob').value.trim();
    var education = document.getElementById('trainer_education').value.trim();
    var mail = document.getElementById('trainer_mail').value.trim();
    var phone = document.getElementById('trainer_phone').value.trim();
    var languages = document.getElementById('trainer_languages').value.trim();
    var address = document.getElementById('trainer_address').value.trim();
    var photo = document.getElementById('trainer_photo').value.trim();
    var bank = document.getElementById('trainer_bank').value.trim();
    var aadhar = document.getElementById('trainer_aadhar').value.trim();
    var role = document.getElementById('trainer_role').value.trim();

    // Validation flags
    var isValid = true;

    // Clear previous error messages
    document.getElementById('trainer-name-error').textContent = '';
    document.getElementById('trainer-dob-error').textContent = '';
    document.getElementById('trainer-mail-error').textContent = '';
    document.getElementById('trainer-phone-error').textContent = '';
    document.getElementById('trainer-language-error').textContent = '';
    document.getElementById('trainer-photo-error').textContent = '';
    document.getElementById('trainer-aadhar-error').textContent = '';

    // Validate Name
    if (name === '') {
        document.getElementById('trainer-name-error').textContent = 'Name is required';
        isValid = false;
    }

    // Validate DOB
    if (dob === '') {
        document.getElementById('trainer-dob-error').textContent = 'Date of Birth is required';
        isValid = false;
    }

    // Validate Email
    if (mail === '') {
        document.getElementById('trainer-mail-error').textContent = 'Email is required';
        isValid = false;
    } else if (!isValidEmail(mail)) {
        document.getElementById('trainer-mail-error').textContent = 'Enter a valid email';
        isValid = false;
    }

    // Validate Phone
    if (phone === '') {
        document.getElementById('trainer-phone-error').textContent = 'Phone number is required';
        isValid = false;
    } else if (!isValidPhone(phone)) {
        document.getElementById('trainer-phone-error').textContent = 'Enter a valid phone number';
        isValid = false;
    }

    // Validate Languages
    if (languages === '') {
        document.getElementById('trainer-language-error').textContent = 'Languages are required';
        isValid = false;
    }

    // Validate Photo
    if (photo === '') {
        document.getElementById('trainer-photo-error').textContent = 'Photo is required';
        isValid = false;
    }

    // Validate Aadhar
    if (aadhar === '') {
        document.getElementById('trainer-aadhar-error').textContent = 'Aadhar number is required';
        isValid = false;
    } else if (!isValidAadhar(aadhar)) {
        document.getElementById('trainer-aadhar-error').textContent = 'Enter a valid Aadhar number';
        isValid = false;
    }

    // Additional validation can be added as needed

    // Return validation result
    return isValid;
}

function isValidEmail(mail) {
    // Basic email validation regex
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(mail);
}

function isValidPhone(phone) {
    // Basic phone number validation regex (accepts numbers and optional '+', '-', '(' and ')')
    var phoneRegex = /^[\d()+-]+$/;
    return phoneRegex.test(phone);
}

function isValidAadhar(aadhar) {
    // Basic Aadhar number validation regex (accepts exactly 12 digits)
    var aadharRegex = /^\d{12}$/;
    return aadharRegex.test(aadhar);
}

