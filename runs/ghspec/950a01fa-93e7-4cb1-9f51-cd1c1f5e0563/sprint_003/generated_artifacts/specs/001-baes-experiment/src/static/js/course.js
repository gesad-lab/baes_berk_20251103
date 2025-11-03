```javascript
// File: static/js/course.js

// Function to create a new course
async function createCourse(name, level) {
    // Validate required fields
    if (!name) {
        return handleError({ code: "E001", message: "Name is required" });
    }
    if (!level) {
        return handleError({ code: "E002", message: "Level is required" });
    }

    try {
        const response = await fetch('/courses', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, level })
        });

        if (!response.ok) {
            const errorData = await response.json();
            return handleError(errorData.error);
        }

        const course = await response.json();
        return course;  // Successfully created course object
    } catch (error) {
        // Log and handle unexpected errors
        console.error('Error creating course:', error);
        handleError({ code: "E003", message: "An unexpected error occurred." });
    }
}

// Function to retrieve all courses
async function getCourses() {
    try {
        const response = await fetch('/courses');

        if (!response.ok) {
            const errorData = await response.json();
            return handleError(errorData.error);
        }
        
        const courses = await response.json();
        return courses;  // Successfully retrieved list of courses
    } catch (error) {
        // Log and handle unexpected errors
        console.error('Error retrieving courses:', error);
        handleError({ code: "E003", message: "An unexpected error occurred." });
    }
}

// Function to handle displaying errors to the user
function handleError(error) {
    // Display error message to the user (this function should be implemented accordingly)
    console.error(`Error ${error.code}: ${error.message}`);
    alert(`Error: ${error.message}`);
}

// Event listeners or UI integration to call createCourse and getCourses would be set up here
// Example: document.querySelector('#createCourseButton').addEventListener('click', () => createCourse(courseName, courseLevel));

// Initialization code to fetch and display courses on page load can be added
document.addEventListener('DOMContentLoaded', async () => {
    const courses = await getCourses();
    console.log('Retrieved courses:', courses);
});
```