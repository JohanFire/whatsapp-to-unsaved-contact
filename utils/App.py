import tkinter
from tkinter import ttk
import webbrowser
import re

from utils.screen import render_center_of_screen

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

        self.info_button = tkinter.Button(
            self.frame, text='info', border=0, bg='#333333', fg='#636e72', font=("Arial", 14),
            cursor='hand2', activebackground='#333333', activeforeground='#FFFFFF',
            command=self.info_action
            ).grid(row=4, column=1)

        self.frame.pack()

        self.phone_number_entry.focus_set()

    def send_message_action(self):
        if len(self.phone_number_entry.get()) >= 10:
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
        
    def info_action(self):
        info_window = tkinter.Toplevel(self.master)
        info_window.title("App Info")
        width, height, x, y = render_center_of_screen(info_window, width=400, height=200)
        info_window.geometry(f"{width}x{height}+{x}+{y}")
        info_window.resizable(width=False, height=False)
        info_window.configure(bg='#333333')

        johanfire = tkinter.Label(info_window, 
            text='www.johanfire.com', 
            bg='#333333', fg='#ff5cad', font=("Arial", 12),
            ).pack()
        github = tkinter.Label(info_window, 
            text='See open source project on github.com/johanfire', 
            bg='#333333', fg='#ff5cad', font=("Arial", 12), pady=60,
            ).pack()
        version = tkinter.Label(info_window, 
            text='v1.1', 
            bg='#333333', fg='#ff5cad', font=("Arial", 12),
            ).pack()