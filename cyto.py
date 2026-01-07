import tkinter as tk


class CytoApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x200")
        self.window.resizable(0, 0)
        self.window.title("Cyto Application")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    cyto = CytoApp()
    cyto.run()
