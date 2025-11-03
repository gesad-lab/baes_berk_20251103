'''
Graphical User Interface for the application using Tkinter.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
    import requests
except ImportError:
    print("Tkinter is not installed. Please install it to run the GUI.")
    exit(1)
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
        self.students_list = tk.Listbox(master)
        self.students_list.pack()
    def add_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
                self.entry_name.delete(0, tk.END)
                self.entry_email.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def show_students(self):
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']}")  # Show email
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()