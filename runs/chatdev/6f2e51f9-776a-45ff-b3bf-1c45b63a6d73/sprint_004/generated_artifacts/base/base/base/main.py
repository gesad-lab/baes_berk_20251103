'''
Graphical User Interface for the Student application.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
    import requests
except ImportError:
    print("Tkinter is not available. Please install it to run the GUI.")
    exit()
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Application")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.list_button = tk.Button(master, text="List Students", command=self.list_students)
        self.list_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
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
    def list_students(self):
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