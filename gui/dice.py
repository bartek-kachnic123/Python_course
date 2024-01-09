from random import randint
import tkinter as tk


def roll_dice():
    label["text"] = "{}".format(randint(1, 6))


root = tk.Tk()

root.rowconfigure(0, minsize=300, weight=1)
root.columnconfigure(0, minsize=400, weight=1)
root.columnconfigure(1, minsize=400, weight=1)


button_roll = tk.Button(root, text="Rzuć kostką", command=roll_dice,  font=("Arial", 25), bg="#32a897")

button_roll.grid(row=0, column=0, sticky=tk.NSEW)

label = tk.Label(root, text="",  font=("Arial", 25))
label.grid(row=0, column=1)

root.mainloop()