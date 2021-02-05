from tkinter import filedialog
from tkinter import *

window = Tk()
window.title("Process Mining tool")
window.geometry("600x300")
lbl = Label(window, text = "Input your training and test .csv files, and give a name to the output file:", font=("Helvetica Neue", 12))
lbl.grid(column=0, row=0)

training_path = filedialog.askopenfilename(filetypes = ("CSV files", "*.csv"))

test_path = filedialog.askopenfilename(filetypes = ("CSV files", "*.csv"))


window.mainloop()