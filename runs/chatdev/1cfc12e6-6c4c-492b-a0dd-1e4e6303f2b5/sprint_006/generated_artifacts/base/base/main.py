'''
Graphical User Interface for the Student Management Application.
'''
import tkinter as tk
import requests
from api import create_student, create_course, get_students, get_courses, enroll_student_in_course
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    raise ImportError("tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.label_course = tk.Label(master, text="Enter Course ID to Enroll:")
        self.label_course.pack()
        self.entry_course = tk.Entry(master)
        self.entry_course.pack()
        self.enroll_button = tk.Button(master, text="Enroll in Course", command=self.enroll_student)
        self.enroll_button.pack()
        self.view_button = tk.Button(master, text="View Students", command=self.view_students)
        self.view_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        '''
        Add a student by sending a POST request to the API.
        '''
        name = self.entry.get()
        email = self.entry_email.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {name}, Email: {email}\n")
        else:
            self.output.insert(tk.END, "Failed to add student.\n")
    def enroll_student(self):
        '''
        Enroll a student in a course by sending a POST request to the API.
        '''
        student_id = self.entry.get()  # Assuming student ID is entered in the name field
        course_id = self.entry_course.get()
        response = requests.post(f"http://127.0.0.1:8000/enroll/{student_id}/{course_id}")
        if response.status_code == 200:
            result = response.json()
            if "message" in result:
                self.output.insert(tk.END, result["message"] + "\n")
            else:
                self.output.insert(tk.END, f"Enrolled Student ID: {student_id} in Course ID: {course_id}\n")
        else:
            self.output.insert(tk.END, "Failed to enroll student.\n")
    def view_students(self):
        '''
        Retrieve and display all students by sending a GET request to the API.
        '''
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")
        else:
            self.output.insert(tk.END, "Failed to retrieve students.\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()