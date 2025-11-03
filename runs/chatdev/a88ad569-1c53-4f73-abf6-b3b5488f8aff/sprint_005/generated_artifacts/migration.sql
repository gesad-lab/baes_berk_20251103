-- Step 1: Add the email column as nullable
ALTER TABLE students ADD COLUMN email TEXT;
-- Step 2: (Optional) Populate the email column if needed
-- UPDATE students SET email = 'default@example.com' WHERE email IS NULL;
-- Step 3: Alter the column to be non-nullable if necessary
-- Note: This step can be skipped if you choose to keep it nullable
-- ALTER TABLE students ALTER COLUMN email SET NOT NULL;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);