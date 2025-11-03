# README.md

# Project Title

## Introduction
[Brief description of the project and its purpose]

## Setup Instructions
[Instructions on how to set up and run the application]

## API Endpoints
[Documentation of the API endpoints, methods, request/response formats]

## Assumptions
1. The users of the application are familiar with consuming REST APIs and JSON.
2. The application will be hosted in an environment that supports the execution of Python 3.11+ without dependency conflicts.
3. There is a requirement for simplicity; hence complex authentication or authorization mechanisms will not be implemented in this version.

## Known Limitations
- **Database**: SQLite has been chosen for its simplicity and zero-configuration setup for development purposes. It's important to note that SQLite may not perform well under high concurrency, which could affect its usability in high-traffic production environments.
- **Framework**: Flask was selected for its ease of use and rapid development capabilities. However, the simplicity of Flask means that more complex features may require additional libraries or frameworks to implement effectively.
- **Scalability**: The application has been designed with minimal components for straightforward deployment and development. As such, scaling may involve significant refactoring or architectural changes if needed in the future.

## Contributing
[Instructions for contributing to the project]

## License
[Details about the license governing the project]