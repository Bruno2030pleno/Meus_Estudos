# USANDO CLASSES 
import tkinter as tk
from tkinter import ttk

class Aplicativo(tk.Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador_1 = 0
        self.contador_2 = 0
        self.title('Contadores')
        self.geometry("400x300")
        self.cria_quadro()
        self.config(bg='orange')
    def cria_quadro(self):
        self.quadro = ttk.Frame(self)
        self.l_contador_1 = ttk.Label(self.quadro, text=self.formata_contador(1, self.contador_1))
        self.l_contador_1.pack()
        self.botao = ttk.Button(self.quadro, text='adiciona ao contador 1', command=self.conta_1)
        self.botao.pack()

        self.l_contador_2 = ttk.Label(self.quadro, text=self.formata_contador(2, self.contador_2))
        self.l_contador_2.pack()
        self.botao_2 = ttk.Button(self.quadro, text='adiciona ao contador 2', command=self.conta_2)
        self.botao_2.pack()
        self.quadro.pack(expand=True)
    def formata_contador(self, contador, valor):
        return f"Contador {contador}: {valor}"
    def conta_1(self):
        self.contador_1 += 1
        self.l_contador_1['text'] = self.formata_contador(1, self.contador_1)

    def conta_2(self):
        self.contador_2 += 1 
        self.l_contador_2['text'] = self.formata_contador(2, self.contador_2)
raiz = Aplicativo()
raiz.mainloop()               
