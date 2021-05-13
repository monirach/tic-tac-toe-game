#import library
from tkinter import *
import random

#initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg ='seashell3')


#heading
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'seashell2').pack()

##user choice
userinput = StringVar()
Label(root, text = 'Pick one: rock, paper ,scissors' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = userinput , bg = 'antiquewhite2').place(x=90 , y = 130)



#computer choice
gameaction = ["rock", "paper", "scissors"]
computerpick = random.choice(gameaction)
    



#function to play
Result = StringVar()

def play():
    userpick = userinput.get()
    if userpick == computerpick:
        Result.set('Its a tie! You both chose ' + user_pick)
    elif userpick == 'rock' and computerpick == 'paper':
        Result.set('Computer chose Paper and covers Rock. You Lose.')
    elif userpick == 'rock' and computerpick == 'scissors':
        Result.set('Computer chose Rock and smashes scissors. You Win!')
    elif userpick == 'paper' and computerpick == 'scissors':
        Result.set('Computer chose Scissors and cuts Paper. You Lose')
    elif userpick == 'paper' and computerpick == 'rock':
        Result.set('Computer chose Paper and covers rock. You win!')
    elif userpick == 'scissors' and computerpick == 'rock':
        Result.set('Computer chose Rock and smashes scissors. You Lose.')
    elif userpick == 'scissors' and computerpick == 'paper':
        Result.set('Computer chose Scissors and cuts Paper. You Win!')
    else:
        Result.set('Field cannot be blank. Choose rock, paper, scissors')
    
        
    
##reset button function
def Reset():
    Result.set("") 
    userinput.set("")

#exit button function
def Exit():
    root.destroy()


#Design for buttons
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)

root.mainloop()
