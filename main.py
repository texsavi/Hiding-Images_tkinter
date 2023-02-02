
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

labelOn = True

def hideLabel():
  global labelOn

  if labelOn: # if labelOn is Python shorthand for 'if labelOn == True'
    hello.pack_forget()
    labelOn = False
  else:
    hello.pack()
    labelOn = True

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command = hideLabel) 
button.pack()

tk.mainloop()