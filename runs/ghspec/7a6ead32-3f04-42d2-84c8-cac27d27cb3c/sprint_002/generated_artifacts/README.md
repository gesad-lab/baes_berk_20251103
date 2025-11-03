# README.md

# Project Title

## Migration Instructions

### Adding Email Field to Student Table

In this migration, we will be adding a new `email` field to the existing `Student` table in the database schema. This field is required and must conform to standard email format. 

#### Migration Steps

1. **Backup Your Database**: Before proceeding with any migrations, ensure that you have a backup of your existing database. This will help prevent data loss in case something goes wrong during the migration.

2. **Create a Migration Script**:
   - You can use Alembic to create a migration script. Run the following command in your terminal:
     ```bash
     alembic revision --autogenerate -m "Add email field to Student table"
     ```

3. **Modify the Migration Script**: 
   - Open the generated migration script in the `migrations` folder and update the `upgrade()` function to include the following:
     ```python
     def upgrade():
         # Add email column with required constraint
         op.add_column('student', sa.Column('email', sa.String(), nullable=False))
     ```

4. **Downgrade Step**: Always provide a way to undo the migration:
   ```python
   def downgrade():
       # Remove email column
       op.drop_column('student', 'email')
   ```

5. **Run the Migration**: Once the migration script is ready, apply the migration by running:
   ```bash
   alembic upgrade head
   ```

6. **Validate the Migration**:
   - After running the migration, verify that the `email` field has been added to the `Student` table. You can do this by connecting to your database and running a query to describe the `student` table.

7. **Update Application Logic**:
   - Ensure that the application code is updated to handle the new `email` field by:
     - Validating user inputs for the email format.
     - Including the email in all relevant API responses pertaining to the `Student` entity.

### Important Notes
- Make sure all existing student records are checked for compliance with the new schema. If there are existing records, you may need to provide default values or handle null cases accordingly.
- Unauthorized or invalid email inputs must be managed gracefully in your application logic, triggering appropriate error responses.

Following these migration instructions will ensure that your database schema updates smoothly while preserving existing data.