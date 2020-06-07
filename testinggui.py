from tkinter import *
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack(side = LEFT)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side = RIGHT)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
photo = PhotoImage(file = "slogo.png")
root.iconphoto(False, photo)
root.mainloop()