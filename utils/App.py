import tkinter
import webbrowser
import re

class App:
    def __init__(self, master):
        self.master = master
        # master.title("WhatsApp to Unsaved Contact")

        self.frame = tkinter.Frame(bg='#333333')

        """ Frame Widgets """
        self.title_label  = tkinter.Label(
            self.frame, text='WhatsApp to Unsaved Contact', bg='#333333', fg='#FF3399', font=("Arial", 30)
            ).grid(row=0, column=1, sticky='news', pady=40)
        
        self.phone_number_entry = tkinter.Entry(self.frame, font=("Arial", 20), validate='key')
        self.phone_number_entry['validatecommand'] = (self.phone_number_entry.register(self.validate_phone_digit), '%P')        
        
        # Formatear automáticamente el número al estilo "XX XXXX XXXX"
        self.phone_number_entry.bind('<KeyRelease>', self.format_phone_number)
        # self.phone_number_entry.bind('<KeyRelease>', self.validate_phone_format)
        
        self.phone_number_entry.grid(row=1, column=1, pady=20)

        self.send_message_button = tkinter.Button(
            self.frame, text='Send message', bg='#FF3399', fg='#FFFFFF', font=("Arial", 18),
            command=self.send_message_action
            ).grid(row=3, column=1, columnspan=2, pady=30)

        self.frame.pack()

    def send_message_action(self):
        if self.phone_number_entry:
            print(self.phone_number_entry.get())
            phone_number = self.phone_number_entry.get().replace(' ', '')
            print(phone_number)

            if len(phone_number) == 10:
                self.phone_number_entry.delete(0, 'end')

                webbrowser.open(f"https://wa.me/{phone_number}")

    def validate_phone_digit(self, digit):
        """ Validate textbox to allow only numbers """
        # return digit.isdigit() or digit == ""

        patron = re.compile(r'^[0-9\s]+$')
            
        # Verificar si el texto coincide con el patrón
        if patron.match(digit):
            return True
        else:
            return False
    


        # current_text = self.phone_number_entry.get()
    
        # # Permitir solo dígitos y espacios si ya hay al menos un dígito
        # return digit.isdigit() or (digit == " " and any(char.isdigit() for char in current_text))

    # def validate_phone_format(self, event):
    #     phone_number = self.phone_number_entry.get()

    #     if len(phone_number) == 2:
    #         print(phone_number)




    def format_phone_number(self, event):
        # Formatear automáticamente el número al estilo "XX XXXX XXXX"
        current_text = self.phone_number_entry.get()
        formatted_text = self.format_as_phone_number(current_text)
        # self.phone_number_entry.delete(0, 'end')
        self.phone_number_entry.insert(0, formatted_text)

    def format_as_phone_number(self, raw_text):
        # Formatear el número al estilo "XX XXXX XXXX"
        digits = [char for char in raw_text if char.isdigit()]
        formatted_text = ''

        if len(digits) == 2:
            if digits[-1] == ' ':
                print(digits[-1])
                return
                
            print('len(digits) == 2')
            # formatted_text += ''.join(digits[0:2]) + ' '
            
            new_text = raw_text + ' '
            self.phone_number_entry.delete(0, 'end')
            self.phone_number_entry.insert(2, ' ')

        if len(digits) == 6:
            print('len(digits) == 6')
            # formatted_text += ''.join(digits[2:6]) + ' '

            self.phone_number_entry.insert(7, ' ')


        return formatted_text