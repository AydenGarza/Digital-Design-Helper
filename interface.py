import tkinter as tk
import truthtablelogic as truth

#configuring main window
main_window = tk.Tk()
main_window.geometry("600x750")
main_window.title("Digital Design Helper")

#initializing menu bar
mode_bar = tk.Menu(main_window)

#adding menu bar options
mode_bar.add_command(label="Truth Table Generator")
mode_bar.add_command(label="Karnaugh Map Helper")
mode_bar.add_command(label="Sequential Circuit Analysis")
mode_bar.add_command(label="Sequential Circuit Synthesis")

#adding menu bar to main window
main_window.config(menu=mode_bar)

#creating frame that will contain everything
main_frame = tk.Frame(main_window, bg="lightgreen")
main_frame.pack(fill="both", expand=True)

#creating the frame that will contain the truth table
truth_table_container = tk.Frame(main_frame, bg="lightblue")
truth_table_container.pack(fill="x")

#creating the truth table
for x in range(0,4):
    truth_table_container.columnconfigure(x,weight=1)
    test_label = tk.Label(truth_table_container, text=f'{x}',padx=10,pady=10)
    test_label.grid(row=0,column=x,sticky="we",pady=10,padx=10)

#creating frame to contain prompt into
prompt_frame = tk.Frame(main_frame,bg="yellow")
prompt_frame.pack(fill="x", pady=10)

#text box and prompt for user to input their expression
user_instructions = tk.Label(prompt_frame,text="Enter a Boolean expression:")
user_instructions.grid(sticky="w")


main_window.mainloop()