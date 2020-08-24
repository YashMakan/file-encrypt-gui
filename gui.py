import tkinter as tk
from tkinter import filedialog
from tkinter import *

def show_entry_fields():
    print('path:'+pat.get())
    path=pat.get()
    fo=open(path,'rb')
    image=fo.read()
    fo.close()
    image=bytearray(image)

    key=48

    for index , value in enumerate(image):
        image[index]=value^key

    fo=open(path,'wb')
    fo.write(image)
    fo.close()

def fun():
    master.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file to encrypt",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    pat.set(master.filename)
    print(pat.get())

master = tk.Tk()
master.title('Master')
pat = StringVar(value="Default Value")
tk.Label(master,textvariable=pat).grid(row=0)
tk.Button(master,text='Choose', command=fun).grid(row=1,column=0,sticky=tk.W,pady=4)
tk.Button(master,text='Encrypt/Decrypt', command=show_entry_fields).grid(row=2, column=0, sticky=tk.W, pady=4)
tk.mainloop()
