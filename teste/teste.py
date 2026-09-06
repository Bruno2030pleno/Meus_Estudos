# Exercício 1 — Aquecimento
# Quero que você escreva um programinha que:
# Peça ao usuário o nome e a idade dele
# Calcule em que ano essa pessoa completa (ou completou) 100 anos
# Exiba uma frase dizendo isso

# def dados_pessoais():
#     nome = input("digite seu nome: ")
#     idade = int(input("digite sua idade"))
#     resultado = 2026 - idade
#     anos = resultado + 100
#     print(f"seu nome {nome}")
#     print(f"sua idade {idade}")
#     print(f"ano que você nasceu {resultado}")
#     print(f"atualmente você tem {idade} anos e faz aniversario em março no dia 19")
#     print(f"você completa 100 anos em {anos}")
# dados_pessoais()         



# Bloco 2 — Condicionais e Laços
# Vamos subir um degrau. Ainda usando nome e idade, quero que você escreva um programa que:
# Peça o nome e a idade da pessoa
# Classifique essa pessoa em uma faixa: criança (até 12), adolescente (13 a 17), adulto (18 a 59) ou idoso (60 ou mais)
# Imprima uma frase dizendo o nome e a faixa correspondente

# def faixa_idade():
#     while True:
#         nome = input("digite seu nome: ou ENTER para sair: ")
#         if nome == '':
#             print("fim do programinha")
#             break
#         try:    
#             idade = int(input("digite sua idade"))
#             if idade <= 12:
#                 print(f"o {nome} tem {idade} anos:criança")
#             elif idade >= 13 and idade <= 17:
#                     print(f"o {nome} tem {idade} anos: adolecente")
#             elif idade >= 18 and idade <= 59:
#                 print(f"o {nome} tem {idade} anos: adulto")   
#             elif idade >= 60:
#                 print(f"o {nome} tem {idade} anos: idoso") 
#         except ValueError:
#             print("Por favor digite apenas numeros: ")                
# faixa_idade()            



# Bloco 3 — Funções

# Agora vamos separar responsabilidades. Até aqui, tudo mora dentro de uma função só (faixa_idade), 
# misturando entrada de dados, lógica de decisão e impressão.

# Quero que você reescreva esse mesmo problema, mas dividido em pelo menos duas funções:

# Uma função que recebe uma idade e retorna (não imprime!) a faixa correspondente como string ("criança", "adolescente", etc.)
# Uma função "principal" que fica com o loop,
#  pede nome/idade ao usuário, chama a primeira função pra descobrir a faixa,
#  e só ela é responsável por imprimir o resultado

# def recebe_uma_idade(idade):
#     if idade <= 12:
#         return "Criança"
#     elif idade >= 13 and idade <= 17:
#         return "adolecente" 
#     elif idade >= 18 and idade <= 59:
#         return "adulto"
#     elif idade >= 60:
#         return "idoso"

# def nome_idade():
#     lista = []
#     while True:
#         nome = input("digite seu nome: OU ENTER PARA SAIR: ")
#         if nome == '':
#             break
#         idade = int(input("digite sua idade"))
#         if  idade:
#             faixa = recebe_uma_idade(idade)
#             print(f"nome {nome} e {idade}: {faixa}")   
#             lista.append({'nome': nome, 'idade': idade, 'faixa': faixa}) 
#     for nomeS in lista:
#         print(f"{nomeS['nome']}, {nomeS['idade']} anos: {nomeS['faixa']}")      
# nome_idade()                                

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.faixa = self.recebe_uma_idade()
#     def recebe_uma_idade(self):
#         if self.idade <= 12:
#             return "Criança"
#         elif self.idade >= 13 and self.idade <= 17:
#             return "adolecente" 
#         elif self.idade >= 18 and self.idade <= 59:
#             return "adulto"
#         elif self.idade >= 60:
#             return "idoso"        
# def loop():
#     lista = []
#     while True:
#         nome = input("digite seu nome: ou enter para sair: ")
#         if nome == '':
#             break
#         idade = int(input("qual a sua idade ?: "))
#         pessoa = Pessoa(nome, idade) 
#         lista.append(pessoa)
#     for nomes in lista:
#         print(f"nome {nomes.nome} idade {nomes.idade} faixa {nomes.faixa}")                
# loop()    

# O exercício

# Vamos criar uma classe Aluno que substitui aquele dicionário de aluno que você tinha no Bloco 4. Ela precisa:

# Guardar nome e notas (uma lista de notas, tipo 3 provas).
# Ter um método que calcula a média dessas notas.
# Ter um método que diz se o aluno foi aprovado (média ≥ 7) ou reprovado.
# No final, criar uma lista de objetos Aluno (não mais de dicionários) e percorrer essa lista imprimindo nome, média e situação de cada um.


# 1 classe Aluno
# class Aluno:

#     def __init__(self,nome, notas):
#         self.nome  = nome
#         self.notas = notas
#         self.lista = []
   
#     def media_das_notas(self):
#         media = sum(self.notas) / len(self.notas)
#         return media 
#     def reprova_ou_aprova(self):
#         if  self.media_das_notas() >= 7:
#             self.lista.append(self.media_das_notas())
#             print(f"nome do aluno {self.nome} e notas {self.notas}")
#             print("aprovado")
#         else:
#             print("reporvado")
# def notas(): 
#     lista_de_notas = [10, 9.5, 6.7]
#     lista_de_notas1 = [10, 8.9, 7.8]
#     lista_de_notas2 = [10, 5.7, 7.8]
    
#     aluno0 = Aluno('BRUNO', lista_de_notas)
#     aluno1 = Aluno('maria', lista_de_notas1)
#     aluno2 = Aluno('miguel',lista_de_notas2)
#     alunos = [aluno0, aluno1, aluno2]
#     for nomes in alunos:
#         nomes.reprova_ou_aprova()
# notas()


# Bloco A — Tipos e atribuição básica
# Crie uma variável com seu nome, uma com sua idade e uma com sua altura
# (em metros, com casas decimais). Depois, use type() em cada uma e escreva do lado, em comentário, qual tipo o Python vai dizer que é cada uma 
# (antes de rodar — tenta adivinhar primeiro).
# Sem usar input(), crie duas variáveis numéricas e troque os valores delas entre si (a que era a vira b, e vice-versa)
# — sem usar uma terceira variável auxiliar. (Dica: pensa em desempacotamento de tupla, algo que você já viu antes.)

# nome = 'bruno'
# idade = 35
# altura = 1.76
# print(type(nome))
# print(type(idade))
# print(type(altura))
# class N(str):
#     def __init__(self,n):
#         self.n = n 
#         super().__init__()
# a = N('3')
# print(a)  

        