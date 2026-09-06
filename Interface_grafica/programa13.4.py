# ADICIONADO CONTADORES
import tkinter as tk
from tkinter import ttk

class Contador(tk.Frame):
    def __init__(self,numero, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numero = numero
        self.contador = 0
        self.label = ttk.Label(text=self.formata_contador(self.numero, self.contador))
        self.label.pack()
        self.botao = ttk.Button(text=f"adiciona ao contador {self.numero}", command=self.conta)
        self.botao.pack()
        self.pack()
    def formata_contador(self, contador, valor):
        return f"contador {contador}: {valor}"
    def conta(self):
        self.contador += 1
        self.label['text'] = self.formata_contador(self.numero, self.contador)

class Aplicativo(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contadores = []
        self.cria_quadro()
    def cria_quadro(self):
        self.quadro = ttk.Frame(self)
        self.botao = ttk.Button(text="adiciona ao contador", command=self.adiciona_contador)
        self.botao.pack()
        self.quadro.pack(expand=True)
    def adiciona_contador(self):
        novo_contador = Contador(len(self.contadores) + 1, master=self.quadro) 
        self.contadores.append(novo_contador)   
raiz = Aplicativo()
raiz.mainloop()
