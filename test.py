from time import sleep
import psutil
from tkinter import *


temperatures = psutil.sensors_temperatures()
root = Tk()

# for el in temperatures:
#     print(el)
#     perv = temperatures[el]
#     print(type(perv))
#     print(perv[0])
#     print(type(perv[0]))
#     print('\n')
#     # print(perv[1])
#     # print('\n')
#     #print(perv)

print(temperatures)

new_text = 'name\n'
sec_col  = 'label\n'
third_col= 'current\n'
fo_col   = 'high\n'
fif_col  = 'critical\n'

######## first column ########
for elm in temperatures:
    new_text += elm + len(temperatures[elm])*'\n'

######## second column ########
for elm in temperatures:
    x = 0
    for x in range(len(temperatures[elm])):
        sec_col += str(temperatures[elm][x].label) + '\n'

######## third column ########
for elm in temperatures:
    x = 0
    for x in range(len(temperatures[elm])):
        third_col += str(temperatures[elm][x].current) + '\n'

######## fourt column ########
for elm in temperatures:
    x = 0
    for x in range(len(temperatures[elm])):
        fo_col += str(temperatures[elm][x].high) + '\n'

######## fifth column ########
for elm in temperatures:
    x = 0
    for x in range(len(temperatures[elm])):
        fif_col += str(temperatures[elm][x].critical) + '\n'

# for elm in temperatures:
#     print(elm)


# for elm in temperatures:
#     sec_col += str(temperatures[elm][0].current) + '\n'

text = psutil.sensors_temperatures()
#print(text)
# dlin = len(text)
# print(dlin)


######## lables and titles ########
root.title("System temperature")
root.geometry("600x350")

lbl = Label(root, text = new_text)
lbl.grid(column=0, row=0)

lbl2 = Label(root, text = sec_col)
lbl2.grid(column=2, row=0)

lbl3 = Label(root, text = third_col)
lbl3.grid(column=3, row=0)

lbl4 = Label(root, text = fo_col)
lbl4.grid(column=4, row=0)

lbl5 = Label(root, text = fif_col)
lbl5.grid(column=5, row=0)

######## wndow start ########
root.mainloop()
