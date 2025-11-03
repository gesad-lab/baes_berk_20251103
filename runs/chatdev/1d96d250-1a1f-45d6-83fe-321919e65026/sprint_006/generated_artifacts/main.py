'''
Main entry point for the Student application.
'''
import tkinter as tk
from tkinter import messagebox
import requests
# Check if tkinter is available
try:
    import tkinter
except ImportError:
    raise ImportError("The tkinter module is not available. Please install it to run the application.")
class StudentApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management")
        # Student Entry
        self.label_name = tk.Label(self.root, text="Enter Student Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()
        self.label_email = tk.Label(self.root, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack()
        # Course Entry
        self.label_course_name = tk.Label(self.root, text="Enter Course Name:")
        self.label_course_name.pack()
        self.entry_course_name = tk.Entry(self.root)
        self.entry_course_name.pack()
        self.label_course_level = tk.Label(self.root, text="Enter Course Level:")
        self.label_course_level.pack()
        self.entry_course_level = tk.Entry(self.root)
        self.entry_course_level.pack()
        # Teacher Entry
        self.label_teacher_name = tk.Label(self.root, text="Enter Teacher Name:")
        self.label_teacher_name.pack()
        self.entry_teacher_name = tk.Entry(self.root)
        self.entry_teacher_name.pack()
        self.label_teacher_email = tk.Label(self.root, text="Enter Teacher Email:")
        self.label_teacher_email.pack()
        self.entry_teacher_email = tk.Entry(self.root)
        self.entry_teacher_email.pack()
        # Add buttons
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.add_course_button = tk.Button(self.root, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        self.add_teacher_button = tk.Button(self.root, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.root.mainloop()
    def add_student(self):
        '''
        Add a student by sending a POST request to the FastAPI application.
        '''
        name = self.entry_name.get()
        email = self.entry_email.get()
        if name and email:
            try:
                response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
                if response.status_code == 201:  # Check for 201 Created
                    messagebox.showinfo("Success", "Student added successfully!")
                    self.entry_name.delete(0, tk.END)
                    self.entry_email.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Failed to add student.")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter both name and email.")
    def add_teacher(self):
        '''
        Add a teacher by sending a POST request to the FastAPI application.
        If the teacher already exists, return the existing teacher's ID.
        '''
        name = self.entry_teacher_name.get()
        email = self.entry_teacher_email.get()
        if name and email:
            try:
                # Check if the teacher already exists
                response = requests.get(f"http://127.0.0.1:8000/teachers/?name={name}&email={email}")
                if response.status_code == 200:
                    existing_teachers = response.json()
                    if existing_teachers:
                        return existing_teachers[0]['id']  # Return existing teacher's ID
                    else:
                        # Teacher does not exist, create a new one
                        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
                        if response.status_code == 201:  # Check for 201 Created
                            return response.json().get("id")  # Return new teacher's ID
                        else:
                            messagebox.showerror("Error", "Failed to add teacher.")
                            return None
                else:
                    messagebox.showerror("Error", "Failed to check for existing teacher.")
                    return None
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                return None
        else:
            messagebox.showwarning("Warning", "Please enter both name and email.")
            return None
    def add_course(self):
        '''
        Add a course by sending a POST request to the FastAPI application.
        '''
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        teacher_id = self.add_teacher()  # Get teacher ID from add_teacher method
        if name and level and teacher_id:
            try:
                # Now add the course with the teacher_id
                course_response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level, "teacher_id": teacher_id})
                if course_response.status_code == 201:  # Check for 201 Created
                    messagebox.showinfo("Success", "Course added successfully!")
                    self.entry_course_name.delete(0, tk.END)
                    self.entry_course_level.delete(0, tk.END)
                    self.entry_teacher_name.delete(0, tk.END)
                    self.entry_teacher_email.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Failed to add course.")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter all fields for course and teacher.")
if __name__ == "__main__":
    StudentApp()