import re
def validar_cpf():
    entrada = input("digite o seu cpf ")
    teste = re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}",entrada)
    if teste:
        print("cpf valido")
    else:
        print('cpf invalido')  
validar_cpf()        