import tkinter as tk 

class Application(tk.Frame):
    def __init__(self, n, master=None):

        super().__init__(master)
        self.master = master
        self.master.title("Pickle Break")
        self.create_widgets(n)


    def create_widgets(self, n):

        """
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", bg="blue",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        """

        self.game_frame_hint = tk.Frame(self.master, width=300, height=300)
        self.game_frame_input = tk.Frame(self.master, width=300, height=300, borderwidth=50)

        self.myscrollbar= tk.Scrollbar(self.game_frame_input,orient="vertical")
        self.canvas_test = tk.Canvas(self.game_frame_input,yscrollcommand=self.myscrollbar.set, width= 1200, height=1200, bg="gray")

        self.myscrollbar.config(command=self.canvas_test.yview)
        self.myscrollbar.pack(side="right",fill="y")
        self.canvas_test.config(scrollregion=self.canvas_test.bbox("all"))

        self.canvas_test.pack()
        self.game_frame_hint.pack(side="left")
        self.game_frame_input.pack(side="right")



        """
        self.tiles_grid = [[None]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                self.tiles_grid[i][j] = tk.Label(self.game_frame)
                self.tiles_grid[i][j]["text"] = str(i) + str(j)
                self.tiles_grid[i][j].grid(row = i, column = j)
                self.tiles_grid[i][j].configure(bg="gray")
                self.tiles_grid[i][j].configure(width=50//n)
                #print(self.master.winfo_screenwidth())
                self.tiles_grid[i][j].configure(height=50//n)
        #self.background.pack()
        self.game_frame.pack()
        """


    def change_values(self, data, n):
        for i in range(n):
            for j in range(n):
                self.affiche[i][j]["text"] = str(data[i][j])  

    def say_hi(self):
        print("hi there, everyone!")
    
    """
    def change_hi (self, txt):
        self.hi_there["text"] = txt
        self.quit.configure(command = lambda : print("hi"))
    """

def Pickle_graphical_grid_init():
    root = tk.Tk()
    root.geometry("800x800")
    app = Application(4, master=root)
    #app.change_values([[0,1],[1,0]], 2)
    app.mainloop()

Pickle_graphical_grid_init()