import re
def validar_preco():
    try:
        codigo = input("digite algo UM VALOR  ")
        teste = re.findall(r"[Rr]\$\s*\d{1,3}(?:\.\d{3})*(?:,\d+)?", codigo)
        if teste:
            for valor in teste:
                valor = valor.replace('R','') 
                valor = valor.replace('$','')
                valor = valor.replace('.','')
                valor = valor.replace(',','.')
                print('entrada valida')
                print(f"valor {valor}")  
            return float(valor)             
        else:   
            raise ValueError("mensagem explicando o erro")
    except ValueError:
        print('Erro,  valor incorreto')
print(validar_preco())     

    

