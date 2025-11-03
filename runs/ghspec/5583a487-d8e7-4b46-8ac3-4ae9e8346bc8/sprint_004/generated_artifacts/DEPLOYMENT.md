# DEPLOYMENT.md

## Deployment Instructions for StudentCourse Microservice

This document provides the necessary instructions to deploy the StudentCourse microservice application built with Flask and SQLite.

### 1. Prerequisites

Before deploying, ensure the following tools and services are set up:

- **Python 3.x**: Make sure you have Python installed.
- **Flask**: Install Flask using pip:
  ```
  pip install Flask
  ```
- **Flask-Migrate**: This tool is necessary for handling database migrations. Install it via pip:
  ```
  pip install Flask-Migrate
  ```
- **SQLite**: The application uses SQLite for local development and testing.
- **Heroku/AWS account**: Create an account on either Heroku or AWS for your application's deployment.

### 2. Clone the Repository

Clone the repository that contains the StudentCourse application:

```bash
git clone https://github.com/yourusername/StudentCourse.git
cd StudentCourse
```

### 3. Setup Development Environment

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Database Migration

1. **Initialize Flask-Migrate**:
   ```bash
   flask db init
   ```

2. **Create Migration Script**:
   Automatically generate a migration script for the `StudentCourse` junction table:
   ```bash
   flask db migrate -m "Create StudentCourse table"
   ```

3. **Apply Migrations**:
   Apply the migration to your local database:
   ```bash
   flask db upgrade
   ```

### 5. Create Environment Variables

Create a `.env` file in the root directory to configure your application. Example entries:

```
DATABASE_URL=sqlite:///students_courses.db
FLASK_ENV=development
```

**Important**: Ensure that sensitive configurations (such as production database URLs and API keys) are not hardcoded but rather defined through environment variables.

### 6. Prepare for Deployment

#### For Heroku:

1. **Login to Heroku**:
   ```bash
   heroku login
   ```

2. **Create a New Heroku App**:
   ```bash
   heroku create your-app-name
   ```

3. **Set Environment Variables** on Heroku:
   ```bash
   heroku config:set DATABASE_URL=your-production-database-url
   ```

4. **Deploy to Heroku**:
   Push your local codebase to Heroku:
   ```bash
   git push heroku main
   ```

5. **Run Migrations on Heroku**:
   After deployment, run the migration command on Heroku:
   ```bash
   heroku run flask db upgrade
   ```

#### For AWS:

Depending on your chosen AWS service (like EC2 or Elastic Beanstalk), follow AWS documentation to deploy Flask applications. Ensure the environment variables are set correctly on the AWS service you choose.

### 7. Health Check Endpoint

To ensure the application is running correctly, integrate health check endpoints. A simple example would be:

```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
```

### 8. Monitoring

Once deployed, use monitoring tools offered by Heroku or AWS to keep track of application performance, resource usage, and error rates.

### 9. Restarting the Application

For Heroku:
```bash
heroku restart
```

For AWS services, refer to the service-specific restart commands in the AWS management console.

### Conclusion

Following these steps will ensure a successful deployment of the StudentCourse microservice. For any issues, refer to the logs provided by Heroku or AWS to debug the issues.