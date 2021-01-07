#####################################################
# Tarefa 1 - Produtor Consumidor (Implementação 3)  #
#                                                   #
# Versão do Python: 3.9.0                           #
# Data:      07/01/2020                             #
# Autor:     Diego S. Seabra                        #
# Matrícula: 0040251                                #
#                                                   #
#####################################################

# Importações
from threading import Thread, Condition
import logging
import random
import time

# Define as cores usadas no log
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Cria o buffer
buffer = []

# Condição de Bloqueio
mutex = Condition()

# Pool de produtores e consumidores
produtores = []
consumidores = []

def mostra_buffer(opt):
    if opt == 's' or opt == 'S':
        print(bcolors.WARNING + "Buffer: " + str(buffer) + bcolors.ENDC)

# Define a classe do Produtor
class Produtor(Thread):
    global buffer

    def run(self):
        while True:
            mostra_buffer(logBuffer)
            mutex.acquire()
            if len(buffer) == limiteBuffer:              # Buffer cheio, para de produzir
                print(bcolors.FAIL + 'Buffer cheio! Para de produzir!' + bcolors.ENDC)
                mutex.wait()
                print(bcolors.OKCYAN + 'Acordou o produtor ' + self.name + bcolors.ENDC)
            else:
                valor_produzido = random.randint(1,1000)     # Gera um número aleatório (entre 1 e 1000)
                buffer.append(valor_produzido)
                print(bcolors.OKCYAN + '[' + self.name + '] Produziu ' + str(valor_produzido) + bcolors.ENDC)
                mutex.notifyAll()  # Notifica o mutex
                mutex.release()    # Libera o mutex
                time.sleep(1)      # Espera um segundo (para melhor visualização do histórico)
            mostra_buffer(logBuffer)

# Define a classe do Consumidor
class Consumidor(Thread):
    global buffer

    def run(self):
        while True:
            mostra_buffer(logBuffer)
            mutex.acquire()
            if len(buffer) == 0:    # Buffer vazio, para de consumir
                print(bcolors.OKGREEN + 'Buffer vazio! Começa a produzir!' + bcolors.ENDC)
                mutex.wait()
                print(bcolors.HEADER + 'Acordou o consumidor ' + self.name + bcolors.ENDC)
            else:
                valor_consumido = buffer.pop()       # 'Busca' o valor a ser consumido do buffer (no caso, o último elemento inserido)
                print(bcolors.HEADER + '[' + self.name + '] Consumiu ' + str(valor_consumido) + bcolors.ENDC)
                mutex.notifyAll()  # Notifica o mutex
                mutex.release()    # Libera o mutex
                time.sleep(1)      # Espera um segundo (para melhor visualização do histórico)
            mostra_buffer(logBuffer)

# Imprime um menu de interação
print('-----------------------------------------------')
print('Produtor-Consumidor - Implementação 3\n')
qtdeProdutores = int(input("\nInsira a quantidade de PRODUTORES:\n"))
qtdeConsumidores = int(input("\nInsira a quantidade de CONSUMIDORES:\n"))
limiteBuffer = int(input("\nInsira o tamanho do BUFFER:\n"))
logBuffer = input("\nImprime histórico do buffer? (s/n)\n")
print('\n')

# Inicia o pool de produtores
for i in range(qtdeProdutores):
    p = Produtor(name = 'Produtor ' + str(i))
    produtores.append(p)
    p.start()

# Inicia o pool de consumidores
for i in range(qtdeConsumidores):
    c = Consumidor(name = 'Consumidor ' + str(i))
    consumidores.append(c)
    c.start()