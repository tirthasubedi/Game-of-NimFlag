from tkinter import *
from PIL import ImageTk, Image

class Flag:

    def __init__(self, root,var):
        self.image = "snepal1.gif"
        self.img = ImageTk.PhotoImage(Image.open("snepal1.gif"))
        self.root=root
        self.panel = Label(self.root, image=self.img)
        self.panel.pack(padx=0, pady=0, side=RIGHT)
    def remove(self):
        """
        destrying panel
        :return: none
        """
        self.panel.destroy()
