from tkinter import filedialog
from tkinter import *

window = Tk()
window.title("Process Mining tool")
window.geometry("600x300")
lbl = Label(window, text = "Input your training and test .csv files, and give a name to the output file:", font=("Helvetica Neue", 12))
lbl.grid(column=0, row=0)
lbl2 = Label(window, text = "Important! The files should be in the same directory as this file, otherwise specify complete path", font=("Helvetica Neue", 9))
lbl2.grid(column=0, row=1)

txt = Entry(window, width = 30).grid(column=0, row=2)
txt2 = Entry(window, width=30).grid(column=0, row=3)
def print_file():
    filenames = "Path to training: {} /// Path to test: {}".format(txt.get(), txt2.get())
    lbl3.configure(text=filenames)
submit_btn = Button(window, text="Submit", command=print_file).grid(column=0, row=4)
lbl3 = Label(window, text="Submit the two csv files").grid(column=0, row=5)


window.mainloop()