import re
class Validar:
   def __init__(self):
      pass
   def validar_ambos(self,entrada):
      validar_cnpj = re.fullmatch(r"\d{2}\.\d{3}\.\d{3}/\d{4}\-\d{2}",entrada)
      validar_cpf = re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}",entrada)
      if validar_cnpj:
         print('CNPJ VALIDO')
      elif validar_cpf:
         print('CPF VALIDO')
      else:
         print('ambos os dados estão invalidos') 
validando = Validar()
entrada = input("digite cpf ou cnpj")
validando.validar_ambos(entrada)