import tkinter
import webbrowser

class App:
    def __init__(self, master):
        self.master = master
        # master.title("WhatsApp to Unsaved Contact")

        self.frame = tkinter.Frame(bg='#333333')

        """ Frame Widgets """
        self.title_label  = tkinter.Label(
            self.frame, text='WhatsApp to Unsaved Contact', bg='#333333', fg='#FF3399', font=("Arial", 30)
            ).grid(row=0, column=1, sticky='news', pady=40)
        self.phone_number_entry = tkinter.Entry(self.frame, font=("Arial", 20))
        self.phone_number_entry.grid(row=1, column=1, pady=20)

        self.send_message_button = tkinter.Button(
            self.frame, text='Send message', bg='#FF3399', fg='#FFFFFF', font=("Arial", 18),
            command=self.send_message_action
            ).grid(row=3, column=1, columnspan=2, pady=30)

        self.frame.pack()

    def send_message_action(self):
        if self.phone_number_entry:
            phone_number = self.phone_number_entry.get()
            print(f"phone_number: {phone_number}")

            self.phone_number_entry.delete(0, 'end')


        # # Especifica el enlace que deseas abrir
        # enlace = "https://www.google.com"

        # # Abre el enlace en el navegador web predeterminado
        # webbrowser.open(enlace)