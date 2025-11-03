'''
Implements the graphical user interface using Tkinter.
'''
import tkinter as tk
import requests
# Note: Ensure that Tkinter is installed in your Python environment.
# You can install it using the following command:
# For Ubuntu/Debian: sudo apt-get install python3-tk
# For Windows: Tkinter comes pre-installed with Python. If not, reinstall Python.
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it to run the application.")
    exit()
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")  # Add this line
        self.email_label.pack()  # Add this line
        self.email_entry = tk.Entry(root)  # Add this line
        self.email_entry.pack()  # Add this line
        self.submit_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.submit_button.pack()
        self.students_button = tk.Button(root, text="Show Students", command=self.show_students)
        self.students_button.pack()
        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()
    def add_student(self):
        name = self.name_entry.get()
        email = self.email_entry.get()  # Add this line
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Update this line
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Error adding student\n")
    def show_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")  # Update this line
        else:
            self.output.insert(tk.END, "Error fetching students\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()