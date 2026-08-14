from functools import partial
entrada = "meu contato: (85)987654321 me liga"
# preciso entender o funcionamento desse codigo
def numero(entrada, qmin, qmax):
    num = 0
    for caractere in entrada:
        if caractere.isnumeric():
            num += 1
        else:                   
            break   
    if qmin <= num <= qmax:
        return num, 0, num - 1
    else:
        return -1, -1, -1
  
def sequencia(entrada, padrao):
    posicao, posicao_maxima = 0, len(padrao)
    for caractere in entrada:
        if caractere == padrao[posicao]:
            posicao += 1 # caractere igual testa o proximo caractere
        else:
            break # saiu da sequencia
        if posicao == posicao_maxima: # achou toda a sequencia
            return 1, 0, posicao - 1
    return -1, -1, -1
     
def verifica_padrao(entrada, padraoes):
    posicao = 0
    for padrao in padraoes:
        
        achou, _, fim = padrao(entrada[posicao:])
        if achou > 0:
            posicao += fim + 1
        else:
            return -1, -1, -1
    return 1, 0, posicao - 1
    

def ddd(entrada):
    achou, _, fim = verifica_padrao(entrada,[
        partial(sequencia, padrao='('),
        partial(numero, qmin=2, qmax=3),
        partial(sequencia, padrao=')'),],)    
    return (1, 0, fim) if achou > 0 else (-1, -1, -1)

def nova_verifcao(entrada):
       achou, _, fim = verifica_padrao(entrada,[
       partial(numero, qmin=1, qmax=len(entrada))    
       ])
       return (1, 0, fim) if achou > 0 else (-1, -1, -1)
def datinha(entrada):
    achou, _, fim = verifica_padrao(entrada,[
        partial(numero, qmin=2, qmax=2),
        partial(sequencia, padrao='/'),
        partial(numero,qmin=2, qmax=2 ),
        partial(sequencia, padrao='/'),
        partial(numero, qmin=2, qmax=2)
    ])
    return (1, 0, fim) if achou > 0 else (-1, -1, -1)
def valor(entrada):
        achou, _, fim = verifica_padrao(entrada,[
            partial(sequencia, padrao='R$'),
            partial(sequencia, padrao=' '),
            partial(numero, qmin=1, qmax=len(entrada)),
            partial(sequencia, padrao=','),
            partial(numero, qmin=1, qmax=2)
          ])
        return (1, 0, fim) if achou > 0 else (-1, -1, -1)  
def sequenciais(entrada, padrao, qmin, qmax):
    repeticoes = 0
    pos_atual = 0
    
    for vezes in range(qmax):
        achou, _, fim = sequencia(entrada[pos_atual:], padrao)
        
        if achou > 0:
            repeticoes += 1
            pos_atual += fim + 1
        else:
            break
            
    if qmin <= repeticoes <= qmax:
        return 1, 0, pos_atual - 1
    else:
        return -1, -1, -1
def smartphone(entrada):
    achou, _, fim = verifica_padrao(entrada,[
        ddd,
        partial(numero, qmin=9, qmax=9)
    ])
    return (1, 0, fim) if achou > 0 else (-1, -1, -1)                 
for posicao in range(len(entrada)):
    # Agora passamos o padrão ("Z"), o mínimo (1) e o máximo (3)
    achou, inicio, fim = smartphone(entrada[posicao:])
    
    if achou > 0:
        print(f"Sequência encontrada nas posições: {posicao+inicio} a {posicao+fim}")
        print(entrada[posicao + inicio : posicao + fim + 1])   