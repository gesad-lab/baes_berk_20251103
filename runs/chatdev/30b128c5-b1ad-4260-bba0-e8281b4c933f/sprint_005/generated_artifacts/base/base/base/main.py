'''
Implements a simple GUI for interacting with the FastAPI application.
'''
try:
    import tkinter as tk
    import requests
    import re  # Importing regex for email validation
    class StudentApp:
        def __init__(self, root):
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
            self.output_text = tk.Text(root)
            self.output_text.pack()
        def add_student(self):
            name = self.name_entry.get()
            email = self.email_entry.get()  # Get email input
            # Validate email format (using regex for better validation)
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.output_text.insert(tk.END, "Invalid email format\n")
                return
            response = requests.post("http://127.0.0.1:8000/students", json={"name": name, "email": email})
            if response.status_code == 200:
                self.output_text.insert(tk.END, f"Added: {name}, Email: {email}\n")
            else:
                self.output_text.insert(tk.END, "Failed to add student\n")
        def fetch_students(self):
            response = requests.get("http://127.0.0.1:8000/students")
            if response.status_code == 200:
                students = response.json()
                self.output_text.delete(1.0, tk.END)
                for student in students:
                    self.output_text.insert(tk.END, f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")  # Display email
            else:
                self.output_text.insert(tk.END, "Failed to fetch students\n")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("tkinter is not installed. Please install it to run the GUI application.")