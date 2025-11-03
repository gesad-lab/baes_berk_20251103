'''
Implements the GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.students_button = tk.Button(root, text="Show Students", command=self.show_students)
        self.students_button.pack()
        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()
    def add_student(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        if not name.strip() or not email.strip():
            self.output.insert(tk.END, "Name and Email cannot be empty\n")
            return
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Failed to add student\n")
    def show_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)  # Clear previous output
            for student in students:
                self.output.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")  # Include email
        else:
            self.output.insert(tk.END, "Failed to retrieve students\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()