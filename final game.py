from tkinter import *
import random



def computerRandom():

    options = ["Rock", "Paper", "Scissors"]
    randomChoice = random.randint(0, 2)
    computer_choice.set(options[randomChoice])  ##added into the program
    return options[randomChoice]


def comparison(humanChoice, computerChoice):
    if humanChoice == computerChoice:
        return "Draw"
    if humanChoice == "Rock" and computerChoice == "Paper":
        return "Computer Wins"
    if humanChoice == "Paper" and computerChoice == "Scissors":
        return "Computer Wins"
    if humanChoice == "Scissors" and computerChoice == "Rock":
        return "Computer Wins"
    else:
        return "Human Wins"


def play():
    humanChoice = player_choice.get()  ##Modified this line
    computerChoice = computerRandom()

    result = comparison(humanChoice, computerChoice)

    if result == "Draw":
        result_set.set("Its a draw")
    elif result == "Computer Wins":
        result_set.set("Unlucky you lost!")
    else:
        result_set.set("Well done you won!")


root = Tk()
root.title('Rock Paper Scissors')
root.resizable(0,0)
root.geometry("300x300")
# mainframe = Frame(root, padding='3 3 12 12')
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)

##Variables
player_choice = StringVar()
player_choice.set("Rock")
computer_choice = StringVar()
computer_choice.set(None)
result_set = StringVar()
# player_choice.set("Rock")  ## Required to set player as "Rock" by default

##Layout of GUI
##Player
Label(root, text='Player').grid(column=1, row=1, sticky=W)
Radiobutton(root, text='Rock', variable=player_choice, value='Rock').grid(column=1, row=2, sticky=W)
Radiobutton(root, text='Paper', variable=player_choice, value='Paper').grid(column=1, row=3, sticky=W)
Radiobutton(root, text='Scissors', variable=player_choice, value='Scissors').grid(column=1, row=4, sticky=W)

##Computer
Label(root, text='Computer').grid(column=3, row=1, sticky=W)
Radiobutton(root, text='Rock', variable=computer_choice, value='Rock').grid(column=3, row=2, sticky=W)
Radiobutton(root, text='Paper', variable=computer_choice, value='Paper').grid(column=3, row=3, sticky=W)
Radiobutton(root, text='Scissors', variable=computer_choice, value='Scissors').grid(column=3, row=4, sticky=W)

##Play
Button(root, text="Play", command=play).grid(column=2, row=2, sticky=W)

##Result
Label(root, textvariable=result_set).grid(column=1, row=5, sticky=W, columnspan=2)
# Label(root,textvarible=randomChoice).grid(column=1, row=5, sticky=W, columnspan=2)

root.mainloop()
