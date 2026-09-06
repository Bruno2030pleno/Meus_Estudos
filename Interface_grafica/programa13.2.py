# CONTANDO CLIQUES
import tkinter as tk
from tkinter import ttk
contador_1 = 0
contador_2 = 0

def formata_contador(contador, valor):
    return f"contador {contador}: {valor}"

def conta_1():
    global contador_1, l_contador_1
    contador_1 += 1
    l_contador_1['text'] = formata_contador(1, contador_1)

def conta_2():
    global contador_2, l_contador_2
    contador_2 += 1
    l_contador_2['text'] = formata_contador(2, contador_2)

tela = tk.Tk()
tela.title('contadores')
tela.geometry('400x200')
tela.config(bg='orange')

quadro = ttk.Frame(tela)

botao = ttk.Button(quadro, text='sair', command=tela.destroy)
botao.pack()


l_contador_1 = ttk.Label(quadro, text=formata_contador(1, contador_1))
l_contador_1.pack()

botao_1 = ttk.Button(quadro, text='adiciona ao contador 1', command=conta_1)
botao_1.pack()

l_contador_2 = ttk.Label(quadro, text=formata_contador(2, contador_2))
l_contador_2.pack()

botao_2 = ttk.Button(quadro, text='adiciona ao contador 2', command=conta_2)
botao_2.pack()

quadro.pack(expand=True)
tela.mainloop()