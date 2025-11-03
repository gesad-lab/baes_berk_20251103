'''
Defines the GUI for the Student Management application.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.email_label = tk.Label(master, text="Enter Student Email:")  # Add email label
        self.email_label.pack()
        self.email_entry = tk.Entry(master)  # Add email entry
        self.email_entry.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.display_button = tk.Button(master, text="Display Students", command=self.display_students)
        self.display_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.email_entry.get()  # Get the email
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Update this line
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added: {name} with Email: {email}\n")
        else:
            self.output.insert(tk.END, "Error adding student\n")
    def display_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']}\n")  # Display email
        else:
            self.output.insert(tk.END, "Error retrieving students\n")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
    except ImportError as e:
        print("Error: tkinter module is not installed. Please install it to run the application.")