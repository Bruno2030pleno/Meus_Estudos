import tkinter as tk
from tkinter import ttk        
# class Teste(tk.Tk):
#     def __init__(self,*args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.lista = []
#         self.title('classe de teste')
#         self.geometry('300x150')
#     def adicionar(self):
#            texto = self.digitar.get()
#            self.lista.append(texto)
#            print(self.lista)
           
#     def botao_1(self):
#         self.quadro = ttk.Frame(self)
#         self.botao = ttk.Button(self.quadro, text='sair', command=self.destroy)
#         self.testo = ttk.Label(self.quadro, text='bem vindo')
#         self.digitar = ttk.Entry(self.quadro)
#         self.botao_2 = ttk.Button(self.quadro, text='adicionar', command=self.adicionar)
    
#         self.botao_2.pack()
#         self.digitar.pack()
#         self.testo.pack()
#         self.botao.pack()
#         self.quadro.pack(expand=True)
# teste = Teste() 
# teste.botao_1()       
# teste.mainloop()

# raiz = tk.Tk()
# raiz.title('teste')
# raiz.geometry('400x400')
# raiz.config(bg='black')
# raiz.mainloop()

class Interface_grafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('teste')
        self.geometry('1920x1080')
        self.config(bg='black')
    def botoes(self):
        self.quadro = ttk.Frame(self)   
face = Interface_grafica()
face.mainloop()