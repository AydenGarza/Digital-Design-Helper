import customtkinter as ctk

import truthtablelogic as tt

def generateTT():

    user_input_value = user_input.get()

    user_boolean_function = tt.booleanFunction(user_input_value)

    user_function_tt = user_boolean_function.truthTable

    for x in range(0, len(user_function_tt)):

        truth_table_container.columnconfigure(x,weight = 1)

        for y in range(0,len(user_function_tt[x])):
            truth_table_cell = ctk.CTkLabel(truth_table_container, text=f'{user_function_tt[x][y]}')
            truth_table_cell.grid(row = x, column = y)

main_window = ctk.CTk()
main_window.geometry("600x750")
main_window.title("Digital Design Helper")

menu_options = ["Truth Table Generator", "Karnaugh Map Helper", "Sequential Circuit Analysis", "Sequential Circuit Synthesis"]
selected_value = ctk.StringVar(value = menu_options[0])
mode_bar = ctk.CTkOptionMenu(master = main_window, values = menu_options)
mode_bar.pack()

user_prompt = ctk.CTkLabel(master = main_window,text="Enter a Boolean expression:")
user_prompt.pack()

user_input = ctk.CTkEntry(master = main_window)
user_input.pack()

process_input = ctk.CTkButton(master = main_window, command=generateTT, text="Generate Truth Table")
process_input.pack()

truth_table_container = ctk.CTkFrame(master = main_window)
truth_table_container.pack(fill="x", padx=10)


main_window.mainloop()