'''
Implements the GUI using Tkinter.
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
        self.submit_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.submit_button.pack()
        self.students_button = tk.Button(master, text="View Students", command=self.view_students)
        self.students_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Error adding student.\n")
    def view_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"Student ID: {student['id']}, Name: {student['name']}\n")
        else:
            self.output.insert(tk.END, "Error retrieving students.\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()