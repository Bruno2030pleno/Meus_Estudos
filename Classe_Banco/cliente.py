from collections import UserList
from functools import total_ordering
# class Cliente:
#     def __init__(self, nome, telefone):
#         self.nome = nome
#         self.telefone = telefone
# class Conta:
#     def __init__(self, clientes, numero, saldo=0):
#         self.clientes = clientes
#         self.numero = numero
#         self.saldo = saldo
#         self.operacoes = []
#     def resumo(self):
#         print(f'CC numero {self.numero}, saldo R${self.saldo:10.2f}')
#         for dados in self.clientes:
#             print(f'nome {dados.nome} telefone {dados.telefone}')
#     def saque(self, valor):
#         if self.posso_sacar(valor):
#             self.saldo -= valor
#             self.operacoes.append(['SAQUE', valor])
#             print('saque realizado com sucesso')
#             return True
#         else:
#             print('SALDO INSUFICIANTE!!')  
#             return False 
#     def deposito(self, valor):
#         self.saldo += valor
#         print(f'valor depositado R${valor:10.2f}')
#         self.operacoes.append(['DESPOSITO', valor])
#     def extrato(self):
#         print(f'extrato CC N {self.numero}\n')
        
#         for operacao in self.operacoes:
#             print(f"{operacao[0]:.10s} {operacao[1]:10.2f}")
#         print(f'\nsaldo R${self.saldo:10.2f}') 
#     def posso_sacar(self, valor):
#         return self.saldo >= valor 
        
# class Banco:
#     def __init__(self, nome):
#         self.nome = nome
#         self.contas = []
    
#     def abre_conta(self, conta):
#         self.contas.append(conta)
    
#     def lista_contas(self):
#         for c in self.contas:
#             c.resumo()
# class ContaEspecial(Conta):
#     def __init__(self, clientes, numero, saldo=0, limite=0):
#         super().__init__(clientes, numero, saldo)
#         self.limite = limite
   
#     def extrato(self):
#         super().extrato()
#         print(f'seu limite disponivel {self.limite:.2f}')
#         print(f'valor disponivel para saque, {self.saldo + self.limite }')
#     def posso_sacar(self, valor):
#         return self.saldo + self.limite >= valor
# from collections import UserList

# class ListaUnica(UserList):
#     def __init__(self, elem_classe):
#         # Inicia a UserList, que automaticamente cria a lista 'self.data'
#         super().__init__()
#         self.elem_classe = elem_classe
    
#     def verifica_tipo(self, elem):
#         if not isinstance(elem, self.elem_classe):
#             raise TypeError('TIPO INVALIDO!!!!')
#     def extend(self, nova_lista):
#         for elemento in nova_lista:
#             self.append(elemento) 
#     # Sobrescrevendo métodos nativos da lista
#     def append(self, elem):
#         self.verifica_tipo(elem) 
#         if elem not in self.data:
#             super().append(elem)     
    
#     def __setitem__(self, posição, elem):
#         self.verifica_tipo(elem)
#         if elem not in self.data: # Corrigido o typo 'self.deta'
#             super().__setitem__(posição, elem)
    
#     # Adaptando seus métodos personalizados para usar 'self.data'
#     def adicionar(self, elem):
#         # Para evitar duplicar lógica, apenas chamamos o seu próprio append
#         self.append(elem)
    
#     def pesquisa(self, elem):
#         self.verifica_tipo(elem)
#         try:
#             return self.data.index(elem)
#         except ValueError:
#             return -1 
    
#     def indicevalido(self, indice):
#         # Simplificado usando encadeamento de operadores do Python
#         return 0 <= indice < len(self.data)
    
#     def ordena(self, chave=None):
#         self.data.sort(key=chave)  
# @total_ordering        
# class Name:
#     def __init__(self, nome):
#         # Ajuste: garante que nome não é None antes de chamar .strip()
#         if nome is not None and nome.strip():
#            self.nome = nome  
#            self.chave = nome.strip().lower()  
#         else:
#            self.nome = "Desconhecido"
#            self.chave = "desconhecido"
           
#     def __str__(self):
#         return self.nome
        
#     def __repr__(self):
#         return f'<classe {type(self).__name__} em 0x{id(self):x} nome {self.nome} chave: {self.chave}>'
        
#     def __eq__(self, outros):
#         print(f'__eq__ chamado: {self.nome} == {outros.nome}')
#         return self.nome == outros.nome
        
#     def __lt__(self, outros):
#         print(f'__lt__ chamado: {self.nome} < {outros.nome}')
#         return self.nome < outros.nome
#     @staticmethod
#     def criachave(nome):
#         return nome.strip().lower()


# # ==========================================
# # Exemplo Prático com Loop FOR
# # ==========================================

# # 1. Criando uma lista de instâncias da sua classe
# lista_nomes = [Name("Carlos"), Name("Ana"), Name("Beatriz")]

# print("--- Iterando com o loop for ---")
# for pessoa in lista_nomes:
#     # O print chama o método __str__ automaticamente
#     print(f"Processando: {pessoa}")

# print("\n--- Ordenando a lista ---")
# # O método .sort() usa automaticamente o seu __lt__ para organizar a lista
# lista_nomes.sort()

# print("\n--- Resultado após a ordenação ---")
# for pessoa in lista_nomes:
#     # Usando repr() para mostrar os detalhes internos do objeto
#     print(repr(pessoa))        
        
# banco.abre_conta(contaespecial)
# banco.lista_contas()  
# t= contaespecial.posso_sacar(200)
# print(t)
# maria = Cliente('maria', '2324444')
# joão = Cliente('joão', '988767656')
# cliente_joão = Conta([joão],numero='001',saldo=1000) 
# banco = Banco('BRUNODEV')
# contaespecial = ContaEspecial([maria, joão],numero='002',saldo=1000)
# resultado =contaespecial.saque(20000)
# print(resultado)
# contaespecial.extrato()
# banco.abre_conta(cliente_joão)

# Inicializando com o tipo correto: int
# lu = ListaUnica(int) 

# lu.adicionar(5)
# lu.adicionar(3)
# # Testando o resultado graças ao método mágico __iter__ que você criou:
# for numero in lu:
#     print(numero)
# print(f'indice',lu[0])  
# print(f'indice',lu[1])  
# lu.append(5)
# lu.append(3)
# print(lu)
# lu.append(5)
# print(lu)
# a = Name('bruo')
# print(a)

@total_ordering
class Nome:
    def __init__(self,nome):
        self.nome = nome
    def __str__(self):
        return self.nome
    def __repr__(self):
        return f'<Classe {type(self).__name__} em 0x{id(self):x} nome {self.nome} chave {self.__chave}>'    
    def __eq__(self, outro):
        return  self.nome == outro.nome
    def __lt__(self, outro):
        return self.nome < outro.nome
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,  valor):
        if valor is None or not valor.strip():
            raise ValueError('nome nao pode ser nulo nem em branco')
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)
    @property
    def chave(self):
        return self.__chave    
    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()        

A = Nome('BRUNO')
  

print(A.chave)            
