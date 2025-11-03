#!/bin/bash

# Create the tests directory for unit tests
# This directory will hold all test cases for the application, ensuring a structured approach to testing

TESTS_DIR="tests"

# Check if the tests directory already exists
if [ ! -d "$TESTS_DIR" ]; then
  # Create the tests directory
  mkdir "$TESTS_DIR"
  echo "Tests directory created successfully."
else
  echo "Tests directory already exists."
fi