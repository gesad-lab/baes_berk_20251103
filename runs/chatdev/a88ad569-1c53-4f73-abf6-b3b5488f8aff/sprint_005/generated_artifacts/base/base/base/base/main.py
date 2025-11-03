'''
Simple GUI for interacting with the FastAPI backend.
'''
try:
    import tkinter as tk
    import requests
    class StudentApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Student Management")
            self.label = tk.Label(root, text="Enter Student Name:")
            self.label.pack()
            self.entry = tk.Entry(root)
            self.entry.pack()
            self.submit_button = tk.Button(root, text="Add Student", command=self.add_student)
            self.submit_button.pack()
            self.response_label = tk.Label(root, text="")
            self.response_label.pack()
        def add_student(self):
            name = self.entry.get()
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
            if response.status_code == 200:
                self.response_label.config(text=f"Student added: {response.json()['name']}")
            else:
                self.response_label.config(text="Error adding student")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("tkinter module is not available. Please install it to run the GUI.")