class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []
    def resumo(self):
        print(f'CC numero {self.numero}, saldo R${self.saldo:10.2f}')
        for dados in self.clientes:
            print(f'nome {dados.nome} telefone {dados.telefone}')
    def saque(self, valor):
        if self.posso_sacar(valor):
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            print('saque realizado com sucesso')
            return True
        else:
            print('SALDO INSUFICIANTE!!')  
            return False 
    def deposito(self, valor):
        self.saldo += valor
        print(f'valor depositado R${valor:10.2f}')
        self.operacoes.append(['DESPOSITO', valor])
    def extrato(self):
        print(f'extrato CC N {self.numero}\n')
        
        for operacao in self.operacoes:
            print(f"{operacao[0]:.10s} {operacao[1]:10.2f}")
        print(f'\nsaldo R${self.saldo:10.2f}') 
    def posso_sacar(self, valor):
        return self.saldo >= valor 
        
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
    
    def abre_conta(self, conta):
        self.contas.append(conta)
    
    def lista_contas(self):
        for c in self.contas:
            c.resumo()
class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite
   
    def extrato(self):
        super().extrato()
        print(f'seu limite disponivel {self.limite:.2f}')
        print(f'valor disponivel para saque, {self.saldo + self.limite }')
    def posso_sacar(self, valor):
        return self.saldo + self.limite >= valor
maria = Cliente('maria', '2324444')
joão = Cliente('joão', '988767656')
cliente_joão = Conta([joão],numero='001',saldo=1000) 
banco = Banco('BRUNODEV')
contaespecial = ContaEspecial([maria, joão],numero='002',saldo=1000)


resultado =contaespecial.saque(20000)
print(resultado)

contaespecial.extrato()
banco.abre_conta(cliente_joão)
banco.abre_conta(contaespecial)
banco.lista_contas()  
t= contaespecial.posso_sacar(200)
print(t)
