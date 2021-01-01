from script import *
import tkinter as tk
from tkinter import Tk, Label, LabelFrame, Entry, Button, filedialog, messagebox, ttk

root = Tk()
window_width = 650
window_height = 190
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width / 2 - window_width/2)
root.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top-20}')
root.title('Bulk Files Organizer')
root.resizable(0, 0)  # remove maximize tab

heading = Label(root, text='Organize Bulk Files', bg='yellow',
                padx=10, pady=10, font='Helvetica 15 bold')
heading.pack(fill=tk.X)


def Advanced():
    progress['value'] = 0


def clicked():
    Action(progress, e.get())


def Dialog():
    progress['value'] = 0
    l = filedialog.askdirectory()
    global e
    e.delete(0, 'end')
    e.insert(0, l)
    
frame = LabelFrame(root, padx=10, pady=10)
frame.pack(pady=0, fill=tk.X)
eLabel = Label(frame, text="Enter Path:", font='Helvetica 10')
eLabel.pack()
folder = Button(frame, text='---', command=Dialog, borderwidth=3, padx=6)
folder.pack(side=tk.RIGHT, padx=3)
e = Entry(frame, borderwidth=2)
e.pack(fill=tk.X, pady=3)

l = Label(root, text="Status:", padx=16).pack(side=tk.LEFT)
progress = ttk.Progressbar(root, orient="horizontal",
                           length=150, mode='determinate')
progress.pack(side=tk.LEFT, padx=6)

Adv_button = Button(root, text="Advanced Settings", command=Advanced)
Adv_button.pack(side=tk.RIGHT, padx=16)
Org_button = Button(root, text="Organize", background='light green',
                    command=clicked, width=11)  
Org_button.pack(side=tk.RIGHT)


root.mainloop()
