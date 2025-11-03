'''
Graphical User Interface for the Student application.
'''
try:
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
            self.label_email = tk.Label(master, text="Enter Student Email:")  # New label for email
            self.label_email.pack()
            self.entry_email = tk.Entry(master)  # New entry for email
            self.entry_email.pack()
            self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
            self.add_button.pack()
            self.view_button = tk.Button(master, text="View Students", command=self.view_students)
            self.view_button.pack()
            self.output = tk.Text(master)
            self.output.pack()
        def add_student(self):
            '''
            Add a student by sending a POST request to the API.
            '''
            name = self.entry.get()
            email = self.entry_email.get()  # Get email from entry
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Include email in request
            if response.status_code == 200:
                self.output.insert(tk.END, f"Added Student: {name}, Email: {email}\n")
            else:
                self.output.insert(tk.END, "Failed to add student.\n")
        def view_students(self):
            '''
            Retrieve and display all students by sending a GET request to the API.
            '''
            response = requests.get("http://127.0.0.1:8000/students/")
            if response.status_code == 200:
                students = response.json()
                self.output.delete(1.0, tk.END)
                for student in students:
                    self.output.insert(tk.END, f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")  # Display email
            else:
                self.output.insert(tk.END, "Failed to retrieve students.\n")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("tkinter is not installed. Please install it to run the GUI application.")