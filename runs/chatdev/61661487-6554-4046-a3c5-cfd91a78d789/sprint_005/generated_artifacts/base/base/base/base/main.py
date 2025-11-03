'''
Graphical User Interface for the application using Tkinter.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
    import requests
    class StudentApp:
        def __init__(self, master):
            self.master = master
            master.title("Student Management")
            self.label = tk.Label(master, text="Enter Student Name:")
            self.label.pack()
            self.entry = tk.Entry(master)
            self.entry.pack()
            self.submit_button = tk.Button(master, text="Add Student", command=self.add_student)
            self.submit_button.pack()
            self.view_button = tk.Button(master, text="View Students", command=self.view_students)
            self.view_button.pack()
        def add_student(self):
            name = self.entry.get()
            if name:
                response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Student added successfully!")
                else:
                    messagebox.showerror("Error", "Failed to add student.")
            else:
                messagebox.showwarning("Warning", "Name cannot be empty.")
        def view_students(self):
            response = requests.get("http://127.0.0.1:8000/students/")
            if response.status_code == 200:
                students = response.json()
                students_list = "\n".join([f"{student['id']}: {student['name']}" for student in students])
                messagebox.showinfo("Students", students_list)
            else:
                messagebox.showerror("Error", "Failed to retrieve students.")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("Error: Tkinter is not installed. Please install it to run the GUI application.")