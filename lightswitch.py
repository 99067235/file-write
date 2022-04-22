import tkinter as tk
import os
window = tk.Tk()


file = open('actions.log', 'a')




# schijf hier tussen je code
window.configure(bg="black")

def input():
    if(button['text']=='light is off'):
        button.config(text="light is on")
        window.configure(bg="yellow")
        file.write('light is off\n')
    else:
        button.config(text="light is off")
        window.configure(bg="black")
        file.write('light is on\n')



# schijf hier tussen je code

button = tk.Button(text='light is off', bg="white", fg="black", command= input)
button.pack(pady = 100, padx = 100)


window.mainloop()
file.close()