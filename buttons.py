from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look i clicked a button!")
    myLabel.pack()

# myButton = Button(root, text="click me!", state=DISABLED)
# myButton = Button(root, text="click me!", padx=30, pady=50)
myButton = Button(root, text="click me!", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()


root.mainloop()