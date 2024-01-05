# WhatsApp to Unsaved Contact
Send Whatsapp message to an unsaved contact with a GUI App.


## Valid cursor strings for tkinter buttons:
[Valid Cursor Strings](https://www.pysimplegui.org/en/latest/#cursors-setting-for-elements-and-windows)


---

## ToDo
- create Info class for Info window
- fix phone_number_entry somehow


---
## Make executable
Create portable app, it contains more folders/files in order to make the app run.
```bash
pyinstaller main.py
```

Create one single executable, with any other necessary file to run it.
```bash
pyinstaller main.py --onefile
```
but it also opens a bash terminal to run it, so in order to suppress it:
```bash
pyinstaller main.py --onefile -w
```