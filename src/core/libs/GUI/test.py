import tkinter as tk 

class Application(tk.Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.master.title("Pickle Break")
        self.create_widgets(n)


    def create_widgets(self):

        self.text = tk.StringVar(self.master, "Texte de base")
        self.game_frame_hint = tk.Frame(self.master, width=300, height=300)
        self.game_frame_input = tk.Frame(self.master, width=300, height=300, borderwidth=50)

        self.myscrollbar= tk.Scrollbar(self.game_frame_input,orient="vertical")
        self.input_test = tk.Text(self.game_frame_input,bg="gray")
        self.myscrollbar.config(command=self.input_test.yview)
        self.input_test.config(yscrollcommand=self.myscrollbar.set)
        
        self.text_print = tk.Text(self.input_test, bg="gray")
        self.text_print.insert(0.0, 'first text', ('important'))
        self.text_print.config(state="disabled")
        self.input_test.window_create(index=0.0, window=self.text_print)
        self.input_test.insert(1.0, 'Ecrire ici')

        self.bp_exec = tk.Button(self.game_frame_input,text="Execute",fg='navy',command=self.exec_fct)
        self.bp_exec.pack(side= "bottom",padx=10,pady=10)

        self.myscrollbar.pack(side="right",fill="y")

        self.input_test.pack()
        self.game_frame_hint.pack(side="left")
        self.game_frame_input.pack(side="right")



    def exec_fct(self):
        print("toto")


def Pickle_graphical_grid_init():
    root = tk.Tk()
    root.geometry("800x800")
    app = Application(master=root)
    #app.change_values([[0,1],[1,0]], 2)
    app.mainloop()

Pickle_graphical_grid_init()