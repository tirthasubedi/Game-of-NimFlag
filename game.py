import random
from flag import *

class Game:

    def __init__(self):

        global root
        self.root = Tk()
        self.root.configure(background='black')  #bg color
        self.turncount=0
        self.titletext= Label(self.root, text="Welcome to the Game of Nim! \n After inputting the number to start button. \n Then click the buttons on the left side to remove the number of flags"
                                              " \n Player who removes the last flag will win the game. \n"
                                 , font=("Elephant"))
        self.titletext.pack(padx=0, pady=20)
        self.entrytext=Label(self.root, text = "Start the Game by Picking Number in range 10-35.",cursor="hand1", fg= "white", bg="black", font=("Helvetica", 15))
        self.entrytext.pack(padx=5, pady=100, side=LEFT)
        self.entry1=Entry(self.root)
        self.entry1.pack(padx=5, pady=100, side=LEFT)
        self.entry1.delete(0, END)
        self.b5 = Button(self.root, text = "Start by Submitting", command=self.submit_handler, cursor="hand2", font=("Helvetica", 12), bg="green")
        self.b5.pack(padx=5, pady=100, side=LEFT)
        self.root.title("Nim Game")
        self.root.pack_propagate()

        self.numflags=0
        self.user1=0
        self.root.mainloop()

    def start_game(self):
        """
        calling correct button for its command.
        :return: none
        """
        self.b1 = Button(self.root, text="Remove 1 flag", command= self.button_handler1, cursor="hand2" )
        self.b1.pack(padx=20, pady=5, side=TOP)
        self.b2 = Button(self.root, text="Remove 2 flag", command=self.button_handler2, cursor="hand2")
        self.b2.pack(padx=20, pady=5, side=TOP)
        self.b3 = Button(self.root, text="Remove 3 flag", command=self.button_handler3, cursor="hand2")
        self.b3.pack(padx=20, pady=5, side=TOP)
        self.b4 = Button(self.root, text = "Remove 4 flag", command=self.button_handler4, cursor="hand2")
        self.b4.pack(padx=20, pady=5, side=TOP)

    def button_handler1(self):
        """
        Button to remove one flag.
        :return: none
        """

        self.turncount += 1
        if self.turncount % 2 == 0:
            self.turn.config(text="Player 1")

        else:
            self.turn.config(text="Player 2")
        self.flaglist[0].remove()
        self.flaglist = self.flaglist[1:]

        if len(self.flaglist) <= 0:
            if self.turncount % 2 == 0:
                self.turn.config(text="Congratulation! The winner is:")
                text="Player 2"
                self.print_outcome(text)
            else:
                self.turn.config(text="Congratulation! The winner is:")
                text="Player 1"
                self.print_outcome(text)
        self.button_destroyer()

    def button_handler2(self):
        """
        button to remove two flags
        :return: none
        """
        self.turncount += 1
        if self.turncount % 2==0:
            self.turn.config(text="Player 1")
        else:
            self.turn.config(text="Player 2")
        for i in range(2):
            self.flaglist[0].remove()
            self.flaglist = self.flaglist[1:]

        if len(self.flaglist) <= 0:
            if self.turncount % 2 == 0:
                self.turn.config(text="Congratulatoin! The winner is:")
                text="Player 2"
                self.print_outcome(text)
            else:
                self.turn.config(text="Congratulation! The winner is:")
                text="Player 1"
                self.print_outcome(text)
        self.button_destroyer()

    def button_handler3(self):
        """
        button to remove 3 flags.
        :return: none
        """

        self.turncount +=1
        if self.turncount % 2==0:
            self.turn.config(text="Player 1")
        else:
            self.turn.config(text="Player 2")

        if len(self.flaglist)==1:
            self.turn.config(text="")

        for i in range(3):
            self.flaglist[0].remove()
            self.flaglist = self.flaglist[1:]

        if len(self.flaglist[:]) <= 0:
            if self.turncount % 2 == 0:
                self.turn.config(text="Congratulation! The winner is:")
                text="Player 2"
                self.print_outcome(text)
            else:
                self.turn.config(text="Congratulation! The winner is:")
                text="Player 1"
                self.print_outcome(text)
        self.button_destroyer()

    def button_handler4(self):
        """
        Button to remove 4 flags
        :return: none
        """
        self.turncount +=1
        if self.turncount % 2==0:
            self.turn.config(text="Player 1")
        else:
            self.turn.config(text="Player 2")

        if len(self.flaglist)==1:
            self.turn.config(text="")

        for i in range(4):
            self.flaglist[0].remove()
            self.flaglist = self.flaglist[1:]

        if len(self.flaglist[:]) <= 0: # check numb of flags to print correct statemetns
            if self.turncount % 2 ==0:
                self.turn.config(text="Congratulation! The winner is:")
                text="Player 2 wins"
                self.print_outcome(text)
            else:
                self.turn.config(text="Congration! The winner is:")
                text="Player 1"
                self.print_outcome(text)

        self.button_destroyer() # destroy button

    def button_destroyer(self):
        """
        destroyes the button if there are less ball then the button #
        :return: none
        """
        if len(self.flaglist)<4:
            self.b4.destroy()
        if len(self.flaglist)<3:
            self.b3.destroy()
        if len(self.flaglist)<2:
            self.b2.destroy()
        if len(self.flaglist)<1:
            self.b1.destroy()

    def print_outcome(self,text):
        """
        prints text
        :param text:
        :return: the text
        """
        text_widget=Label(self.root,text=text)
        text_widget.pack()

    def submit_handler(self):
        """
        allows user to submit.
        :return: none
        """
        self.numflags = self.entry1.get()
        self.user(self.numflags)

    def user(self, a):
        """
        make sure there are atleast 15 flags to start the game.
        :return: number of flags to start the game with.
        """
        self.user1 = int(a)                       # convert into int
        if self.user1 < 10 or self.user1> 35:
            self.entry1.delete(0, END)
            self.entry1.insert(0, "Try Again!")
            return

        self.entrytext.forget()
        self.entry1.forget()
        self.b5.forget()
        self.flaglist = []
        counter=0
        for i in range(self.user1):
            self.numflags += str(1)
            counter=counter+1
            var= counter//10
            flag=Flag(self.root,3*var)
            self.flaglist.append(flag)
        self.turn=Label(text="Player 1")
        self.turn.pack(padx=40, pady=10)
        self.start_game()
