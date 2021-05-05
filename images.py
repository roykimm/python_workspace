from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("gobella")
root.iconbitmap('images/dumbbells_gym_fitness_sport_icon_186978.png')

my_img = ImageTk.PhotoImage(Image.open("images/dumbbells_gym_fitness_sport_icon_186978.png"))
my_label = Label(image=my_img)
my_label.pack()



button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()