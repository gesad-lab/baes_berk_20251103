```javascript
// src/static/scripts.js

// Base URL for the API
const API_BASE_URL = '/students';

/**
 * Creates a new student by sending a POST request to the API.
 * @param {string} name - The name of the student to create.
 * @returns {Promise<Response>} - The response from the server.
 */
async function createStudent(name) {
    if (!name) {
        throw new Error('Name is required to create a student'); // Validate input
    }
    
    const response = await fetch(API_BASE_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name }), // Send name as JSON
    });
    
    if (!response.ok) {
        const errorData = await response.json(); // Parse error response
        throw new Error(errorData.error.message || 'An error occurred while creating the student');
    }
    
    return response.json(); // Return the created student data
}

/**
 * Retrieves all students by sending a GET request to the API.
 * @returns {Promise<Array>} - A list of students.
 */
async function getStudents() {
    const response = await fetch(API_BASE_URL);

    if (!response.ok) {
        const errorData = await response.json(); // Parse error response
        throw new Error(errorData.error.message || 'An error occurred while retrieving students');
    }

    return response.json(); // Return the list of student names
}

// Example usage of createStudent and getStudents
// These could be triggered by user interactions in the application

// Function to handle the creation of a student
async function handleCreateStudent() {
    const studentName = document.getElementById('student-name').value;
    try {
        const newStudent = await createStudent(studentName);
        console.log('Student created:', newStudent);
        // Additional logic to update UI with the new student
    } catch (error) {
        console.error(error.message); // Show error to the user
    }
}

// Function to handle retrieving students
async function handleGetStudents() {
    try {
        const students = await getStudents();
        console.log('Retrieved students:', students);
        // Additional logic to update the UI with the student list
    } catch (error) {
        console.error(error.message); // Show error to the user
    }
}

// Event listeners can be attached to buttons to trigger these functions
document.getElementById('create-student-button').addEventListener('click', handleCreateStudent);
document.getElementById('retrieve-students-button').addEventListener('click', handleGetStudents);
```