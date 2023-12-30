import tkinter
# from tkinter import messagebox
# from typing import Tuple
from icecream import ic

from utils.screen import render_center_of_screen

def main():
    app = tkinter.Tk()

    app.title("WhatsApp to Unsaved Contact")
    width, height, x, y = render_center_of_screen(app, width=800, height=340)
    app.geometry(f"{width}x{height}+{x}+{y}")
    app.resizable(width=False, height=False)
    app.configure(bg='#333333')

    frame = tkinter.Frame(bg='#333333')

    """ Widgets """
    login_label  = tkinter.Label(
        frame, text='WhatsApp to Unsaved Contact', bg='#333333', fg='#FF3399', font=("Arial", 30)
        ).grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
    # username_label = tkinter.Label(
    #     frame, text='Phone Number:', bg='#333333', fg='#FFFFFF', font=("Arial", 20)
    #     ).grid(row=1, column=0, padx=20)

    opciones = [52, '01', 48]
    options = tkinter.StringVar(frame)
    options.set(opciones[0])
    lada_cmbbox = tkinter.OptionMenu(frame, options, *opciones
        ).grid(row=1, column=0, padx=0)

    username_entry = tkinter.Entry(frame, font=("Arial", 20)
        ).grid(row=1, column=1, pady=20)
    login_button = tkinter.Button(
        frame, text='Send message', bg='#FF3399', fg='#FFFFFF', font=("Arial", 18)
        ).grid(row=3, column=0, columnspan=2, pady=30)

    frame.pack()

    

    app.mainloop()

if __name__ == '__main__':
    main()