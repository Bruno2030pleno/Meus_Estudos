# nome = input("digite um nome ")
# match nome.lower():
#     case 'bruno':
#         print('olá bruno')
#     case 'lena':
#         print('olá lena')
#     case _:
#         print('não conheço vocês ')
# if nome == 'bruno':
#     print('tudo bem com vc bruno ?')
#     sim_ou_nao = input("sim ou nao ?")
#     if sim_ou_nao == 'sim':
#        print('seu dia esta otimo')
# else:
#    print('nome invalido!!!')    
         
# def f(x):
#     match x:
#         case int():
#             print('int')
#         case str():
#             print('str')
#         case m:
#             print(F'default {m}')
# f(2.3)

# def g(x):
#     match x:
#         case x if 0 <= x < 10:
#             print('entre 0 e 9')
#         case BUG:
#             print(F'{BUG} : fora da faixa')
# g(10)
# def h(lista):
#     match lista:
#         case [1, *_]:
#             print('1')
#         case [2, *_]:
#             print('2')
#         case _:
#             print('não começa nem com 1 e nem com 2')
# h([3,4])                    

# def executa(comando):
#     match comando:
#         case ['vá'|'va',para_onde]:
#             print(f"você foi para {para_onde}")
#         case ['suba']:
#             print("vocẽ subiu")
#         case ['pegue', 'pá' | 'martelo' | 'espada' as objeto]:
#             print(f"você pegou o {objeto}")
#         case _:
#             print(" não entendi: redigite") 
# executa(['va', 'pegue'])                       

# def v(lista):
#     match lista:
#         case [primeiro, ultimo]:
#             print(f"{primeiro=} {ultimo=}")
#         case [primeiro, *meio, ultimo]:
#             print(f"{primeiro=} {meio=} {ultimo=}")    
# v(['A','B','C','D']) 
# lista = ['brumo', 'lena', 'miguel', 'money']               
# b, *l, m = lista
# print(l)

# def novo_preco(dicionario):
#     match dicionario:
#         case {'nome': 'batata'}:
#             return 10.0
#         case {'preco': preco} if preco % 1 != 0:
#             return round(preco, 1)
#         case _:
#             return dicionario['preco'] * 1.1
# print(novo_preco({'nome': 'cebola', 'preco': 1.85}))        

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self. preco = preco

    def __str__(self):
        return self.nome
class Vegetal(Produto):
        pass
class Animal(Produto):
    pass
def imprime_produto(produto):
    match produto:
        case Vegetal():
            print(f"{produto} e um vegetal") 
        case Animal(preco=v) if v > 50.0:
            print(f"{produto} e um animal")
            
        case Animal():
            print(f"{produto} e um animal")
        case Produto():
            print(f"{produto} e prouto orinario")
imprime_produto(Vegetal('CEBOLA', 2.0))                   
        