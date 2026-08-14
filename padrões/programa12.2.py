entrada = "compre R$ 50.00. ligue já (85) 98765-7657 antes de 10/04/2026"
saida = []
numero = []
codigo_ddd = []
def ddd(entrada):
    estado = 0
    posição_ddd = []
    for posição, caratecre in  enumerate(entrada):
        if estado == 0 and caratecre == "(":
            estado = 1
            posição_ddd.append(caratecre)
        elif estado == 1 and caratecre.isnumeric() and posição <= 3:
            posição_ddd.append(caratecre)
        elif estado == 1 and caratecre == ")":
            estado = 2
            codigo_ddd.append(caratecre)
            return True, 0, posição
        else:
            break
    return False, -1, -1
for posição in range(len(entrada)):
        achou, inicio, fim = ddd(entrada[posição])    
        if achou:
            print(f"DDD encontrado nas posições: {posição+inicio} a {posição+fim}")
            print(entrada[posição+inicio : posição + fim + 1])