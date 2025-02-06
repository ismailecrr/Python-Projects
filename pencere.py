from tkinter import *

window = Tk()
window.title("python tkinter")
window.geometry("800x600+200+200")  
window.minsize(300, 200)  

my_label = Label(window, text="This is a label") 
my_label.pack()

window.mainloop()



