from time import sleep
import psutil
from tkinter import *

temperatures = psutil.sensors_temperatures()
root = Tk()


new_text = ''
sec_col  = ''
third_col= ''
fo_col   = ''
fif_col  = ''

####### update columns #######
def update():
    temperatures = psutil.sensors_temperatures()
    third_col= ''
    fo_col   = ''
    fif_col  = ''

    ######## third column ########
    for elm in temperatures:
        x = 0
        for x in range(len(temperatures[elm])):
            third_col += str(temperatures[elm][x].current) + '\n'
            fo_col += str(temperatures[elm][x].high) + '\n'
            fif_col += str(temperatures[elm][x].critical) + '\n'

######## lables and titles ########
    lbl3 = Label(root, text = third_col,  font=("Arial Bold", 12))
    lbl3.grid(column=2, row=1)

    lbl4 = Label(root, text = fo_col,  font=("Arial Bold", 12))
    lbl4.grid(column=3, row=1)

    lbl5 = Label(root, text = fif_col,  font=("Arial Bold", 12))
    lbl5.grid(column=4, row=1)
    root.after(1000, update)

######## first column ########
for elm in temperatures:
    new_text += elm + len(temperatures[elm])*'\n'

######## second column ########
for elm in temperatures:
    x = 0
    for x in range(len(temperatures[elm])):
        sec_col += str(temperatures[elm][x].label) + '\n'


######## lables and titles ########
root.title("System temperature")
root.geometry("600x350")

title1 = Label(root, text = "  Name  ",  font=("Arial Bold", 18))
title1.grid(column=0,row=0)

title2 = Label(root, text = "  Label  ",  font=("Arial Bold", 18))
title2.grid(column=1,row=0)

title3 = Label(root, text = "  Current  ",  font=("Arial Bold", 18))
title3.grid(column=2,row=0)

title2 = Label(root, text = "  High  ",  font=("Arial Bold", 18))
title2.grid(column=3,row=0)

title2 = Label(root, text = "  Critical  ",  font=("Arial Bold", 18))
title2.grid(column=4,row=0)

lbl = Label(root, text = new_text,  font=("Arial Bold", 12))
lbl.grid(column=0, row=1)

lbl2 = Label(root, text = sec_col,  font=("Arial Bold", 12))
lbl2.grid(column=1, row=1)

######## window start ########
update()
root.mainloop()
