from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from services.student import update_student_email

app = Flask(__name__)

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update a student's email.

    Args:
        student_id (int): The ID of the student to update.

    Returns:
        JSON response with the updated student information or an error message.
    """
    try:
        data = request.get_json()
        if not data or 'email' not in data:
            # Validate input
            raise BadRequest("E001: Invalid input - email is required.")

        email = data['email']

        # Call the update service method
        updated_student = update_student_email(student_id, email)

        return jsonify(updated_student), 200

    except BadRequest as e:
        return jsonify({"error": {"code": "E001", "message": str(e)}}), 400
    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"Error updating student {student_id}: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Failed to update student email."}}), 500

if __name__ == '__main__':
    app.run(debug=True)