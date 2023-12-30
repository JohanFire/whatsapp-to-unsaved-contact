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
        """ Validate textbox to allow 
        - only numbers or space
        - no more than 10 digits or 12 if contains format's space
        """
        # return digit.isdigit() or digit == ""

        if ' ' in digit:
            if len(digit) >= 13:
                # self.phone_number_entry.configure(state='disabled')
                return False
            
        else:
            if len(digit) == 10:
                digit_spaced = digit[:2] + ' ' + digit[2: ]
                digit_spaced = digit_spaced[:7] + ' ' + digit_spaced[7: ]
                print(digit_spaced)

                self.phone_number_entry.delete(0, 'end')
                self.phone_number_entry.insert(0, digit_spaced)

                # return False
            elif len(digit) > 10:
                return False
        
        validated_digit = digit
        pattern = re.compile(r'^[0-9\s]+$')
            
        # Verify if phone number matchs with the pattern
        if pattern.match(validated_digit):
            return True
        elif validated_digit == "":
            return True
        else:
            return False