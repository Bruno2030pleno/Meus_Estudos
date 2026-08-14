telefone = "compre R$ 50.00. ligue já (85) 98765-7657 antes de 10/04/2026"
saida = []

def numero(entrada, qmin, qmax):
    num = 0
    for caractere in entrada:
        if caractere.isnumeric():
            num += 1
        else:
            break
    if qmin <= num <= qmax:
        return True, 0, num - 1
    return False, -1, -1

def ddd(entrada):
    estado = posicao = 0
    while posicao < len(entrada):
        caractere = entrada[posicao]
        if estado == 0 and caractere == "(":
            estado = 1
            posicao += 1
        elif estado == 1:
            achou, inicio, fim = numero(entrada[posicao:], 2, 3)
            if achou:
                estado = 2
                posicao += fim + 1
            else:
                break
        elif estado == 2:
            if caractere == ')':
                return True, 0, posicao
            break
        else:
            break
    return False, -1, -1

for posicao in range(len(telefone)):
    achou, inicio, fim = ddd(telefone[posicao:])
    if achou:
        print(f"DDD encontrado nas posições: {posicao+inicio} a {posicao+fim}")
        print(telefone[posicao+inicio : posicao+fim+1])                   