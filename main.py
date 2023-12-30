import tkinter
from tkinter import ttk
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
    title_label  = tkinter.Label(
        frame, text='WhatsApp to Unsaved Contact', bg='#333333', fg='#FF3399', font=("Arial", 30)
        ).grid(row=0, column=1, sticky='news', pady=40)

    """ 
    # username_label = tkinter.Label(
    #     frame, text='Phone Number:', bg='#333333', fg='#FFFFFF', font=("Arial", 20)
    #     ).grid(row=1, column=0, padx=20)
    
    opciones = [52, '01', 48]
    options = tkinter.StringVar(frame)
    options.set(opciones[0])
    # lada_optionMenu = tkinter.OptionMenu(frame, options, *opciones, 
    #     ).grid(row=1, column=0, padx=0)

    # Crear un estilo para personalizar el menú desplegable
    estilo = ttk.Style()
    estilo.theme_create("mi_tema", parent="alt", settings={
        "TCombobox": {
            "configure": {"fieldbackground": '#333333', "background": '#C0C0C0', "foreground": "#FFFFFF",
                "font": ('Helvetica', 22)
            },
        }
    })
    # estilo.configure('TCombobox', font=('Helvetica', 22))
    estilo.theme_use("mi_tema")


    lada_cmbbox = ttk.Combobox(frame, values=opciones, textvariable=options, style='TCombobox')
    lada_cmbbox.grid(row=1, column=0, padx=0)
    """


    username_entry = tkinter.Entry(frame, font=("Arial", 20)
        ).grid(row=1, column=1, pady=20)
    login_button = tkinter.Button(
        frame, text='Send message', bg='#FF3399', fg='#FFFFFF', font=("Arial", 18)
        ).grid(row=3, column=1, columnspan=2, pady=30)

    frame.pack()

    

    app.mainloop()

if __name__ == '__main__':
    main()