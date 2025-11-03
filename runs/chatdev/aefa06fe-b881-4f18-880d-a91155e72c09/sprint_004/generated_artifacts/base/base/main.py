'''
Implements a simple GUI using Tkinter for user interaction.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student App")
        self.label = tk.Label(root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.label_email = tk.Label(root, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_student)
        self.submit_button.pack()
        self.response_label = tk.Label(root, text="")
        self.response_label.pack()
    def submit_student(self):
        """Submit the student data to the API."""
        name = self.entry.get()
        email = self.entry_email.get()  # Get email input
        try:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
            response.raise_for_status()  # Raise an error for bad responses
            self.response_label.config(text=f"Student created: {response.json()['name']}")
        except requests.exceptions.RequestException as e:
            self.response_label.config(text=f"Error creating student: {str(e)}")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()