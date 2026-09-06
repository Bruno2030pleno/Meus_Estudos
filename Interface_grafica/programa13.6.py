# ENTRANDO DADOS
import tkinter as tk
from tkinter import ttk
class Aplicacao(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("conversor")
        self.cria_quadro()
        
    def cria_quadro(self):
        self.quadro = ttk.Frame(self,padding="40 15")
        
        self.l_temperatura = ttk.Label(self.quadro, text="TEMPERATURA DO AMBIENTE")
        self.l_temperatura.pack(pady=1, padx=1)

        self.temperatura = ttk.Entry(self.quadro)
        self.temperatura.pack(padx=8, pady=5, ipadx=5, ipady=5)

        self.botao_CF = ttk.Button(self.quadro, text='celsius para fahrenheit', command=self.celsius_para_fahrenheit)   
        self.botao_CF.pack(padx=8, pady=5) 

        self.botao_FC = ttk.Button(self.quadro, text='fahrenheit para celsius  ', command=self.fahrenheit_para_celsius)
        self.botao_FC.pack()

        self.l_resultado = ttk.Label(self.quadro, text='resultado')
        self.l_resultado.pack(pady=8, padx=8)
        self.quadro.pack(expand=True)
        
    def celsius_para_fahrenheit(self):
        temperatura = float(self.temperatura.get())
        fahrenhit = 9 / 5.0 * temperatura + 32
        self.l_resultado["text"] = f"{fahrenhit:5.2f} \u00B0F"

    def fahrenheit_para_celsius(self):
        temperatura = float(self.temperatura.get())
        celsius = (temperatura - 32) * 5 / 9.0
        self.l_resultado['text'] = f"{celsius:5.2f} \u00B0C"
raiz = Aplicacao()
raiz.mainloop()        

            