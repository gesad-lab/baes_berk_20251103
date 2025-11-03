'''
Implements a simple GUI for interacting with the FastAPI application.
'''
try:
    import tkinter as tk
    import requests
    class StudentApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Student Management")
            self.name_label = tk.Label(root, text="Student Name:")
            self.name_label.pack()
            self.name_entry = tk.Entry(root)
            self.name_entry.pack()
            self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
            self.add_button.pack()
            self.fetch_button = tk.Button(root, text="Fetch Students", command=self.fetch_students)
            self.fetch_button.pack()
            self.output_text = tk.Text(root)
            self.output_text.pack()
        def add_student(self):
            name = self.name_entry.get()
            response = requests.post("http://127.0.0.1:8000/students", json={"name": name})
            if response.status_code == 200:
                self.output_text.insert(tk.END, f"Added: {name}\n")
            else:
                self.output_text.insert(tk.END, "Failed to add student\n")
        def fetch_students(self):
            response = requests.get("http://127.0.0.1:8000/students")
            if response.status_code == 200:
                students = response.json()
                self.output_text.delete(1.0, tk.END)
                for student in students:
                    self.output_text.insert(tk.END, f"Student ID: {student['id']}, Name: {student['name']}\n")
            else:
                self.output_text.insert(tk.END, "Failed to fetch students\n")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("tkinter is not installed. Please install it to run the GUI application.")