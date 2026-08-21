import re
def validar_cnpj():
    entrada = input("digite o seu CNPJ ")
    teste = re.fullmatch(r"\d{2}\.\d{3}\.\d{3}/\d{4}\-\d{2}",entrada)
    if teste:
       print("CNPJ valido")
    else:
       print('CNPJ invalido')   
