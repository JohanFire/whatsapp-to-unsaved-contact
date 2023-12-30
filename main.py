import tkinter
from tkinter import ttk
# from tkinter import messagebox
# from typing import Tuple
from icecream import ic

from utils.App import App
from utils.screen import render_center_of_screen

def main():
    root = tkinter.Tk()

    root.title("WhatsApp to Unsaved Contact")
    width, height, x, y = render_center_of_screen(root, width=800, height=360)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(width=False, height=False)
    root.configure(bg='#333333')

    app = App(root)

    root.mainloop()

if __name__ == '__main__':
    main()