#imports the library's we need to run everything
import tkinter as tk
import random

#picks a random number
x = 100
num_wins = 0
num = random.randint(1,x)


#this runs when the button is clicked
def get_num(wins,number):
    #turning the user input into a number (int)
    
    try:
        user_input_int = int(user_input.get())
    except:
        win_label.config(text="NOT A NUMBER")
        return None

    #will check if user input is equal to the random number
    if number == user_input_int:
        global num_wins
        num_wins += 1
        global num
        num = random.randint(1,x)
        print(num)
        user_input.delete(1)
        num_of_wins.config(text=f'Number of wins: {num_wins}')
        win_label.config(text="win")
    elif user_input_int <= number:
        win_label.config(text="Number is too small")
        user_input.delete(0)
    elif user_input_int >= number:
        win_label.config(text="Number is too big")
        user_input.delete(0)
#    else:
#        win_label.config(text="Lose")      
#        user_input.delete(0)
        





#makes window
gamewindow = tk.Tk()

gamewindow.title("Guessing game")
gamewindow.geometry("300x150")

label = tk.Label(gamewindow, text="Guess a number between 1-100")
#calling the VAR "label" then ".pack()" will add it to the window
label.pack()


#allows the user to input their number
user_input = tk.Entry(gamewindow)
user_input.pack()

#button to sumbit your response, "command" is what it runs when clicked
button = tk.Button(gamewindow, text= "submit", command=lambda: get_num(num_wins,num))
button.pack()

num_of_wins = tk.Label(gamewindow, text=f'number of wins:{num_wins}')
num_of_wins.pack()

#empty text to change later
win_label = tk.Label(gamewindow, text="")
win_label.pack()


#loop
gamewindow.mainloop() 