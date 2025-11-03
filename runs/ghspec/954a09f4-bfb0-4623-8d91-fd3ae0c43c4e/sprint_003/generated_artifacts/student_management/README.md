# student_management/README.md

# Student Management System

## Environment Setup

To set up the environment for the Student Management System, follow the steps below:

### Prerequisites

- Ensure you have Python 3.7 or above installed on your machine.
- Ensure you have `pip` available for package management.

### Setup Environment

1. **Clone the repository**:
   ```bash
   git clone https://your-repository-url.git
   cd student_management
   ```

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install or update necessary dependencies**:
   ```bash
   pip install Flask SQLAlchemy
   ```

4. **Setup environment variables**:
   - Create a `.env` file based on `.env.example` to configure environment-specific settings.

### Database Migration

Before running the application, ensure the database is set up correctly. This includes applying any migrations that have been created. 

1. **Example migration script**:
   Create a new migration script to add the `courses` table along with the required fields:
   ```python
   """Create courses table"""
   from alembic import op
   import sqlalchemy as sa

   # revision identifiers, used by Alembic.
   revision = 'xxxxxx'
   down_revision = 'previous_revision'

   def upgrade():
       op.create_table('courses',
           sa.Column('id', sa.Integer(), nullable=False),
           sa.Column('name', sa.String(), nullable=False),
           sa.Column('level', sa.String(), nullable=False),
           sa.PrimaryKeyConstraint('id')
       )

   def downgrade():
       op.drop_table('courses')
   ```

### Create Application Structure

Make sure your project directory follows the structure shown below to maintain organization and ease of use.

```
student_management/
├── src/
│   ├── app.py
│   ├── models.py    # Contains data models
│   ├── services.py   # Contains service layer logic
│   ├── repositories.py # Contains repository layer for database access
│   └── database.py
├── tests/
│   ├── test_courses.py # Contains unit tests for course functionalities
├── requirements.txt
├── .env.example
└── README.md
```

### Running the Application

After setting up your environment and migrating the database, you can run the application using:

```bash
flask run
```

### Testing

Make sure to run the tests to ensure everything is functioning correctly after setup:

```bash
pytest
``` 

This concludes the initial environment setup for the Student Management System. Follow the instructions provided above to get started.