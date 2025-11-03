'''
Implements the GUI using Tkinter for user interaction.
'''
import tkinter as tk
import requests
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the application.")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label_name = tk.Label(master, text="Enter Student Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.show_button = tk.Button(master, text="Show Students", command=self.show_students)
        self.show_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Added email to request
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Failed to add student.\n")
    def show_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")  # Added email to output
        else:
            self.output.insert(tk.END, "Failed to retrieve students.\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()