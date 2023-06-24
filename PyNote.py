import tkinter as tk
from tkinter import filedialog, Text, Frame, LEFT, BOTH, WORD, END

def save_file():
    new_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if new_file is not None:
        text = str(entry.get(1.0, END))
        new_file.write(text)
        new_file.close()

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)  # Clear the text widget
        entry.insert(tk.END, content)

def clear_file():
    entry.delete(1.0, END)

gui = tk.Tk()
gui.geometry("400x600")  # Size of the notepad
gui.title("PyNote")  # Title of the notepad
gui.configure(bg='#e3f2fd')

top = Frame(gui)
top.pack(padx=10, pady=5, anchor='nw')

open_btn = tk.Button(top, text="Open", font=('arial', 10), command=open_file)
open_btn.pack(side=LEFT, padx=2)

save_btn = tk.Button(top, text="Save", font=('arial', 10), command=save_file)
save_btn.pack(side=LEFT, padx=2)

clear_btn = tk.Button(top, text="Clear", font=('arial', 10), command=clear_file)
clear_btn.pack(side=LEFT, padx=2)

entry = Text(gui, wrap=WORD, bg='white', font=("arial", 12))
entry.pack(padx=10, pady=5, expand=True, fill=BOTH)

gui.mainloop()
