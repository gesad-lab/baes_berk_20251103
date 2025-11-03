'''
Implements the GUI using Tkinter for user interaction.
'''
try:
    import tkinter as tk
    import requests  # Added import for requests
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
# Check if Tkinter is installed and provide instructions if not
try:
    import tkinter
except ImportError:
    print("Tkinter is not installed. Please install it using 'pip install tk'.")
    exit()  # Added exit to stop execution if Tkinter is not installed
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")  # Added email label
        self.label_email.pack()
        self.entry_email = tk.Entry(master)  # Added email entry
        self.entry_email.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()  # Get email input
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Updated to send email
        if response.status_code == 200:
            self.result_label.config(text=f"Student added: {response.json()['name']} with email: {response.json()['email']}")
        else:
            self.result_label.config(text="Error adding student")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()