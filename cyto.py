import tkinter as tk

# ------------------ UI CONSTANTS ------------------
WINDOW_WIDTH = 375
WINDOW_HEIGHT = 667

BG_DARK = "#1E1E1E"
BG_LIGHT = "#F2F2F2"
GREEN = "#2ECC71"
RED = "#E74C3C"
WHITE = "#FFFFFF"

TITLE_FONT = ("Calibri", 22, "bold")
COUNT_FONT = ("Calibri", 40, "bold")
BUTTON_FONT = ("Calibri", 18, "bold")


class HemocytometerCounter:
    def __init__(self):
        self.count = 0

        self.window = tk.Tk()
        self.window.title("Hemocytometer Counter")
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.window.resizable(False, False)
        self.window.configure(bg=BG_LIGHT)

        self.create_header()
        self.create_display()
        self.create_buttons()

    # ------------------ HEADER ------------------
    def create_header(self):
        header = tk.Frame(self.window, bg=BG_DARK, height=80)
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Hemocytometer Counter",
            fg=WHITE,
            bg=BG_DARK,
            font=TITLE_FONT
        )
        title.pack(expand=True)

    # ------------------ DISPLAY ------------------
    def create_display(self):
        display_frame = tk.Frame(self.window, bg=BG_LIGHT)
        display_frame.pack(expand=True, fill="both")

        self.count_label = tk.Label(
            display_frame,
            text=f"Cell Count: {self.count}",
            font=COUNT_FONT,
            fg="#000000",
            bg=BG_LIGHT
        )
        self.count_label.pack(expand=True)

    # ------------------ BUTTONS ------------------
    def create_buttons(self):
        button_frame = tk.Frame(self.window, bg=BG_LIGHT)
        button_frame.pack(fill="x", pady=20)

        count_button = tk.Button(
            button_frame,
            text="+  Count Cell",
            font=BUTTON_FONT,
            bg=GREEN,
            fg=WHITE,
            height=2,
            command=self.increment_count
        )
        count_button.pack(fill="x", padx=30, pady=10)

        reset_button = tk.Button(
            button_frame,
            text="⟳  Reset Counter",
            font=BUTTON_FONT,
            bg=RED,
            fg=WHITE,
            height=2,
            command=self.reset_count
        )
        reset_button.pack(fill="x", padx=30)

    # ------------------ LOGIC ------------------
    def increment_count(self):
        self.count += 1
        self.update_display()

    def reset_count(self):
        self.count = 0
        self.update_display()

    def update_display(self):
        self.count_label.config(text=f"Cell Count: {self.count}")

    def run(self):
        self.window.mainloop()


# ------------------ RUN APP ------------------
if __name__ == "__main__":
    app = HemocytometerCounter()
    app.run()
