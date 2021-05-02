from tkinter import *
from tkinter.ttk import *
from sklearn import tree
import time as tm
#=====================================================

window = Tk()

window.title("Welcome to Prediction app")

window.geometry('400x250')

window.configure(bg='#009900')

lbl = Label(window, text="Weight: ")

lbl.grid(column=0, row=1, padx=10, pady=10)

txt = Entry(window,width=20)

txt.grid(column=1, row=1,padx=10, pady=10)

lbl2 = Label(window, text="Skin: ")

lbl2.grid(column=0, row=2)

combo = Combobox(window)

combo['values']= ('Bumpy','Smooth')

combo.current(1) #set the selected item

combo.grid(column=1, row=2)

lbl3 = Label(window, text="Can I help you?", font=("Arial Bold", 20))

lbl3.grid(column=1, row=6,  padx=10, pady=10)
#=====================================================

def clicked():
    features = [[140,1], [130,1], [150,0], [170, 0]]
    labels = [0,0,1,1]

    if txt.get() == "":
        lbl3.configure(text="Please enter weight :(")
    else:
        weight = float(txt.get())
        if combo.get() == 'Smooth':
            skin = 1
        else:
            skin = 0

        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        x = clf.predict([[weight,skin]])

        if x == 0:
            lbl3.configure(text="This is a apple!")
        else:
            lbl3.configure(text="This is a orange!")

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=4, padx=10, pady=10)
#=====================================================

def display_time():
    current_time = tm.strftime('%I:%M:%S:%p')
    clock_label['text'] = current_time
    clock_label.after(1000, display_time)

clock_label = Label(window, font=("Arial Bold", 10)) 
clock_label.grid(column=1, row=0, padx=10, pady=10)
display_time()
window.mainloop()
