import base64
import tkinter as tk
import tkinter.filedialog as fd
from datetime import date, time
import os
import uuid
from os import path
from tkinter import messagebox


root = tk.Tk()
v = tk.StringVar()
root.title("Base64 Decoder")

tk.Label(root, text="Base64 file location").grid(row=1)

base64string  = tk.Entry(root)
base64string.grid(row=1, column=1)



def browse():
    currdir = os.getcwd()
    fileDir = fd.askopenfilename(parent=root, initialdir=currdir, title='Please select a file')
    base64string.insert(0, fileDir)
    return fileDir

def convert():
    fileName = 'Output' + str(uuid.uuid4()) + str(v.get())
    file = open(base64string.get(), 'rb')
    coded_string = file.read()

    decodedStr = base64.b64decode(coded_string)

    pdfFile = open(os.getcwd() + "\\" + str(fileName), 'wb')
    #print(decodedStr)
    pdfFile.write(decodedStr)
    pdfFile.close()
    if(path.exists(os.getcwd() + "\\" + str(fileName))):
        messagebox.showinfo("Success", "File created.")


browseButton = tk.Button(root, text="Browse", fg="red", command=browse)
browseButton.grid(row=3, column=1)
convertButton = tk.Button(root, text="Convert", fg="green", command=convert)
convertButton.grid(row=6, column=0)

choiceLabel = tk.Label(root, text="""Choose output format:""",justify = tk.LEFT)
xmlButton = tk.Radiobutton(root, text="XML",padx = 20, variable=v, value='.xml')
xmlButton.grid(row=4, column=0)
pdfButton = tk.Radiobutton(root, text="PDF",padx = 20, variable=v, value='.pdf')
pdfButton.grid(row=5, column=0)

pdfButton.select() # select #PDF as a default
choiceLabel.grid(row=3, column=0)

root.mainloop()

