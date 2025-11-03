'''
Graphical User Interface for the Student application using Tkinter.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
    import requests
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run this application.")
class StudentApp:
    def __init__(self, root):
        '''
        Initialize the GUI components.
        '''
        self.root = root
        self.root.title("Student Management")
        self.label = tk.Label(root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
    def add_student(self):
        '''
        Add a student by sending a request to the FastAPI backend.
        '''
        name = self.entry.get()
        if name:
            try:
                response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Student added successfully!")
                    self.entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Failed to add student.")
            except requests.exceptions.RequestException:
                messagebox.showerror("Error", "Server is not running.")
        else:
            messagebox.showwarning("Warning", "Please enter a name.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()