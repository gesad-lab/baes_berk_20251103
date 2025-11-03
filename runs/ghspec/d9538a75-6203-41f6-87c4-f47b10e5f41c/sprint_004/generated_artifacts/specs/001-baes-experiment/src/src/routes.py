from flask import Flask, jsonify, request
from models import StudentCourses, Course  # Assuming Course model exists
from database import session

app = Flask(__name__)

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_courses_for_student(student_id):
    """
    Retrieve a list of courses associated with a student.
    
    :param student_id: The ID of the student whose courses are being retrieved.
    :return: JSON response with list of courses or an empty list if none are found.
    """
    try:
        # Query to find courses associated with the given student
        courses = session.query(StudentCourses.course_id).filter(StudentCourses.student_id == student_id).all()
        # Extract course IDs from query results
        course_ids = [course[0] for course in courses]
        
        if not course_ids:
            # Return an empty list if no courses are found
            return jsonify([]), 200
        
        # Fetch course details based on course IDs
        course_details = session.query(Course).filter(Course.id.in_(course_ids)).all()
        # Convert course objects to dictionaries for JSON response
        course_list = [{"id": course.id, "name": course.name} for course in course_details]

        return jsonify(course_list), 200

    except Exception as e:
        # Log error details (not exposing stack trace to the user)
        app.logger.error(f"Error retrieving courses for student {student_id}: {e}")
        return jsonify({"error": {"code": "E500", "message": "Internal error occurred."}}), 500

# Ensure that the Flask app runs if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)