#!/bin/bash

# upgrade_script.sh - Script to apply database migrations for the course relationship feature

# Ensure that the script fails on any command failure
set -e

# Step 1: Generate a migration script for creating the junction table
echo "Generating migration script..."
flask db migrate -m "Create student_courses table for relationships"

# Step 2: Apply the generated migration to the database
echo "Applying migration..."
flask db upgrade

echo "Migration applied successfully."

# Optional: Output the current database state for verification
echo "Current database state:"
flask db current
echo "Migration completed."