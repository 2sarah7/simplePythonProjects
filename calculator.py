import tkinter as tk

global mathstr
#create the window
window = tk.Tk()
window.title("Calculator")
window.geometry("500x500")

#create the label at the top
label = tk.Label(text="Calc1:")
label.grid(row=0, column=0)

#create where you can manually type in math expressions
txtBox = tk.Entry(window, width=5)
txtBox.grid(row=1)

dispEq = tk.Button(text="=")
dispEq.grid(row=1, column=1)

#this shows answer from both manual typing
txtAnswer = tk.Label(text="Ans")
txtAnswer.grid(row=1, column=3)

label2 = tk.Label(text="Calc2:")
label2.grid(row=2, column=0)

bExpress = tk.Label(text=".")
bExpress.grid(row=2, column=1)

bAns = tk.Label(text="Ans")
bAns.grid(row=2, column=3)

#creates all buttons 
b1 = tk.Button(window, text="1")
b1.grid(row=3, column=0)

b2 = tk.Button(window, text="2")
b2.grid(row=3, column=1)

b3 = tk.Button(window, text="3")
b3.grid(row=3, column=2)

b4 = tk.Button(window, text="4")
b4.grid(row=4, column=0)

b5 = tk.Button(window, text="5")
b5.grid(row=4, column=1)

b6 = tk.Button(window, text="6")
b6.grid(row=4, column=2)

b7 = tk.Button(window, text="7")
b7.grid(row=5, column=0)

b8 = tk.Button(window, text="8")
b8.grid(row=5, column=1)

b9 = tk.Button(window, text="9")
b9.grid(row=5, column=2)

bPlus = tk.Button(window, text="+")
bPlus.grid(row=3, column=3)

bMinus = tk.Button(window, text="-")
bMinus.grid(row=4, column=3)

bDiv = tk.Button(window, text="/")
bDiv.grid(row=5, column=3)

buttonEqual = tk.Button(window, text="=")
buttonEqual.grid(row=6, column=3)

#solves from text box
def calculateByTyping():
  global i 
  i = 2
  value = txtBox.get()
  result = eval(value)
  txtAnswer.config(text=result)

#might need to rearange this to put it at the top - each button is supposed to add a digit or symbol to mathstr so when the equal button is hit the fully typed expression can be calculated
mathstr = " "
def addone():
    mathstr = mathstr + "1"
b1.config(command=addone())

def addtwo():
    mathstr = mathstr + "2"
b2.config(command=addtwo)


def calculateByButtons():
    value1 = eval(mathstr)
    bAns.config(text=value1)

#how to make it so the = can do both?

dispEq.config(command=calculateByTyping)

buttonEqual.config(command=calculateByButtons)




















window.mainloop()

