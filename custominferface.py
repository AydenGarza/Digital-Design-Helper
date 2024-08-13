import customtkinter as ctk
import tkinter
import truthtablelogic as tt




#heirarchy of widgets goes
    
#main_window
    #mode_bar, drop down menu that lets you select which program function you want
    #user_prompt, just a label with the text ''enter a boolean expression:''
    #user_input, the entry where the user types in their boolean expression
    #process_input, the button that processes the input in the user_input entry
    #truth_table_container, the frame where the truht table is generated in
        #all the truth table cells that are generated by the generateTT function

def runApp():
        #deletes all widgets in a frame
    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    #function that fills the truth table container with the actual truth table
    def generateTT():
        clear_frame(truth_table_container)
        user_input_value = user_input.get()
        
        user_boolean_function = tt.booleanFunction(user_input_value)

        user_function_tt = user_boolean_function.truthTable
        
        #going through every element of the truth table array user_function_tt and placing it via grid method into the truth table container frame
        for x in range(0, len(user_function_tt)):

            truth_table_container.columnconfigure(x ,weight = 1)

            for y in range(0,len(user_function_tt[x])):
                truth_table_cell = ctk.CTkLabel(truth_table_container, text=f'{user_function_tt[x][y]}')
                truth_table_cell.grid(row = x, column = y)
        #clears user input once button is pressed
        user_input.delete(0,tkinter.END)
        
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