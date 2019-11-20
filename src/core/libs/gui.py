import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self):
        self.master = tk.Tk()#Generate the main window
        super().__init__(self.master)#Fill the window with a frame
        self.master.title("Pickle Break")#Put a title to te window
        self.hint_list=[]#list of hint panel widget
        self.notepad_list=[]#list of notepad panel widget
        self.turbo_init_frame()#panels initialization, shared by every level
    
    def mainloop(self):
        return self.master.mainloop()
    
# TURBO FUNCTIONS *********************************************************************************
    def turbo_init_frame(self):
        """
        Runs the panels initialization (creates element shared by every level)
        ARGS:
            None
        RETURN:
            None
        """
        self.init_frames()
        self.init_notepad()
        self.init_hint()
        self.init_output()

    def turbo_init_level(self, hint_list,notepad_list):
        """
        Runs the level initialization
        ARGS:
            notepad_list -> list of string : "" for a mutable text zone and "text_to_print" to display the string in a immutable text zone
            hint_list -> list of tuples : objects to display for the level. Each tuple has this shape : (type, object) where type = "txt" or "img" and object = image address or image object (from PIL) or text (string) to display
        RETURN:
            None
        """
        self.init_level_hint(hint_list)
        self.init_level_notepad(notepad_list)
        self.init_level_output()

    def turbo_update_level(self, hint_list,notepad_list):
        """
        Updates the level panels
        ARGS:
            notepad_list -> list of string : "" for a mutable text zone and "text_to_print" to display the string in a immutable text zone
            hint_list -> list of tuples : objects to display for the level. Each tuple has this shape : (type, object) where type = "txt" or "img" and object = image address or image object (from PIL) or text (string) to display
        RETURN:
            None
        """
        self.update_level_hint(hint_list)
        self.update_level_notepad(notepad_list)

# GLOBAL INIT FUNCTIONS ***************************************************************************
    def init_frames(self):
        """
        Generation of the three main panels
        ARGS:
            None
        RETURN:
            None
        """
        self.game_frame_hint = tk.Frame(self.master, width=300, height=200, bg="red")
        self.game_frame_notepad = tk.Frame(self.master, width=300, height=200, bg="yellow")
        self.game_frame_output = tk.Frame(self.master, bg="black", height=200)
        self.game_frame_hint.grid(row=0, column=0, sticky="nesw")
        self.game_frame_notepad.grid(row=0, column=1, sticky='nesw')
        self.game_frame_output.grid(row=1, column=0, columnspan=2, sticky ="nesw")

    def init_notepad(self):
        """
        Generation of the master text zone (will contains the script text zones) and the scrollbar for the notepad panel
        Creation of the buttons
        ARGS:
            None
        RETURN:
            None
        """
        self.notepad_scrollbar= tk.Scrollbar(self.game_frame_notepad,orient="vertical")
        self.master_text = tk.Text(self.game_frame_notepad,bg="white", width=50)
        self.notepad_scrollbar.config(command=self.master_text.yview)
        self.master_text.config(yscrollcommand=self.notepad_scrollbar.set)
        self.notepad_scrollbar.pack(side="right",fill="y")
        self.master_text.pack()

        self.btn_exec = tk.Button(self.game_frame_notepad,text="Execute",fg='navy')
        self.btn_reset = tk.Button(self.game_frame_notepad,text="Reset",fg='navy')
        self.btn_exec.pack(side= "bottom",padx=10,pady=10)
        self.btn_reset.pack(side= "bottom",padx=10,pady=10)
    
    def init_hint(self):
        """
        Do nothing
        ARGS:
            None
        RETURN:
            None
        """
        pass

    def init_output(self):
        """
        Generation of the output text zone
        ARGS:
            None
        RETURN:
            None
        """
        self.output_text = tk.Text(self.game_frame_output, bg="black", fg="white")
        self.output_text.config(state="disabled")
        self.output_text.pack()

