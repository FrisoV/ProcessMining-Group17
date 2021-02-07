from tkinter import filedialog
from tkinter import *

from most_frequent_opt import baseline_next_event

def print_file():
    
    res = "ERROR! We cannot find some files.\n Please check the file paths again!".format(train_path.get(), test_path.get(), output_filename.get())
    lbl3.configure(text=res)
    baseline_next_event(train_path.get(), test_path.get(), output_filename.get())
    lbl3.configure(text="Task done!")
    
window = Tk()
window.title("2IOI0 Group 17 tool")
window.geometry("270x300")
lbl = Label(window, text = "Baseline tool for 2IOI0 ", font=("Helvetica Neue", 11))
lbl.grid(column=0, row=0)


train_label = Label(window, text="Training set path(.csv)")
train_label.grid(column=0, row=1)
train_path = Entry(window, width = 40)
train_path.grid(column=0, row=2)
train_label = Label(window, text="Test set path(.csv)")
train_label.grid(column=0, row=3)
test_path = Entry(window, width=40)
test_path.grid(column=0, row=4)
train_label = Label(window, text="Ouput file name(including .csv)")
train_label.grid(column=0, row=5)
output_filename = Entry(window, width=40)
output_filename.grid(column=0, row=6)

submit_btn = Button(window, text="Submit", command=print_file).grid(column=0, row=7)
lbl3 = Label(window, text="Submit the two csv files")
lbl3.grid(column=0, row=8)



window.mainloop()