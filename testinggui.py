import tkinter as tk

def on_tearoff():
    print("Menu was torn off!")

root = tk.Tk()

menu = tk.Menu(root, tearoff=1)
menu.add_command(label="Option 1", command=lambda: print("Option 1 clicked"))
menu.add_command(label="Option 2", command=lambda: print("Option 2 clicked"))
menu.add_separator()
menu.add_command(label="Tear off", command=on_tearoff)

# Attach the menu to the root window
root.config(menu=menu)

root.mainloop()