'''
Simple GUI to interact with the FastAPI backend.
'''
import tkinter as tk
import requests
class StudentApp:
    '''GUI application for managing students.'''
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.view_button = tk.Button(master, text="View Students", command=self.view_students)
        self.view_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        self.students_label = tk.Label(master, text="")
        self.students_label.pack()
    def submit(self):
        '''Submit a new student name to the backend.'''
        name = self.entry.get()
        try:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
            response.raise_for_status()  # Raise an error for bad responses
            self.result_label.config(text=f"Student {name} added successfully!")
        except requests.exceptions.RequestException as e:
            self.result_label.config(text="Error adding student.")
    def view_students(self):
        '''Retrieve and display the list of students from the backend.'''
        try:
            response = requests.get("http://127.0.0.1:8000/students/")
            response.raise_for_status()
            students = response.json()
            student_names = "\n".join([f"{student['id']}: {student['name']}" for student in students])
            self.students_label.config(text=f"Students:\n{student_names}")
        except requests.exceptions.RequestException as e:
            self.students_label.config(text="Error retrieving students.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()