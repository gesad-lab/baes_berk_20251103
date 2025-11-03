'''
Graphical User Interface for the Student application using Tkinter.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
    import requests
    class StudentApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Student Management")
            self.label_name = tk.Label(root, text="Enter Student Name:")
            self.label_name.pack()
            self.entry_name = tk.Entry(root)
            self.entry_name.pack()
            self.label_email = tk.Label(root, text="Enter Student Email:")
            self.label_email.pack()
            self.entry_email = tk.Entry(root)
            self.entry_email.pack()
            self.submit_button = tk.Button(root, text="Submit", command=self.submit_student)
            self.submit_button.pack()
            self.get_button = tk.Button(root, text="Get Students", command=self.get_students)
            self.get_button.pack()
            self.output = tk.Text(root, height=10, width=50)
            self.output.pack()
        def submit_student(self):
            name = self.entry_name.get()
            email = self.entry_email.get()
            if name and email:
                response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Student added successfully!")
                else:
                    messagebox.showerror("Error", "Failed to add student.")
            else:
                messagebox.showwarning("Input Error", "Please enter both name and email.")
        def get_students(self):
            response = requests.get("http://127.0.0.1:8000/students/")
            if response.status_code == 200:
                students = response.json()
                self.output.delete(1.0, tk.END)
                for student in students:
                    self.output.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")
            else:
                messagebox.showerror("Error", "Failed to retrieve students.")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("Tkinter module is not available. Please install Tkinter to use the GUI.")