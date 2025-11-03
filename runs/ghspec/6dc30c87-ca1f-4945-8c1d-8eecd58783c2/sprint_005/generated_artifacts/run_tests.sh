```bash
#!/bin/bash

# run_tests.sh

# Creating a teacher entity API testing script

# Function to run API tests for creating a teacher
function test_create_teacher {
    echo "Running test for creating a teacher..."

    # Prepare the JSON payload for creating a teacher
    local teacher_json='{"name": "John Doe", "email": "john.doe@example.com"}'

    # Send POST request to create a teacher
    response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/json" -d "$teacher_json" http://localhost:8000/teachers)

    # Check if the response is 201 Created
    if [ "$response" -eq 201 ]; then
        echo "Test passed: Teacher created successfully."
    else
        echo "Test failed: Expected 201, got $response"
    fi
}

# Function to run API tests for retrieving a teacher
function test_retrieve_teacher {
    echo "Running test for retrieving a teacher..."

    # Assume that we have a teacher ID of 1 for testing
    local teacher_id=1

    # Send GET request to retrieve teacher details
    response=$(curl -s -o /dev/null -w "%{http_code}" -X GET http://localhost:8000/teachers/$teacher_id)

    # Check if the response is 200 OK
    if [ "$response" -eq 200 ]; then
        echo "Test passed: Successfully retrieved teacher details."
    else
        echo "Test failed: Expected 200, got $response"
    fi
}

# Function to run API tests for error handling when creating a teacher
function test_create_teacher_error_handling {
    echo "Running test for error handling during teacher creation..."

    # Prepare invalid JSON payload (missing name)
    local teacher_json_invalid='{"email": "invalid.email@example.com"}'

    # Send POST request to create a teacher with invalid data
    response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/json" -d "$teacher_json_invalid" http://localhost:8000/teachers)

    # Check if the response is 400 Bad Request
    if [ "$response" -eq 400 ]; then
        echo "Test passed: Correctly handled error for missing name."
    else
        echo "Test failed: Expected 400, got $response"
    fi
}

# Running all tests
test_create_teacher
test_retrieve_teacher
test_create_teacher_error_handling
```