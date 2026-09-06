# leyout do aplicativo de desenho
import tkinter as tk
from tkinter import ttk
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quadro = ttk.Frame(self)
        self.cria_barra()
        self.cria_area_de_desenho()
        self.title("Desenho")
        self.geometry("800x600")
        self.config(bg='black')
        self.quadro.pack(expand=True, fill='both') 

    def cria_area_de_desenho(self):
        self.trabalho = ttk.Frame(self.quadro, height=600)
        self.trabalho.grid(column=1, row=0, sticky=tk.NSEW)
        self.quadro.grid_columnconfigure(1, weight=1)
        self.quadro.grid_rowconfigure(0, weight=1)
        self.canvas = tk.Canvas(self.trabalho, background='gray') 
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Motion>", self.mause_move)
        self.cordenadas = ttk.Label(self.trabalho, text="mova o mause")
        self.cordenadas.pack(ipadx=10, ipady=10)
    def cria_barra(self):
        self.barra = ttk.Frame(self.quadro, width=100, height=600)
        self.barra.grid(column=0, row=0, sticky=tk.NS + tk.SW)
    def mause_move(self, event):
        self.cordenadas['text'] = f"mause x={event.x} y={event.y}"
a = App()
a.mainloop()            


    