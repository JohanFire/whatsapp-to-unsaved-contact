import tkinter
# from tkinter import messagebox
from icecream import ic

def render_center_of_screen(app, width, height):
    # Centrar la ventana en la pantalla
    ancho_ventana = width
    alto_ventana = height

    # Obtener el ancho y alto de la pantalla
    ancho_pantalla = app.winfo_screenwidth()
    alto_pantalla = app.winfo_screenheight()

    # Calcular las coordenadas x e y para centrar la ventana
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2

    # # Establecer la geometría de la ventana con las coordenadas calculadas
    # app.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    return ancho_ventana, alto_ventana, x, y


def main():
    app = tkinter.Tk()
    app.title("WhatsApp to Unsaved Contact")

    width, height, x, y = render_center_of_screen(app, width=440, height=440)
    app.geometry(f"{width}x{height}+{x}+{y}")
    app.resizable(width=False, height=False)
    app.configure(bg='#333333')




    # Frame = container, with can place widgets inside the frame or directly to the app
    frame = tkinter.Frame(bg='#333333')

    # Widgets
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

    # Placing widgets on screen
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