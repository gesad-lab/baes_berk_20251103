'''
Implements the GUI using Tkinter for user interaction.
'''
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it to run the GUI.")
    exit()
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")  # New label for email
        self.label_email.pack()
        self.entry_email = tk.Entry(master)  # New entry for email
        self.entry_email.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()  # Get email from entry
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Send email in request
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error: {response.text}\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()