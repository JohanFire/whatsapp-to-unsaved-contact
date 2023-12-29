import tkinter
# from tkinter import messagebox

def main():
    app = tkinter.Tk()
    app.title("WhatsApp to Unsaved Contact")
    app.geometry('340x440')
    app.configure(bg='#333333')

    # Geometry managers: pack, place, grid
    label = tkinter.Label(app, text='Hello').pack()

    app.mainloop()

if __name__ == '__main__':
    main()