import tkinter as tk

# ------------------ UI CONSTANTS ------------------
WINDOW_WIDTH = 375
WINDOW_HEIGHT = 667

BG_DARK = "#1E1E1E"
BG_LIGHT = "#F2F2F2"
GREEN = "#0B4523"
RED = "#991A0B"
WHITE = "#FFFFFF"

TITLE_FONT = ("Calibri", 22, "bold")
COUNT_FONT = ("Calibri", 40, "bold")
BUTTON_FONT = ("Calibri", 18, "bold")


class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, radius, bg, fg, text, command):
        super().__init__(
            parent,
            width=width,
            height=height,
            bg=parent["bg"],
            highlightthickness=0
        )
        self.command = command

        self.create_rounded_rect(0, 0, width, height, radius, fill=bg)
        self.text_id = self.create_text(
            width // 2,
            height // 2,
            text=text,
            fill=fg,
            font=BUTTON_FONT
        )

        self.bind("<Button-1>", lambda e: self.command())
        self.bind("<Enter>", lambda e: self.itemconfig(
            self.text_id, fill="#EAEAEA"))
        self.bind("<Leave>", lambda e: self.itemconfig(self.text_id, fill=fg))

    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1 + r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1
        ]
        self.create_polygon(points, smooth=True, **kwargs)


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
        button_frame.pack(pady=30)

        count_btn = RoundedButton(
            button_frame,
            width=300,
            height=60,
            radius=25,
            bg=GREEN,
            fg=WHITE,
            text="+  Count Cell",
            command=self.increment_count
        )
        count_btn.pack(pady=12)

        reset_btn = RoundedButton(
            button_frame,
            width=300,
            height=60,
            radius=25,
            bg=RED,
            fg=WHITE,
            text="⟳  Reset Counter",
            command=self.reset_count
        )
        reset_btn.pack()

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
