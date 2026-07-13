# OBJETO COMO REPRESENTAÇÃO DO MUNDO REAL
class Televisão:
    def __init__(self,canal_min=1, canal_max=11, canal=0):
        self.ligada = False
        self.canal_min = canal_min
        self.canal_mx = canal_max
        self.canal = canal
    
    def canal_aumentar(self):
        if self.ligada:
            if  self.canal - 1 >= self.canal_min:
                    self.canal -= 1
            return f'canal  {self.canal}'
                
    def canal_diminuir(self):
        if self.ligada:
            if  self.canal + 1  <= self.canal_mx:
                    self.canal += 1  
            return f'canal  {self.canal}'       

class ControleRemoto:
    def __init__(self, televisao, pilha):
        self.televisao = televisao
        self.pilha = pilha
    def  ligar(self):
        if self.pilha.consumo(1):
            self.televisao.ligada =  True
            print('a tv esta ligada')
    def desligada(self):
        if self.pilha.consumo(1):
           self.televisao.ligada = False
           print('tv esta desligada')
    
    def canal_mais(self):
        if self.pilha.consumo(1):
           self.televisao.canal_aumentar()
    
    def canalmenos(self):
        if self.pilha.consumo(1):
           self.televisao.canal_diminuir()    
class Pilha:
    def __init__(self, energia=100):
        self.energia = energia
    def consumo(self, consuma):
        if consuma > self.energia:
            consuma -= self.energia
        self.energia -= consuma
        return consuma

tv = Televisão(canal_min=1,canal_max=11)
pilhas = Pilha(5)

controle = ControleRemoto(tv, pilhas)
print(pilhas.energia)

controle.canal_mais()
controle.ligar()

print(tv.canal)
controle.canalmenos()

controle.ligar()
print(tv.canal)   

controle.canalmenos()
controle.desligada()

controle.desligada()
controle.canalmenos()
 
