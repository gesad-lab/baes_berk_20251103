# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to introduce a new Course entity within the application to facilitate the association and management of academic courses. By adding this Course entity, stakeholders will have the ability to define and categorize courses by their name and level, enriching the educational offerings within the system. This feature will enhance the data structure and prepare the system for future functionalities related to course management.

## User Scenarios & Testing
### User Scenario 1: Create a Course
**Given** I am a user of the application,  
**When** I provide a name and level for a new course,  
**Then** the course should be successfully created and stored in the database with both name and level attributes.

### User Scenario 2: Retrieve Courses
**Given** I have created several courses,  
**When** I request the list of courses,  
**Then** I should receive a JSON array of the courses with their name and level attributes.

### User Scenario 3: Handle Missing Course Fields
**Given** I attempt to create a course without providing a name or level,  
**When** I submit the request,  
**Then** I should receive an error response indicating that the name and level are required.

### User Scenario 4: Handle Invalid Level Format
**Given** I attempt to create a course with an invalid level format,   
**When** I submit the request,  
**Then** I should receive an error response indicating that the level is invalid.

## Functional Requirements
1. **Create Course (POST /courses)**
   - Input: JSON body with keys "name" (string, required) and "level" (string, required).
   - Output: Response with the created course object in JSON format containing both name and level.

2. **Retrieve Courses (GET /courses)**
   - Input: None (optional query parameters can be supported).
   - Output: JSON array containing all course objects with their name and level attributes.

3. **Validation**
   - Ensure both "name" and "level" fields are required strings.
   - Return appropriate error messages if the "name" or "level" is omitted.
   - Define valid formats for the "level" field (assume it might be "Beginner", "Intermediate", "Advanced") and validate accordingly.

4. **Database Migration**
   - Update the existing database schema to include a new Course table with "name" and "level" fields.
   - Migration must preserve existing Student data while adding the new Course table.

## Success Criteria
1. Success rate of course creation with valid name and level should be 95% or higher.
2. The application should accurately return a list of all courses with their names and levels without any errors.
3. Any attempts to create a course without a name or level should result in a clear error message 100% of the time.
4. The database migration must be completed successfully without data loss, ensuring that existing entities (namely Student) remain unaffected.

## Key Entities
- **Course**
  - Name: String (required)
  - Level: String (required)

## Assumptions
1. Users have a basic understanding of how to interact with RESTful APIs.
2. The application will use the same database as in the previous sprint, which supports schema updates.
3. The existing database setup allows for adding new tables without significant downtime.
4. There will be no extra fields in the Course entity beyond "name" and "level" within the scope of this feature.

## Out of Scope
- User authentication/authorization for course creation.
- Additional features such as updating or deleting courses.
- Handling of courses beyond the name and level fields.
- UI design or frontend implementation for course management.