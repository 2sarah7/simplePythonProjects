import tkinter as tk

# Create a window.
window = tk.Tk()

# Add a label to the window.
label = tk.Label(text="Calculator")
label.pack()

# Add a text box to the window.
text_box = tk.Entry()
text_box.pack()

# Add a button to the window.
button = tk.Button(text="Calculate")
button.pack()

# Bind the button to a function that will perform the calculation.
def calculate():
  # Get the value of the text box.
  value = text_box.get()

  # Perform the calculation.
  result = eval(value)

  # Display the result.
  label.config(text=result)

# Bind the button to the calculate function.
button.config(command=calculate)

# Display the window.
window.mainloop()