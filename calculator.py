import tkinter as tk

global mathstr
#create the window
window = tk.Tk()
window.title("Calculator")
window.geometry("500x500")

#create the label at the top
label = tk.Label(text="Calculator:")
label.grid(row=0, column=0)

#create where you can manually type in math expressions
txtBox = tk.Entry(window, width=6)
txtBox.insert("end", " ")
txtBox.grid(row=1)


#this shows answer from both manual typing
txtAnswer = tk.Label(text="Ans")
txtAnswer.grid(row=1, column=3)

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

bClr = tk.Button(window, text="clr")
bClr.grid(row=6, column=0)

b8 = tk.Button(window, text="8")
b8.grid(row=5, column=1)

b0 = tk.Button(window, text="0")
b0.grid(row=6, column=1)

b9 = tk.Button(window, text="9")
b9.grid(row=5, column=2)

bPlus = tk.Button(window, text="+")
bPlus.grid(row=3, column=3)

bMinus = tk.Button(window, text="-")
bMinus.grid(row=4, column=3)

bDiv = tk.Button(window, text="/")
bDiv.grid(row=5, column=3)

bMult = tk.Button(window, text="*")
bMult.grid(row=2, column=3)

bDecimal = tk.Button(window, text=".")
bDecimal.grid(row=6, column=2)

buttonEqual = tk.Button(window, text="=")
buttonEqual.grid(row=6, column=3)

def addone():
    current = txtBox.get()
    txtBox.insert(tk.END, str("1"))
b1.config(command=addone)

def addtwo():
    current = txtBox.get()
    txtBox.insert(tk.END, str("2"))
b2.config(command=addtwo)

def addthree():
    current = txtBox.get()
    txtBox.insert(tk.END, str("3"))
b3.config(command=addthree)

def addfour():
    current = txtBox.get()
    txtBox.insert(tk.END, str("4"))
b4.config(command=addfour)

def addfive():
    current = txtBox.get()
    txtBox.insert(tk.END, str("5"))
b5.config(command=addfive)

def addsix():
    current = txtBox.get()
    txtBox.insert(tk.END, str("6"))
b6.config(command=addsix)

def addseven():
    current = txtBox.get()
    txtBox.insert(tk.END, str("7"))
b7.config(command=addseven)

def addeight():
    current = txtBox.get()
    txtBox.insert(tk.END, str("8"))
b8.config(command=addeight)

def addnine():
    current = txtBox.get()
    txtBox.insert(tk.END, str("9"))
b9.config(command=addnine)

def addzero():
    current = txtBox.get()
    txtBox.insert(tk.END, str("0"))
b0.config(command=addzero)

def plus():
    current = txtBox.get()
    txtBox.insert(tk.END, str("+"))
bPlus.config(command=plus)

def sub():
    current = txtBox.get()
    txtBox.insert(tk.END, str("-"))
bMinus.config(command=sub)

def div():
    current = txtBox.get()
    txtBox.insert(tk.END, str("/"))
bDiv.config(command=div)

def multiply():
    current = txtBox.get()
    txtBox.insert(tk.END, str("*"))
bMult.config(command=multiply)

def deci():
    current = txtBox.get()
    txtBox.insert(tk.END, str("."))
bDecimal.config(command=deci)

def clr():
    current = txtBox.get()
    txtBox.delete(0, tk.END)
bClr.config(command=clr)


#solves from text box
def calculateByTyping():
  value = txtBox.get()
  result = eval(value)
  txtAnswer.config(text=result)




buttonEqual.config(command=calculateByTyping)





















window.mainloop()

