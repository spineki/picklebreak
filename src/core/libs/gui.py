import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self):
        self.master = tk.Tk()
        super().__init__(self.master)
        self.master.title("Pickle Break")
        self.hint_list=[]
        self.note_bloc_list=[]
    
    def mainloop(self):
        return self.master.mainloop()
    
    def init_frames(self):
        #Generation of the 3 principales frames
        self.game_frame_hint = tk.Frame(self.master, width=300, height=200, bg="red")
        self.game_frame_note_bloc = tk.Frame(self.master, width=300, height=200, bg="yellow")
        self.game_frame_output = tk.Frame(self.master, bg="black", height=200)
        self.game_frame_hint.grid(row=0, column=0, sticky="nesw")
        self.game_frame_note_bloc.grid(row=0, column=1, sticky='nesw')
        self.game_frame_output.grid(row=1, column=0, columnspan=2, sticky ="nesw")

    def init_note_bloc(self):
        #Generation of the text zone and its scrollbar
        self.myscrollbar= tk.Scrollbar(self.game_frame_input,orient="vertical")
        self.input_test = tk.Text(self.game_frame_input,bg="white", width=50)
        self.myscrollbar.config(command=self.input_test.yview)
        self.input_test.config(yscrollcommand=self.myscrollbar.set)
        self.myscrollbar.pack(side="right",fill="y")
        self.input_test.pack()

        #Creation of the Buttons and linked to their functions
        self.bp_exec = tk.Button(self.game_frame_input,text="Execute",fg='navy')
        self.bp_reset = tk.Button(self.game_frame_input,text="Reset",fg='navy')
        self.bp_exec.pack(side= "bottom",padx=10,pady=10)
        self.bp_reset.pack(side= "bottom",padx=10,pady=10)
    
    def init_hint(self):
        pass

    def init_output(self):
        self.output_text = tk.Text(self.game_frame_output, bg="black", fg="white")
        self.output_text.config(state="disabled")
        self.output_text.pack()
    
    def init_level_note_bloc(self, text_list):
        self.note_bloc_list=[]
        for text in text_list:
            self.note_bloc_list.append(0)

        #Those lines make the principale Text zone unchangeable (if it was not, the user could delete the Text zones generated before inside this Text zone)


    def update_level_note_bloc(self, text_list):

        for i in range(len(text_list)):
            if self.note_bloc_list[i] !=0:
                self.note_bloc_list[i].destroy()
            if text_list[i] != "":
                self.note_bloc_list[i] = tk.Text(self.input_test, bg="tomato", height=2)
                self.note_bloc_list[i].insert("end", text_list[i])
                self.note_bloc_list[i].config(state="disabled")
            else:
                self.note_bloc_list[i] = tk.Text(self.input_test, bg="white", height=2)
                self.note_bloc_list[i].insert("end", "#You can write here")
            self.note_bloc_list[i].pack()
            self.input_test.window_create(index="end", window=self.note_bloc_list[i])
        self.input_test.insert(0.0, "")
        self.input_test.config(state="disabled")
    
    def init_level_hint(self, hint_list):
        self.hint_list=[]
        for hint in hint_list:
            self.hint_list.append(0) 
        
    def update_level_hint(self, hint_list):
        count=0
        for hint in hint_list:
            if self.hint_list[count] != 0:
                self.hint_list[count].destroy()
            if hint[0]=="txt":
                self.hint_list[count]=tk.Label(self.game_frame_hint, text=hint[1])
                self.hint_list[count].pack(fill="both")
            elif hint[0]=="img" and isinstance(hint[1], str):
                img = ImageTk.PhotoImage(Image.open(hint[1]))
                self.hint_list[count]=tk.Label(self.game_frame_hint, image=img)
                self.hint_list[count].image = img
                self.hint_list[count].pack()
            elif hint[0]=="img" and isinstance(hint[1], Image.Image):
                img = ImageTk.PhotoImage(hint[1])
                self.hint_list[count]=tk.Label(self.game_frame_hint, image=img)
                self.hint_list[count].image = img
                self.hint_list[count].pack()
            count+=1

    def display_output(self, texte):
        """
        Affiche un texte dans la zone sortie
        ARGS:
            texte -> string : texte à afficher
        RETURN:
            None
        """
        self.output_text.config(state="normal")
        self.output_text.insert("end", texte)
        self.output_text.config(state="disabled")

    def get_script(self):
        self.output = []
        for i in range(len(self.note_bloc_list)):
            self.output.append(self.note_bloc_list[i].get(0.0, "end"))
        self.output = "\n".join(self.output)
        return self.output
    
    def set_exec_fct(self, function):
        self.bp_exec.config(command= function)

    def set_reset_fct(self, function):
        self.bp_reset.config(command = function)

    def reset_fct(self, hint_list, text_list):
        update_level_hint(hint_list)
        update_level_note_bloc(text_list)