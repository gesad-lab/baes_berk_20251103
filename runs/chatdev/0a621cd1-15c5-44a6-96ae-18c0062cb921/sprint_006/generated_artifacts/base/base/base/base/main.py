'''
Implements the GUI using Tkinter for user interaction.
'''
import tkinter as tk
import requests
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    print("Error: Tkinter is not installed. Please install it to run the GUI.")
    exit(1)
# Ensure tkinter is properly imported
if not 'tkinter' in locals():
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")  # Add this line
        self.label_email.pack()  # Add this line
        self.entry_email = tk.Entry(master)  # Add this line
        self.entry_email.pack()  # Add this line
        self.submit_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.submit_button.pack()
        self.view_button = tk.Button(master, text="View Students", command=self.view_students)
        self.view_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()  # Add this line
        if not name.strip() or not email.strip():  # Check for empty name or email
            self.output.insert(tk.END, "Error: Name and Email cannot be empty.\n")
            return
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Update this line
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Error adding student.\n")
    def view_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)  # Clear previous output
            for student in students:
                self.output.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")  # Update this line
        else:
            self.output.insert(tk.END, "Error retrieving students.\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()