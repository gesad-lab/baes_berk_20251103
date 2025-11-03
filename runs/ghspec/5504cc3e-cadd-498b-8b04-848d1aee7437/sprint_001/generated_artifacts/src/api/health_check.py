from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify that the server and database are accessible."""
    try:
        # Attempt to connect to the SQLite database
        conn = sqlite3.connect('students.db')
        conn.execute("SELECT 1")  # Simple query to check if the database is reachable
        conn.close()
        
        # If we reach this point, the server and database are operational
        return jsonify({"status": "healthy"}), 200

    except sqlite3.Error as e:
        # Log the error internally (not shown here), and return an error response
        return jsonify({"error": {"code": "E001", "message": "Database connection error", "details": str(e)}}), 500

if __name__ == '__main__':
    app.run(debug=True)