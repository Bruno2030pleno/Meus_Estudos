entrada = 'ABC431DEF901'
saida = []
numero = []
letras = []
for c in entrada:
    A = c.lower()
    if "a" <= A <= "z":
        if not numero:
           saida.append(numero)
        numero += c
    elif numero:
       numero = []
for e in saida:
    letras.append(''.join(e))     
print(letras) 
caixa = letras[0] + letras[1]
print(caixa)
nova = []
for n in caixa:
    nova.append(n)
cafe = nova[2]+nova[0]+nova[5]+nova[4]
print(cafe)
print(ord('a'))
print(ord('z'))
print(ord('á'))
print(ord('ã'))