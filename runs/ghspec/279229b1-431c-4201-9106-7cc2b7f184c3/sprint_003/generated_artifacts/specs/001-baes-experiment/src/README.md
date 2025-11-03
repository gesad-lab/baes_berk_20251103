# README.md

# Project Setup and Usage Instructions

## Running Migrations

To set up the database schema, including the new `Course` entity, you need to apply the migrations using Alembic. Follow the steps below:

### Step 1: Initialize Migrations (if not done already)

If you haven't initialized Alembic for your project, you can do so by running the following command:

```bash
alembic init migrations
```

### Step 2: Create a Migration for the `Course` Table

Next, generate a migration script to define the `Course` table structure. Use the following command:

```bash
alembic revision --autogenerate -m "Create courses table"
```

This command will create a new migration file in the `migrations/versions` directory.

### Step 3: Apply the Migration

To apply the migration and update your database schema, execute the following command:

```bash
alembic upgrade head
```

This will apply the latest migration, including the new `courses` table, while ensuring that existing data related to the `Student` entity remains intact.

## User Scenarios & Testing

1. **Scenario 1**: A user creates a new course with a name and level.
   - **Test**: When the user provides a valid name and level for the course, a new Course record should be created, returning a success response.

2. **Scenario 2**: A user attempts to create a course without providing a name.
   - **Test**: The application should return an error indicating that the name field is required.

3. **Scenario 3**: A user attempts to create a course without providing a level.
   - **Test**: The application should return an error indicating that the level field is required.

4. **Scenario 4**: A user retrieves the list of courses available in the system.
   - **Test**: The application should return a list of all existing Course records formatted as JSON, including their name and level.

5. **Scenario 5**: The user examines the database schema to ensure the Course entity exists without affecting existing Student data.
   - **Test**: The database schema should reflect the inclusion of the new Course table after migration.

## Functional Requirements
1. The Course entity must contain the following fields:
   - `name` (string, required)
   - `level` (string, required)

2. The system must support a route to create a course with the following properties:
   - Endpoint: `POST /courses`
   - Request body must include a JSON object containing `{ "name": "string", "level": "string" }`.

3. The system must support a route to retrieve all courses:
   - Endpoint: `GET /courses`
   - Response must include a JSON array of course objects with properties `name` and `level`.

4. Update the database schema to include the Course table, ensuring that existing data related to the Student entity is preserved through a reliable migration strategy.

## Success Criteria
1. The application must successfully create a course when provided with valid data (name and level).
2. The application must reject requests to create courses without a name, returning a clear error.

... [Continue with the rest of the documentation as required] ...