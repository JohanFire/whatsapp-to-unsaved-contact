import tkinter
# from tkinter import messagebox

def main():
    app = tkinter.Tk()
    app.title("WhatsApp to Unsaved Contact")
    app.geometry('340x440')
    app.resizable(width=False, height=False)
    app.configure(bg='#333333')

    # Widgets
    login_label  = tkinter.Label(app, text='Login', bg='#333333', fg='#FFFFFF')
    username_label = tkinter.Label(app, text='Username', bg='#333333', fg='#FFFFFF')
    username_entry = tkinter.Entry(app)
    password_label = tkinter.Label(app, text='Password', bg='#333333', fg='#FFFFFF')
    password_entry = tkinter.Entry(app, show='*')
    login_button = tkinter.Button(app, text='Login', bg='#FF3399', fg='#FFFFFF')

    # Placing widgets on screen
    login_label.grid(row=0, column=0, columnspan=2)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)
    login_button.grid(row=3, column=0, columnspan=2)





    app.mainloop()

if __name__ == '__main__':
    main()