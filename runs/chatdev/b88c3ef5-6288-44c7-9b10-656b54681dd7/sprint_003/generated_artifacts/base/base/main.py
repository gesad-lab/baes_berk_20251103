'''
Implements a simple GUI using Tkinter to interact with the API.
'''
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not available. Please install it to use the GUI.")
    exit(1)
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
        self.response_label = tk.Label(root, text="")
        self.response_label.pack()
    def submit_student(self):
        name = self.entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        if response.status_code == 200:
            self.response_label.config(text=f"Student created: {response.json()}")
        else:
            self.response_label.config(text="Error creating student")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()