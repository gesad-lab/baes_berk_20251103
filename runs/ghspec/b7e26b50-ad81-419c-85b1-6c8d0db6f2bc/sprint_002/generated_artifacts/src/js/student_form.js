```javascript
// src/js/student_form.js

// Function to handle the form submission for creating or updating a student
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Collect form data
    const formData = new FormData(event.target);
    const studentData = {
        name: formData.get('name'),
        email: formData.get('email'), // Capture the new email field
    };

    // Validate the input data
    if (!studentData.name || !studentData.email) {
        // Display a message if name or email is missing
        displayError("Name and email are required.");
        return;
    }

    // Determine endpoint
    const studentId = formData.get('studentId');
    const endpoint = studentId ? `/students/${studentId}` : '/students';

    // Select the appropriate HTTP method based on the presence of studentId
    const method = studentId ? 'PUT' : 'POST';

    // Make the API request
    fetch(endpoint, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(studentData), // Convert the student data to JSON for the request
    })
    .then(response => {
        if (!response.ok) {
            // Handle errors based on response status
            return response.json().then(error => {
                throw new Error(error.message || "An error occurred during the submission.");
            });
        }
        return response.json(); // Parse the response as JSON if successful
    })
    .then(data => {
        // Display a success message or update the UI as necessary
        displaySuccess(`Student ${data.email} created/updated successfully!`);
    })
    .catch(error => {
        // Display any errors encountered during the fetch
        displayError(error.message);
    });
}

// Function to display error messages
function displayError(message) {
    const errorContainer = document.getElementById('error-container');
    errorContainer.textContent = message; // Set error message text
    errorContainer.style.display = 'block'; // Make sure the error container is visible
}

// Function to display success messages
function displaySuccess(message) {
    const successContainer = document.getElementById('success-container');
    successContainer.textContent = message; // Set success message text
    successContainer.style.display = 'block'; // Make sure the success container is visible
}

// Attach the form submit event listener
document.getElementById('student-form').addEventListener('submit', handleFormSubmit);

// Ensure to initialize the form correctly on page load, setting the existing data if editing
function initializeForm(student) {
    if (student) {
        document.getElementById('studentId').value = student.id; // Set student ID for updates
        document.getElementById('name').value = student.name; // Set existing student name
        document.getElementById('email').value = student.email; // Set existing email if editing
    }
}

// Example of how to call initializeForm on page load with existing student data (if any)
// const existingStudent = fetchStudentById(studentId); // Fetch student data based on ID
// initializeForm(existingStudent);
```