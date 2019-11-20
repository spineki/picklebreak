import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self):
        self.master = tk.Tk()
        super().__init__(self.master)
        self.master.title("Pickle Break")
        self.hint_list=[]
        self.notepad_list=[]
        self.turbo_init_frame()
    
    def mainloop(self):
        return self.master.mainloop()
    
    def turbo_init_frame(self):
        #Initialisation of all the frames
        self.init_frames()
        self.init_notepad()
        self.init_hint()
        self.init_output()

    def turbo_init_level(self, hint_list,notepad_list):
        self.init_level_hint(hint_list)
        self.init_level_notepad(notepad_list)

    def turbo_update_level(self, hint_list,notepad_list):
        self.update_level_hint(hint_list)
        self.update_level_notepad(notepad_list)

    def init_frames(self):
        #Generation of the 3 principales frames
        self.game_frame_hint = tk.Frame(self.master, width=300, height=200, bg="red")
        self.game_frame_notepad = tk.Frame(self.master, width=300, height=200, bg="yellow")
        self.game_frame_output = tk.Frame(self.master, bg="black", height=200)
        self.game_frame_hint.grid(row=0, column=0, sticky="nesw")
        self.game_frame_notepad.grid(row=0, column=1, sticky='nesw')
        self.game_frame_output.grid(row=1, column=0, columnspan=2, sticky ="nesw")

    def init_notepad(self):
        #Generation of the text zone and its scrollbar
        self.notepad_scrollbar= tk.Scrollbar(self.game_frame_notepad,orient="vertical")
        self.master_text = tk.Text(self.game_frame_notepad,bg="white", width=50)
        self.notepad_scrollbar.config(command=self.master_text.yview)
        self.master_text.config(yscrollcommand=self.notepad_scrollbar.set)
        self.notepad_scrollbar.pack(side="right",fill="y")
        self.master_text.pack()

        #Creation of the Buttons and linked to their functions
        self.btn_exec = tk.Button(self.game_frame_notepad,text="Execute",fg='navy')
        self.btn_reset = tk.Button(self.game_frame_notepad,text="Reset",fg='navy')
        self.btn_exec.pack(side= "bottom",padx=10,pady=10)
        self.btn_reset.pack(side= "bottom",padx=10,pady=10)
    
    def init_hint(self):
        pass

    def init_output(self):
        self.output_text = tk.Text(self.game_frame_output, bg="black", fg="white")
        self.output_text.config(state="disabled")
        self.output_text.pack()
    
    def init_level_notepad(self, notepad_list):
        if self.notepad_list != []:
            for widget in self.notepad_list:
                widget.destroy()
            self.notepad_list=[]
        for text in notepad_list:
            self.notepad_list.append(0)

    def update_level_notepad(self, notepad_list):
        """
        This function initiate the text zones in the text area at the right format  
        """
        
        for i in range(len(notepad_list)):
            if self.notepad_list[i] !=0:
                self.notepad_list[i].destroy()
            if notepad_list[i] != "":
                self.notepad_list[i] = tk.Text(self.master_text, bg="tomato", height=2)
                self.notepad_list[i].insert("end", notepad_list[i])
                self.notepad_list[i].config(state="disabled")
            elif self.notepad_list[i] == 0:
                self.notepad_list[i] = tk.Text(self.master_text, bg="white", height=2)
                self.notepad_list[i].insert("end", "")
            self.notepad_list[i].pack()
            self.master_text.window_create(index="end", window=self.notepad_list[i])
            self.master_text.insert(0.0, "")
            self.master_text.config(state="disabled")
    
    def init_level_hint(self, hint_list):
        if self.hint_list != []:
            for widget in self.hint_list:
                widget.destroy()
            self.hint_list=[]
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
        for i in range(len(self.notepad_list)):
            self.output.append(self.notepad_list[i].get(0.0, "end"))
        self.output = "\n".join(self.output)
        return self.output
    
    def set_exec_fct(self, function):
        self.btn_exec.config(command= function)

    def set_reset_fct(self, function):
        self.btn_reset.config(command = function)

    def reset_fct(self, hint_list, notepad_list):
        self.update_level_hint(hint_list)
        self.update_level_notepad(notepad_list)





#Partie test

def test_Application(list_notepad_list, list_hint_list):
    root = Application()
    root.turbo_init_level(list_hint_list, list_notepad_list)
    root.turbo_update_level(list_hint_list, list_notepad_list)

    def test_exec():
        root.turbo_init_level(list_hint_list2, list_notepad_list2)
        root.turbo_update_level(list_hint_list2, list_notepad_list2)
    
    root.set_exec_fct(test_exec)
    root.mainloop()

if __name__ == '__main__':
    list_notepad_list = ["Coucou, c'est el level1","","Tu peux écrire?", "", "", "", "", "", ""]
    list_hint_list = [("txt","Salut gérard"), ("img","./src/res/pickle.png")]
    list_notepad_list2 = ["Level2", ""]
    list_hint_list2 = [("img","./src/res/pickle_in_prison.png")]
    test_Application(list_notepad_list, list_hint_list)