# def box_print(symbol, width, height):
#     if len(symbol) != 1:
#        raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#        raise Exception('Width must be greater than 2.')
#     if height <= 2:
#        raise Exception('Height must be greater than 2.')

#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)

# try:
#     box_print('*', 4, 4)
#     box_print('O', 20, 5)
#     box_print('x', 1, 3)
#     box_print('ZZ', 3, 3)
# except Exception as err:
#    print('An exception happened: ' + str(err))
# try:
#     box_print('ZZ', 3, 3)
# except Exception as err:
#     print('An exception happened: ' + str(err))
# from pathlib import Path as path

# class Arquivo:
#     def __init__(self,conteudo, nome_arquivo):
#         self.nome_arquivo = nome_arquivo
#         self.conteudo = conteudo
#     def apen(self):
#         if path(self.nome_arquivo).exists():
#             print('o arquivo ja existe') 
#         with open(self.nome_arquivo, 'a', encoding='utf-8') as arquivo:
#             arquivo.write(self.conteudo) 
# teste = Arquivo('TESTE DE REVISÃO''\n', 'brundod.txt')   
# teste.apen()               


# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73, 10]
# ages.sort()
# print(ages)
# [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
# assert ages[0] <= ages[-1]        

# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# print(logging)

# import logging 
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
# format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.debug('Start of program')

# def factorial(n):
#     logging.debug('Start of factorial(' + str(n) + ')')
#     total = 1

#     for i in range(1, n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(' + str(n) + ')')
#     return total

# print(factorial(5))
# logging.debug('End of program')


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
logging.debug('Some minor code and debugging details.')
# 2035-05-18 19:04:26,901 - DEBUG - Some debugging details.
logging.info('An event happened.')
# 2035-05-18 19:04:35,569 - INFO - The logging module is working.
logging.warning('Something could go wrong.')
logging.error('An error has occurred.')
# 2035-05-18 19:05:07,737 - ERROR - An error has occurred.
logging.critical('The program is unable to recover!')
# 2035-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!