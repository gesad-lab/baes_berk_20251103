```
# README.md
# Educational Management System

## Setup
To run the application, ensure you have the necessary dependencies:

```bash
pip install Flask SQLAlchemy Flask-Migrate
```

## Testing

### Teacher Creation Tests
To ensure that teacher creation functionality works as expected, we have implemented the following tests:

1. **Creating a Teacher**
   - **Scenario**: A user submits a request to create a new Teacher with the required fields.
   - **Test**: Verify that the Teacher is created successfully and that the response contains the correct name and email of the newly created Teacher.

   ```python
   def test_create_teacher_success(client):
       response = client.post('/teachers', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
       assert response.status_code == 201
       json_data = response.get_json()
       assert json_data['message'] == 'Teacher created successfully.'
       assert json_data['teacher']['name'] == 'John Doe'
       assert json_data['teacher']['email'] == 'john.doe@example.com'
   ```

2. **Validating Teacher Creation**
   - **Scenario**: A user attempts to create a Teacher without providing a name or an email.
   - **Test**: Confirm that the system returns an appropriate error message indicating that both fields are required.

   ```python
   def test_create_teacher_missing_fields(client):
       response = client.post('/teachers', json={})
       assert response.status_code == 400
       json_data = response.get_json()
       assert json_data['error']['code'] == 'E001'
       assert json_data['error']['message'] == 'Both name and email are required.'
   ```

3. **Database Migration Testing**
   - **Scenario**: After the new Teacher table is added, a user checks for existing Student and Course data in the database.
   - **Test**: Validate that Student and Course data remains intact, with no loss of information due to the new Teacher table creation.

   ```python
   def test_database_migration_preserves_data(client):
       # Assuming initial data setup here
       # Validate student and course data remain intact after migration
       response = client.get('/students')
       students = response.get_json()
       assert len(students) > 0  # Assuming there were students before the test

       response = client.get('/courses')
       courses = response.get_json()
       assert len(courses) > 0  # Assuming there were courses before the test
   ```

4. **Retrieving Teacher Data**
   - **Scenario**: A user requests to retrieve details of the teacher just created.
   - **Test**: Ensure that the returned Teacher data matches the input data used during creation.

   ```python
   def test_retrieve_teacher_success(client):
       create_response = client.post('/teachers', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
       teacher_id = create_response.get_json()['teacher']['id']
       
       response = client.get(f'/teachers/{teacher_id}')
       assert response.status_code == 200
       
       json_data = response.get_json()
       assert json_data['name'] == 'Jane Doe'
       assert json_data['email'] == 'jane.doe@example.com'
   ```

These tests can be run using `pytest` to ensure that the teacher-related functionalities work correctly and meet the specifications outlined in the User Scenarios & Testing section.

## Usage Notes
- Make sure to run database migrations before testing.
- Check `.env.example` for environment configuration details and adjust your `.env` file accordingly.
```