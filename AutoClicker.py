import tkinter as tk
import pyautogui
import time

def auto_clicker():
    try:
        rate = int(click_rate_entry.get())
    except ValueError:
        status_label.config(text="Invalid Input. Please enter a number.")
        return

    if rate <= 0:
        status_label.config(text="Invalid Input. Please enter a positive number.")
        return

    start_button.config(state=tk.DISABLED)

    def stop_auto_clicker():
        global running
        running = False
        start_button.config(state=tk.NORMAL)
        status_label.config(text="Stopped.")

    root.protocol("WM_DELETE_WINDOW", stop_auto_clicker)

    running = True
    status_label.config(text="Running.")

    while running:
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(1 / rate)

    start_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Auto Clicker by NoahPrm")

start_button = tk.Button(root, text="Start", command=auto_clicker)
start_button.pack(pady=10)

click_rate_label = tk.Label(root, text="Click Rate (Times per Second):")
click_rate_label.pack()

click_rate_entry = tk.Entry(root)
click_rate_entry.pack()

status_label = tk.Label(root, text="Ready.")
status_label.pack(pady=5)

root.mainloop()
