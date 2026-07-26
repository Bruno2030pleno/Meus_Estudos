# class NovaException(Exception):
#     pass
# def lançador():
#     raise NovaException
# try:
#     lançador()
# except NovaException:
#     print('UMA EXCEÇÃO DO TIPO NOVAEXCEPTION FOI LAÇADA')    
class BancoException(Exception):
    pass
class SaldoIndisponivel(BancoException):
    pass
class ClienteNãoExiste(BancoException):
    pass
def saque(saldo, valor):
    
    if valor > saldo:
        raise SaldoIndisponivel
    return saldo - valor
try:
    saldo = saque(100, 500)
except SaldoIndisponivel:
    
    print('Erro, saldo insuficiente')
class EstoqueException(Exception):
    def __init__(self,mensagem, codigo_de_erro):
        super().__init__(mensagem)                  
        self.codigo_de_erro = codigo_de_erro
def verifique_quantidade(quantidade):
        if quantidade < 0:
            raise EstoqueException('QUANTIDADE INSUFICIENTE', codigo_de_erro=1)
try:
    verifique_quantidade(-10)
except EstoqueException as ee:
    print(f"Erro, {ee.codigo_de_erro} {ee}" )      