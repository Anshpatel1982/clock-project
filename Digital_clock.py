import tkinter as tk
from tkinter import colorchooser
from datetime import datetime

class AdvancedClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Digital Clock")
        self.configure(padx=30, pady=30, bg="#000000")

        # Create label for displaying time, date, and day
        self.time_label = tk.Label(self, font=("Arial", 70, "bold"), fg="white", bg="#000000")
        self.time_label.pack(pady=20)

        # Function to update time and display it on the label
        self.update_time()

        # Start the timer to update time every second
        self.after(1000, self.update_time)

        # Create frame for customization options
        self.customize_frame = tk.Frame(self, bg="#000000")
        self.customize_frame.pack(pady=20)

        # Font size label
        self.font_size_label = tk.Label(self.customize_frame, text="Font Size:", fg="white", bg="#000000")
        self.font_size_label.pack(side=tk.LEFT)

        # Font size entry box
        self.font_size_entry = tk.Entry(self.customize_frame, width=5, justify=tk.CENTER)
        self.font_size_entry.insert(tk.END, "70")  # Default font size
        self.font_size_entry.bind("<Return>", self.update_font_size)
        self.font_size_entry.pack(side=tk.LEFT, padx=5)

        # Color picker for text and background
        self.text_color_label = tk.Label(self.customize_frame, text="Text Color:", fg="white", bg="#000000")
        self.text_color_label.pack(side=tk.LEFT, padx=10)
        self.text_color_button = tk.Button(self.customize_frame, text="Choose", command=self.choose_text_color)
        self.text_color_button.pack(side=tk.LEFT)

        self.background_color_label = tk.Label(self.customize_frame, text="Background:", fg="white", bg="#000000")
        self.background_color_label.pack(side=tk.LEFT, padx=10)
        self.background_color_button = tk.Button(self.customize_frame, text="Choose", command=self.choose_background_color)
        self.background_color_button.pack(side=tk.LEFT)

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S\n%A, %d %B %Y")
        self.time_label.config(text=current_time)
        self.after(1000, self.update_time)  # Update every second

    def update_font_size(self, event):
        try:
            new_font_size = int(self.font_size_entry.get())
            self.time_label.config(font=("Arial", new_font_size, "bold"))
        except ValueError:
            pass  # Ignore invalid font size input

    def choose_text_color(self):
        color = tk.colorchooser.askcolor(title="Choose Text Color")[1]
        if color:
            self.time_label.config(fg=color)

    def choose_background_color(self):
        color = tk.colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            self.config(bg=color)
            self.customize_frame.config(bg=color)

if __name__ == "__main__":
    clock = AdvancedClock()
    clock.mainloop()
