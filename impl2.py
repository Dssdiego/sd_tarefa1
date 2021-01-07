#####################################################
# Tarefa 1 - Produtor Consumidor (Implementação 2)  #
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
limiteBuffer = 10

# Inicia com o consumidor bloqueado
consumidorBloqueado = True
produtorBloqueado = False

# Imprime um menu de interação
print('-----------------------------------------------')
print('Produtor-Consumidor - Implementação 2')
print('')
print('1) Rodar SEM histórico do buffer')
print('2) Rodar COM histórico do buffer')
opcao = input("\nEscolha uma opção:\n")

# Verifica a opção inserida
if opcao == '1':
    mostraBuffer = False

if opcao == '2':
    mostraBuffer = True

# Loop que roda o programa
while(True):
    # Se o usuário escolher, mostra o buffer
    if mostraBuffer:
        print(bcolors.WARNING + "Buffer: " + str(buffer) + bcolors.ENDC)

    # Produtor 
    if len(buffer) == limiteBuffer:               # Buffer cheio, começa a consumir
        print(bcolors.FAIL + 'Buffer cheio! começa a consumir!' + bcolors.ENDC)
        consumidorBloqueado = False                  # Desbloqueia o consumidor
        produtorBloqueado = True                     # Bloqueia o produtor
    if not produtorBloqueado:
        valor_produzido = random.randint(1,1000)     # Gera um número aleatório (entre 1 e 1000)
        buffer.append(valor_produzido)               # Adiciona o valor produzido no buffer
        print(bcolors.OKCYAN + "Produzido: " + str(valor_produzido) + bcolors.ENDC)

    # Consumidor
    if len(buffer) == 0:                             # Buffer vazio, começa a produzir
        print(bcolors.OKGREEN + 'Buffer vazio! Começa a produzir!' + bcolors.ENDC)
        consumidorBloqueado = True                   # Bloqueia o consumidor
        produtorBloqueado = False                    # Debloqueia o produtor
    if not consumidorBloqueado:
        valor_a_consumir = buffer.pop()              # 'Busca' o valor a ser consumido do buffer (no caso, o último elemento inserido)
        print(bcolors.HEADER + "Consumido: " + str(valor_a_consumir) + bcolors.ENDC)

    # Espera meio segundo (para melhor visualização do histórico)
    time.sleep(0.5)