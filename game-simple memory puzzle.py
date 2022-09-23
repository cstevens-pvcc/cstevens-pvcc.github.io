# NAME: your name here
# Program Purpose: Match color & shape game
# This program uses "tkinter," the standard Python GUI (Graphical User Interface).

from tkinter import *
import random
from tkinter import ttk


def draw(a,l,m):
    global base
    if a == 'A':
        d = base.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
    elif a == 'B':
        d = base.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
    elif a == 'C':
        d = base.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
    elif a == 'D':
        d = base.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
    elif a == 'E':
        d = base.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
    elif a == 'F':
        d = base.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
    elif a == 'G':
        d = base.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='red')
    elif a == 'H':
        d = base.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='green')
    
def quizboard():
    global base, answer, board, moves
    count=0
    for i in range(4):
        for j in range(4):
            rec = base.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="#cf00cc") #you can use hex color numbers
            if(board[i][j] != '.'):
                draw(board[i][j],i,j)
                count+=1
    if count == 16:
        base.create_text(200,450,text="Number of moves: " + str(moves),font=('arial',18))
            

def call(event):
    global base,answer,board,moves,previous
    i = event.x//100
    j = event.y//100
    if board[i][j] != '.':
        return
    
    moves+=1
    #print(moves)
    if(previous[0]>4):
        previous[0] = i
        previous[1] = j
        board[i][j] = answer[i][j]
        quizboard()
    else:
        board[i][j] = answer[i][j]
        quizboard()
        if(answer[i][j] == board[previous[0]][previous[1]]):
            print("matched")
            previous = [100,100]
            quizboard()
            return
        else:
            board[previous[0]][previous[1]]='.'
            quizboard()
            previous = [i,j]
            return

#Set up the puzzle window using tkinter objects
PuzzleWindow=Tk()
PuzzleWindow.title('Memory Puzzle Game Using Shapes')
tabs = ttk.Notebook(PuzzleWindow) 
matchgame = ttk.Frame(tabs)

base=Canvas(matchgame,width=500,height=500)
base.pack()

answer = list('AABBCCDDEEFFGGHH')
random.shuffle(answer)
answer = [answer[:4],
       answer[4:8],
       answer[8:12],
       answer[12:]]

base.bind("<Button-1>", call)

moves = IntVar()
moves = 0
previous = [100,100]
board = [list('.'*4) for count in range(4)]
quizboard()
tabs.add(matchgame, text ='Click a square to reveal shape. \nMatch all color-shapes in the fewest moves.') 
tabs.pack(expand = 1, fill = "both") 

#mainloop() tells Python to run the Tkinter event 
mainloop()
