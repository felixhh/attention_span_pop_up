import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox

def show_reminder(seconds):
    while True:
        time.sleep(seconds)
        # Show a red pop-up reminder
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        root.title("Focus Reminder")
        root.geometry("300x100")
        root.configure(bg='red')

        reminder_label = ttk.Label(root, text=f"Time to focus for {seconds} seconds!\nClose this window to reset the timer.", background='red', font=('Arial', 12))
        reminder_label.pack(padx=20, pady=20)

        result = messagebox.showinfo("Reminder", f"Time to focus for {seconds} seconds!\nClose this window to reset the timer.")
        root.destroy()

        # When the reminder window is closed, reset the timer
        if result == "ok":
            continue

def set_reminder():
    seconds = int(reminder_entry.get())
    if seconds > 0:
        show_reminder(seconds)
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid reminder time in seconds.")

app = tk.Tk()
app.title("Focus Reminder")

frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=10, pady=10)

reminder_label = ttk.Label(frame, text="Enter reminder time (seconds):")
reminder_label.grid(column=0, row=0)

reminder_entry = ttk.Entry(frame)
reminder_entry.grid(column=1, row=0)

reminder_button = ttk.Button(frame, text="Set Reminder", command=set_reminder)
reminder_button.grid(column=2, row=0)

app.mainloop()