# NOTEPAD LEVEL FUNCTIONS ************************************************************************* 
    def init_level_notepad(self, notepad_list):
        """
        Initialization of the notepad panel for a level:
            - Destroy old widgets
            - Prepare new ones
        ARGS:
            notepad_list -> list of string : "" for a mutable text zone and "text_to_print" to display the string in a immutable text zone
        RETURN:
            None
        """
        if self.notepad_list != []:
            for widget in self.notepad_list:
                widget.destroy()
            self.notepad_list=[]
        for text in notepad_list:
            self.notepad_list.append(0)

    def update_level_notepad(self, notepad_list):
        """
        Update and display text zones in a level
        ARGS:
            notepad_list -> list of string : "" for a mutable text zone and "text_to_print" to display the string in a immutable text zone
        RETURN:
            None
        """
        for i in range(len(notepad_list)):
            if self.notepad_list[i] !=0:
                self.notepad_list[i].destroy()
            if notepad_list[i] != "":
                self.notepad_list[i] = tk.Text(self.master_text, bg="tomato", fg="white", height=2)
                self.notepad_list[i].insert("end", notepad_list[i])
                self.notepad_list[i].config(state="disabled")
            elif self.notepad_list[i] == 0:
                self.notepad_list[i] = tk.Text(self.master_text, bg="white", fg="black", height=2)
                self.notepad_list[i].insert("end", "")
            self.notepad_list[i].pack()
            self.master_text.window_create(index="end", window=self.notepad_list[i])
            self.master_text.insert(0.0, "")
            self.master_text.config(state="disabled")

# HINT LEVEL FUNCTIONS **************************************************************************** 
    def init_level_hint(self, hint_list):
        """
        Initialization of the hint panel for a level:
            - Destroy old widgets
            - Prepare new ones
        ARGS:
            hint_list -> list of tuples : objects to display for the level. Each tuple has this shape : (type, object) where type = "txt" or "img" and object = image address or image object (from PIL) or text (string) to display
        RETURN:
            None
        """
        if self.hint_list != []:
            for widget in self.hint_list:
                widget.destroy()
            self.hint_list=[]
        self.hint_list=[]
        for hint in hint_list:
            self.hint_list.append(0) 
        
    def update_level_hint(self, hint_list):
        """
        Update and display level objects in the hint panel
        ARGS:
            hint_list -> list of tuples : objects to display for the level. Each tuple has this shape : (type, object) where type = "txt" or "img" and object = image address or image object (from PIL) or text (string) to display
        RETURN:
            None
        """
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

# OUTPUT LEVEL FUNCTIONS **************************************************************************
    def init_level_output(self):
        """
        Initialization of the output panel for a level by erasing previous output
        ARGS:
            None
        RETURN:
            None
        """
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.config(state="disabled")

# MISCELLANEOUS ***********************************************************************************
    def display_output(self, text):
        """
        Display text in the output panel
        ARGS:
            text -> string : texte to print
        RETURN:
            None
        """
        self.output_text.config(state="normal")
        self.output_text.insert("end", text)
        self.output_text.config(state="disabled")

    def get_script(self):
        """
        Get the script written by the player in the notepad zone
        ARGS:
            None
        RETURN:
            script -> string : script
        """
        self.script = []
        for i in range(len(self.notepad_list)):
            self.script.append(self.notepad_list[i].get(0.0, "end"))
        self.script = "\n".join(self.script)
        return self.script
    
    def set_exec_fct(self, function):
        """
        Bind a fonction to the "Execute" button
        ARGS:
            function -> function : function to bind
        RETURN:
            None
        """
        self.btn_exec.config(command= function)

    def set_reset_fct(self, function):
        """
        Bind a fonction ton the "Reset" button
        ARGS:
            function -> function : function to bind
        RETURN:
            None
        """
        self.btn_reset.config(command = function)






#Test part

def test_Application(list_notepad_list, list_hint_list):
    root = Application()
    root.turbo_init_level(list_hint_list, list_notepad_list)
    root.turbo_update_level(list_hint_list, list_notepad_list)

    def test_exec():
        root.turbo_init_level(list_hint_list2, list_notepad_list2)
        root.turbo_update_level(list_hint_list2, list_notepad_list2)
    
    def test_reset():
        root.display_output("Youpi")
    
    root.set_reset_fct(test_reset)
    root.set_exec_fct(test_exec)
    root.mainloop()

if __name__ == '__main__':
    list_notepad_list = ["Coucou, c'est el level1","","Tu peux écrire?", "", "", "", "", "", ""]
    list_hint_list = [("txt","Salut gérard"), ("img","./src/res/pickle.png")]
    list_notepad_list2 = ["Level2", ""]
    list_hint_list2 = [("img","./src/res/pickle_in_prison.png")]
    test_Application(list_notepad_list, list_hint_list)