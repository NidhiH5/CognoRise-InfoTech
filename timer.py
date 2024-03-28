import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        self.label = tk.Label(master, text="Enter time in seconds:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        self.time_remaining = 0
        self.running = False

    def start_timer(self):
        try:
            self.time_remaining = int(self.entry.get())
            if self.time_remaining <= 0:
                raise ValueError
            self.running = True
            self.update_timer()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer.")

    def stop_timer(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.running:
            self.label.config(text=f"Time Remaining: {self.time_remaining}")
            if self.time_remaining == 0:
                messagebox.showinfo("Countdown Timer", "Time's up!")
                self.stop_timer()
            else:
                self.time_remaining -= 1
                self.master.after(1000, self.update_timer)

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
