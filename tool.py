from tkinter import filedialog
from tkinter import *

from most_frequent_opt import baseline_next_event

def print_file():
    
    res = "Input files are TRAIN: {}, TEST: {}, Output filename: {}".format(train_path.get(), test_path.get(), output_filename.get())
    lbl3.configure(text=res)
    baseline_next_event(train_path.get(), test_path.get(), output_filename.get())
    lbl3.configure(text="Task done!")
    
window = Tk()
window.title("Process Mining tool")
window.geometry("600x300")
lbl = Label(window, text = "Input your training and test .csv files, and give a name to the output file:", font=("Helvetica Neue", 12))
lbl.grid(column=0, row=0)
lbl2 = Label(window, text = "Important! The files should be in the same directory as this file, otherwise specify complete path", font=("Helvetica Neue", 9))
lbl2.grid(column=0, row=1)

train_path = Entry(window, width = 30)
train_path.grid(column=0, row=2)
test_path = Entry(window, width=30)
test_path.grid(column=0, row=3)
output_filename = Entry(window, width=30)
output_filename.grid(column=0, row=4)

submit_btn = Button(window, text="Submit", command=print_file).grid(column=0, row=5)
lbl3 = Label(window, text="Submit the two csv files")
lbl3.grid(column=0, row=6)



window.mainloop()