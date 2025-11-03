'''
Implements the GUI using Tkinter to interact with the API.
'''
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it to run the GUI.")
    exit(1)
import requests
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")
        self.email_label.pack()  # Added email label
        self.email_entry = tk.Entry(root)  # Added email entry
        self.email_entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.students_list = tk.Listbox(root)
        self.students_list.pack()
        self.load_students()
    def add_student(self):
        name = self.name_entry.get()
        email = self.email_entry.get()  # Get email
        if name and email:  # Check both name and email
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Include email in request
            if response.status_code == 200:
                self.load_students()
                self.name_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)  # Clear email entry
    def load_students(self):
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, f"{student['id']}: {student['name']} ({student['email']})")  # Display email
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()