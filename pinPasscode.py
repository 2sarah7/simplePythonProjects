
import tkinter as tk


passpin = "1234"

tryleft = 3

def getpass(entered, pin, tries):
    entered = userInput.get()
    if tries > 0:
        if entered == pin:
            row.config(text=f"Password is correct, access granted. ")
        else:
            
            tries -= 1

            row.config(text=f"Password is incorrect")
            #, {tries} tries left
    else:
        row.config(text=f"Too many failed atempts. Please try again later. ")

window = tk.Tk()
window.title("Enter password")
window.geometry("400x200")
heading = tk.Label(window, text="Please enter your password")
heading.pack()

userInput = tk.Entry(window)
userInput.pack()

button = tk.Button(window, text="Submit", command=lambda: getpass(userInput, passpin, tryleft) )
button.pack()

row = tk.Label(window, text=f"...")
row.pack()

window.mainloop()
