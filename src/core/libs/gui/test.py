import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.master.title("Pickle Break")
        self.create_widgets()


    def create_widgets(self):

        self.game_frame_hint = tk.Frame(self.master, width=300, height=200, bg="red")
        self.game_frame_input = tk.Frame(self.master, width=300, height=200, bg="yellow")
        self.game_frame_output = tk.Frame(self.master, bg="black", height=200)

        self.myscrollbar= tk.Scrollbar(self.game_frame_input,orient="vertical")
        self.input_test = tk.Text(self.game_frame_input,bg="white", width=50)
        self.myscrollbar.config(command=self.input_test.yview)
        self.input_test.config(yscrollcommand=self.myscrollbar.set)
        
        self.output_text = tk.Text(self.game_frame_output, bg="black", fg="white")
        self.text_print = tk.Text(self.input_test, bg="white", height=2)
        self.text_print.insert(0.0, 'Texte immuable', ('important'))
        self.text_print.config(state="disabled")
        self.text_print.pack()
        self.input_test.window_create(index=0.0, window=self.text_print)
        self.input_test.insert(2.0, "#votre vode ici")

        self.bp_exec = tk.Button(self.game_frame_input,text="Execute",fg='navy',command=self.exec_fct)
        self.bp_exec.pack(side= "bottom",padx=10,pady=10)

        self.myscrollbar.pack(side="right",fill="y")

        self.input_test.pack()
        self.output_text.pack()

        img = ImageTk.PhotoImage(Image.open("./src/res/pickle.png"))
        self.image=tk.Label(self.game_frame_hint, image=img)
        self.image.image = img
        self.image.pack()

        self.game_frame_hint.grid(row=0, column=0, sticky="nesw")
        self.game_frame_input.grid(row=0, column=1, sticky='nesw')
        self.game_frame_output.grid(row=1, column=0, columnspan=2, sticky ="nesw")
        #self.game_frame_hint.pack(side="left")
        #self.game_frame_input.pack(side="right")
        #self.game_frame_output.pack(side="bottom")

    def get_input(self):
        """
        Récupère le texte entré par le joueur
        ARGS : 
            None
        RETURN:
            texte -> string : texte entrée par l'utilisateur dans le champ bloc-note
        """
        return self.input_test.get("1.0","end")
    
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
    
    def display_hint(self, list_to_display):
        self.image = None
        for thing in list_to_display:
            if thing[0]=="txt":
                pass #à faire
            elif thing[0]=="img" and isinstance(thing[1], str):
                img = ImageTk.PhotoImage(Image.open("./src/res/pickle.png"))
                self.image=tk.Label(self.game_frame_hint, image=img)
                self.image.image = img
                self.image.pack()
            elif thing[0]=="img" and isinstance(thing[1], Image.Image):
                img = ImageTk.PhotoImage(thing[1])
                self.image=tk.Label(self.game_frame_hint, image=img)
                self.image.image = img
                self.image.pack()


    def exec_fct(self):
        """
        Fonction qui s'éxécute quand le joueur clique sur le bouton execute
        """
        self.output_text.config(state="normal")#débloque la zone de sortie pour pouvoir afficher

        self.output_text.insert("end", self.input_test.get("1.0","end"))#exemple, à modifier

        self.output_text.config(state="disabled")#rebloque la zonne de sortie pour ne pas que le joueur puisse écrire dans la sortie



def Pickle_graphical_grid_init():
    root = tk.Tk()
    root.geometry("800x800")
    app = Application(master=root)
    #app.change_values([[0,1],[1,0]], 2)
    app.mainloop()

if __name__ == '__main__':

    Pickle_graphical_grid_init()