'''
Simple GUI for adding students using Tkinter.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
    import requests
    class StudentApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Student Registration")
            self.label = tk.Label(root, text="Enter Student Name:")
            self.label.pack()
            self.entry = tk.Entry(root)
            self.entry.pack()
            self.submit_button = tk.Button(root, text="Add Student", command=self.add_student)
            self.submit_button.pack()
        def add_student(self):
            name = self.entry.get()
            if name:
                response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Student added successfully!")
                    self.entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Failed to add student.")
            else:
                messagebox.showwarning("Warning", "Please enter a name.")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("Tkinter is not available. Please install it to run the GUI application.")