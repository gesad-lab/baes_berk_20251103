'''
Implements a simple GUI using Tkinter to interact with the API.
'''
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it using your package manager.")
    print("For example, on Ubuntu, you can run: sudo apt-get install python3-tk")
    exit(1)
import requests
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.label = tk.Label(root, text="Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")  # Added email label
        self.email_label.pack()  # Added email label
        self.email_entry = tk.Entry(root)  # Added email entry
        self.email_entry.pack()  # Added email entry
        self.submit_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.submit_button.pack()
        self.output = tk.Text(root, height=10, width=30)
        self.output.pack()
    def add_student(self):
        '''
        Sends a request to add a new student to the API.
        '''
        name = self.entry.get()
        email = self.email_entry.get()  # Get email input
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Send email in request
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()['name']} with Email: {response.json()['email']}\n")
        else:
            self.output.insert(tk.END, "Failed to add student.\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()