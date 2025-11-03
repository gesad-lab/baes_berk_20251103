# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to introduce a new Course entity within the existing system, enabling the storage and management of courses associated with students. Each Course will have a name and level, facilitating better organization and record-keeping within the educational context. This addition is crucial for accommodating the growing needs of educational institutions and for enhancing overall data management.

## User Scenarios & Testing
1. **Creating a Course**
   - **Scenario**: An user wants to create a new course with a name and level.
   - **Test**: The system should allow the user to submit a request to create a new course with valid name and level values. The response should confirm the creation with the Course's ID, name, and level.

2. **Retrieving Courses**
   - **Scenario**: A user wants to view all available courses.
   - **Test**: The user sends a request to retrieve a list of all courses. The system should return a JSON array containing all Course records, each with the name and level.

3. **Handling Missing Fields**
   - **Scenario**: A user tries to create a course without providing the name or level.
   - **Test**: If the user submits a request with a missing name or level, the system should respond with an appropriate error message indicating which fields are required.

4. **Data Persistence for Courses**
   - **Scenario**: After creating a course, a user restarts the application and checks the course list.
   - **Test**: The previously created course (with its name and level) should still be retrievable after the application restarts, confirming successful data persistence.

## Functional Requirements
1. The application must allow users to create a Course with both a name and level (both required).
2. The application must respond to requests with JSON formatted responses.
3. The Course entity must include:
   - `id`: Integer (auto-incremented, primary key)
   - `name`: String (required)
   - `level`: String (required)
4. The database schema should be updated to include the new Course table while preserving existing Student data.
5. The application must allow users to retrieve a list of all courses.

## Success Criteria
- The application must successfully create a Course with valid name and level 95% of the time during testing.
- The application must return a correct JSON response format for all endpoints without errors.
- The system must gracefully handle invalid input (missing name or level), returning appropriate error messages 100% of the time.
- After the application restarts, previously added courses must still be retrievable, ensuring data persistence.

## Key Entities
- **Course**:
  - `id`: Integer (auto-incremented, primary key)
  - `name`: String (required)
  - `level`: String (required)

## Assumptions
1. The application will be hosted in a controlled environment similar to previous sprints with necessary dependencies available.
2. Users of the application will be skilled in using APIs and sending requests via HTTP.
3. The development team will adhere to standard exception handling and data validation practices.

## Out of Scope
- User authentication and authorization measures are not included in this feature.
- Additional functionalities related to Course (such as enrollment or prerequisites) are outside the current scope.
- Frontend interfaces or UI elements facilitating Course interactions are not included; only backend API features are considered.