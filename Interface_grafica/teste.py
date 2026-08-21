import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz.title('minha primeiro vez')
raiz.geometry('400x150')
quadro = ttk.Frame(raiz)
texto = ttk.Label(quadro,text='bom dia bruno')
texto.pack()

botao = ttk.Button(quadro, text='sair', command=raiz.destroy)
botao.pack()
quadro.pack(expand=True)
raiz.mainloop()