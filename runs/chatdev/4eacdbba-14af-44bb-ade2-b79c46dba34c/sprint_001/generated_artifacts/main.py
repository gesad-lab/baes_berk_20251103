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
            self.label = tk.Label(root, text="Enter Student Name:")
            self.label.pack()
            self.entry = tk.Entry(root)
            self.entry.pack()
            self.submit_button = tk.Button(root, text="Submit", command=self.submit_student)
            self.submit_button.pack()
            self.get_button = tk.Button(root, text="Get Students", command=self.get_students)
            self.get_button.pack()
            self.output = tk.Text(root, height=10, width=50)
            self.output.pack()
        def submit_student(self):
            name = self.entry.get()
            if name:
                response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Student added successfully!")
                else:
                    messagebox.showerror("Error", "Failed to add student.")
            else:
                messagebox.showwarning("Input Error", "Please enter a name.")
        def get_students(self):
            response = requests.get("http://127.0.0.1:8000/students/")
            if response.status_code == 200:
                students = response.json()
                self.output.delete(1.0, tk.END)
                for student in students:
                    self.output.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}\n")
            else:
                messagebox.showerror("Error", "Failed to retrieve students.")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("Tkinter module is not available. Please install Tkinter to use the GUI.")