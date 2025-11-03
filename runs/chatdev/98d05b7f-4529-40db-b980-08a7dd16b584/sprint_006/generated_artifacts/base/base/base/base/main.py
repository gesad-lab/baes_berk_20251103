'''
Tkinter GUI for interacting with the FastAPI application.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, root):
        '''
        Initialize the Tkinter GUI components.
        '''
        self.root = root
        self.root.title("Student Management")
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")  # Added email label
        self.email_label.pack()
        self.email_entry = tk.Entry(root)  # Added email entry
        self.email_entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.fetch_button = tk.Button(root, text="Fetch Students", command=self.fetch_students)
        self.fetch_button.pack()
        self.students_list = tk.Listbox(root)
        self.students_list.pack()
    def add_student(self):
        '''
        Add a new student by sending a POST request to the FastAPI application.
        '''
        name = self.name_entry.get()
        email = self.email_entry.get()  # Get email from the entry
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)  # Clear email entry
            self.fetch_students()
    def fetch_students(self):
        '''
        Fetch the list of students by sending a GET request to the FastAPI application.
        '''
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, f"{student['name']} - {student['email']}")  # Display email as well
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()