import customtkinter as ctk

import truthtablelogic as tt

main_window = ctk.CTk()
main_window.geometry("600x750")
main_window.title("Digital Design Helper")

menu_options = ["Truth Table Generator", "Karnaugh Map Helper", "Sequential Circuit Analysis", "Sequential Circuit Synthesis"]
selected_value = ctk.StringVar(value = menu_options[0])
mode_bar = ctk.CTkOptionMenu(master = main_window, values = menu_options)
mode_bar.pack()

user_prompt = ctk.CTkLabel(master = main_window,text="Enter a Boolean expression:")
user_prompt.pack()

user_input_box = ctk.CTkInputDialog(master = main_window, text="as")

main_window.mainloop()