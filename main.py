import tkinter
# from tkinter import messagebox
# from typing import Tuple
from icecream import ic

from utils.screen import render_center_of_screen

def main():
    app = tkinter.Tk()

    app.title("WhatsApp to Unsaved Contact")
    width, height, x, y = render_center_of_screen(app, width=800, height=640)
    app.geometry(f"{width}x{height}+{x}+{y}")
    app.resizable(width=False, height=False)
    app.configure(bg='#333333')

    frame = tkinter.Frame(bg='#333333')

    """ Widgets """
    login_label  = tkinter.Label(
        frame, text='Login', bg='#333333', fg='#FF3399', font=("Arial", 30) )
    username_label = tkinter.Label(
        frame, text='Username', bg='#333333', fg='#FFFFFF', font=("Arial", 16) )
    username_entry = tkinter.Entry(frame, font=("Arial", 16) )
    password_label = tkinter.Label(
        frame, text='Password', bg='#333333', fg='#FFFFFF', font=("Arial", 16) )
    password_entry = tkinter.Entry(frame, show='*', font=("Arial", 16) )
    login_button = tkinter.Button(
        frame, text='Login', bg='#FF3399', fg='#FFFFFF', font=("Arial", 16) )

    """ Placing widgets on screen """
    login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    frame.pack()



    app.mainloop()

if __name__ == '__main__':
    main()