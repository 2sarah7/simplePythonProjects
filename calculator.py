import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("500x500")

label = tk.Label(text="Calculator")
label.grid(row=0, column=0)

txtBox = tk.Entry(window, width=5)
txtBox.grid(row=1)

txtMath = tk.Label(text="Eq")
txtMath.grid(row=1, column=1)

txtAnswer = tk.Label(text="Ans")
txtAnswer.grid(row=1, column=3)

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


def calculateByTyping():
  value = txtBox.get()
  result = eval(value)
  txtAnswer.config(text=result)


buttonEqual.config(command=calculateByTyping)





















window.mainloop()

