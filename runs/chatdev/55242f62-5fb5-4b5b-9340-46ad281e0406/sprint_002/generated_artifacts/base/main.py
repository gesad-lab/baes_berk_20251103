'''
Simple GUI for interacting with the FastAPI application.
'''
import tkinter as tk
import requests
def create_gui():
    def submit_student():
        name = entry_name.get()
        try:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
            if response.status_code == 200:
                print("Student created:", response.json())
            else:
                print("Error:", response.text)
        except requests.exceptions.RequestException as e:
            print("HTTP Request failed:", e)
    root = tk.Tk()
    root.title("Student Registration")
    label_name = tk.Label(root, text="Student Name:")
    label_name.pack()
    entry_name = tk.Entry(root)
    entry_name.pack()
    button_submit = tk.Button(root, text="Submit", command=submit_student)
    button_submit.pack()
    try:
        root.mainloop()
    except Exception as e:
        print("Failed to start GUI. Make sure Tkinter is installed. Error:", e)
if __name__ == "__main__":
    create_gui()