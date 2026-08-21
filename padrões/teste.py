import re
# codigo = 'ABC431DEF901c432139SDF9'
# teste = re.findall(r"\(\d{2,4}\)", ' (8834)9495-1234' )
# print(teste)

# import re
# codigo = 'ABC431DEF901c432139SDF9'
# teste = re.findall(r"\(\d{3}\)\d{3}\d{3}-\d{2}", ' 345.456.543-44' )
# print(teste)

# import re
# codigo = 'compre por 50,72. ligue já (92)9981-8912 antes de 30/08/2026'
# teste = re.findall(r"(?:\(\d{2,3}\))?\s*\d{4}-\d{4,5}", codigo )
# print(teste)

# import re
# codigo = input("digite algo")
# teste = re.findall(r"[Rr]\$\s*\d*,?\d*",codigo) 
# print(teste)

# import re
# codigo = input("")
# teste = re.findall(r"[Rr]\$\s*(\d*,?\d*)", codigo ,re.IGNORECASE ) 
# print(teste)


# codigo = 'compre por R$50,72. ligue já (92)9981-8912 antes de 30/08/2026'
# teste = re.findall(r"\d{6}", codigo ) 
# print(teste)

# exemplo = 'ola mundo. tudo "bem"? por "ai"'
# teste = re.compile(r"\".*?\"") 
# print(teste.findall(exemplo))
# print(teste.search(exemplo))

# exemplo = 'ola mundo. tudo "bem"? por "ai"'
# teste = re.compile(r"r\$\s*\d+,?\d+", re.IGNORECASE) 
# print(teste.match("R$  10"))

# REAIS = re.compile(r"r\$\s*(\d+),?(\d+)",re.IGNORECASE)
# valores = REAIS.match("R$ 100,99")
# print(valores.groups())


# REAIS = re.compile(r"r\$\s*(?P<principal>\d+),?(?P<centavos>\d+)", re.IGNORECASE)
# valores = REAIS.match("R$ 100,99")
# print(valores.groupdict())
# print(valores.group('principal'))

# seq = re.compile(r"(?P<seq>\w{3})(.*?)(?P=seq)")
# teste= seq.match("AAAabcfAAA").groups()
# print(teste)

# import re
# codigo = input("digite algo")
# teste = re.findall(r"[Rr]\$\s*\d*,?\d*",codigo)
# print(teste)

      

def salario():
    salario_base = 1920.00
    gastos = {
    'inss': 130.00,
    'desntista': 30.00,
    'cesta': 16.00,
    'sindicato': 16.00,
    'emprestimos': 530.00,
    'faculdade': 370.00,
    'cabelo': 60.00,
    'agua_flavio':70.00,
    'tim': 30.00,
    'spotyfi': 14.00,
    'cartao': 145.00,
    'nubank': 190.00,
    'net': 100.00,
    'luz': 230.00
}
    
    acumulador = 0
    for chave, valor in gastos.items():
        acumulador += valor
        print(f"{chave} valor: R$ {valor:.2F}")
    meu_salario = salario_base - acumulador
    print('----------------------------------') 
    print(f"VALOR DOS GASTOS R$ {acumulador:.2f}")
    print(f"SALARIO BASE R$ {salario_base:.2f}")
    print(f"SALDO FINAL R$ {meu_salario:.2f}")
    print("DIA 20 CAI O CARTAO DOS  R$ 300.00 REAIS")
    print("EU TENHO UM VALE REFEIÇÃO DE 450 REAIS + 450 REAIS DE CESTA FICA R$ 900 REAIS MAIS OS 300 ")
    

def utilizando():
    salario()
utilizando()    

     

