'''
Implements the GUI for user interaction using Tkinter.
'''
try:
    import tkinter as tk
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
import requests
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
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def submit(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Student created: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error: {response.text}\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()