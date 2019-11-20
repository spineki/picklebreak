import tkinter as tk 

class Application(tk.Frame):
    def __init__(self, text, master=None):

        super().__init__(master)
        self.master = master
        self.master.title("Pickle Break")
        self.init_frames()
        self.init_note_bloc()        
        self.init_level(text)


    def init_frames(self):

        #Generation of the 3 principales frames
        self.game_frame_hint = tk.Frame(self.master, width=300, height=200, bg="red")
        self.game_frame_input = tk.Frame(self.master, width=300, height=200, bg="yellow")
        self.game_frame_output = tk.Frame(self.master, bg="black", height=200)

    def init_note_bloc(self):
        #Generation of the text zone and its scrollbar
        self.myscrollbar= tk.Scrollbar(self.game_frame_input,orient="vertical")
        self.input_test = tk.Text(self.game_frame_input,bg="white", width=50)
        self.myscrollbar.config(command=self.input_test.yview)
        self.input_test.config(yscrollcommand=self.myscrollbar.set)
        self.myscrollbar.pack(side="right",fill="y")

        #Generate the Frames in a grid in ordre to have a good disposition
        self.game_frame_hint.grid(row=0, column=0, sticky="nesw")
        self.game_frame_input.grid(row=0, column=1, sticky='nesw')
        self.game_frame_output.grid(row=1, column=0, columnspan=2, sticky ="nesw")
        self.input_test.pack()

    def init_level(self, text):
        #Use of the display_text function which will add in the Text widget, Text widgets with the right organisation
        self.display_text(text)

        #Those lines make the principale Text zone unchangeable (if it was not, the user could delete the Text zones generated before inside this Text zone)
        self.input_test.insert(0.0, "")
        self.input_test.config(state="disabled")

        #Creation of the Buttons and linked to their functions
        self.bp_exec = tk.Button(self.game_frame_input,text="Execute",fg='navy')
        self.bp_reset = tk.Button(self.game_frame_input,text="Reset",fg='navy',command=self.reset_fct)
        self.bp_exec.pack(side= "bottom",padx=10,pady=10)
        self.bp_reset.pack(side= "bottom",padx=10,pady=10)
       
        
    def display_text(self, text):
        """
        This function display the texts zones where the informations are printed and where the user can write
        ARGS:
        text: str: Contains the informations which will be printed (nb: A string empty (ie "") represent a zone where the user can write)
        RETURNS:
        None
        """
        self.text_zones = [" "]*len(text)
        for i in range(len(text)):
            
            if text[i] != "":
                self.text_zones[i] = tk.Text(self.input_test, bg="tomato", height=2)
                self.text_zones[i].insert("end", text[i])
                self.text_zones[i].config(state="disabled")
                
            else:
                self.text_zones[i] = tk.Text(self.input_test, bg="white", height=2)
                self.text_zones[i].insert("end", "#You can write here")

            self.text_zones[i].pack()
            self.input_test.window_create(index="end", window=self.text_zones[i])
        return(self.text_zones)

    def get_code(self):
        self.output = []
        for i in range(len(self.text_zones)):
            self.output.append(self.text_zones[i].get(0.0, "end"))
        self.output = "\n".join(self.output)
        return self.output
    
    def set_exec_fct(self, function):
        self.bp_exec.config(command= function)

    def set_reset_fct(self, function):
        self.bp_reset.config(command = function)

    def reset_fct(self):
        for widget in self.game_frame_output.winfo_children():
            widget.destroy()
        for widget in self.game_frame_input.winfo_children():
            widget.destroy()
        for widget in self.game_frame_hint.winfo_children():
            widget.destroy()
        self.init_frames()
        self.init_note_bloc()        
        self.init_level(text)


def Pickle_graphical_grid_init(text):
    root = tk.Tk()
    root.geometry("800x800")
    app = Application(text ,master=root)
    #app.change_values([[0,1],[1,0]], 2)
    app.mainloop()
    
text = ["Coucou","","Tu peux écrire?", "", "", "", "", "", ""]
Pickle_graphical_grid_init(text)