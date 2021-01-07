#####################################################
# Tarefa 1 - Produtor Consumidor (Implementação 1)  #
#                                                   #
# Versão do Python: 3.9.0                           #
# Data:      16/12/2020                             #
# Autor:     Diego S. Seabra                        #
# Matrícula: 0040251                                #
#                                                   #
#####################################################

# Importações
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

# Produz um elemento
def produz():
    valor_produzido = random.randint(1,1000)     # Gera um número aleatório (entre 1 e 1000)
    buffer.append(valor_produzido)               # Adiciona o valor produzido no buffer
    print(bcolors.OKCYAN + "Produzido: " + str(valor_produzido) + bcolors.ENDC)

# Consome um elemento
def consome():
    valor_a_consumir = buffer.pop()              # 'Busca' o valor a ser consumido do buffer 
                                                 # (no caso, o último elemento inserido)
    print(bcolors.HEADER + "Consumido: " + str(valor_a_consumir) + bcolors.ENDC)

# Mostra o estado do buffer (sim/não)
def estado_buffer(mostra):
    if mostra:
        print(bcolors.WARNING + "Buffer: " + str(buffer) + bcolors.ENDC)

# Roda o algoritmo
def roda(mostra_historico):
    while(True):
        estado_buffer(mostra_historico)
        produz()
        estado_buffer(mostra_historico)
        consome()
        estado_buffer(mostra_historico)
        time.sleep(0.5) # Espera meio segundo (para melhor visualização do histórico)

# Mostra um menu de opções
def menu():
    print('-----------------------------------------------')
    print('Produtor-Consumidor - Implementação 1')
    print('')
    print('1) Rodar SEM histórico do buffer')
    print('2) Rodar COM histórico do buffer')
    opcao = input("\nEscolha uma opção:\n")

    if opcao == '1':
        roda(False)

    if opcao == '2':
        roda(True)

# 'Main' do programa
if __name__ == "__main__":
    menu()