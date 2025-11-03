'''
A simple GUI using Tkinter to interact with the API.
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
        self.label_email = tk.Label(master, text="Enter Student Email:")  # Added email label
        self.label_email.pack()
        self.entry_email = tk.Entry(master)  # Added email entry
        self.entry_email.pack()
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def submit(self):
        name = self.entry.get()
        email = self.entry_email.get()  # Get email input
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Updated to include email
        if response.status_code == 200:
            self.result_label.config(text=f"Student {name} added successfully!")
        else:
            self.result_label.config(text="Error adding student.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()