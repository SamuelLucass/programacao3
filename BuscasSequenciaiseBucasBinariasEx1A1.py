
def buscaSequencial(dados,buscado):
    achou = 0
    i = 0 

    while (((i < len(dados))) and (achou == 0)):
        if (dados[i] == buscado):
            achou = 1 
        else: 
            i = i + 1 
    if (achou == 0):
        return -1
    else:
        return i + 1

#Programa Principal 
import random

#gerando 10 valores dentro de um intervalo de 0 até 9 
dados = random.sample(range(10), 10)
dados.sort()
print (dados)
buscado = int(input('Digite o valor que deseja buscar: '))
achou = buscaSequencial(dados, buscado)
if (achou == -1):
    print('valor não encontrado.')
else: 
    print('valor encontrado na posição {}'.format(achou))
     

def buscaBinaria (inicio,fim,dados,buscado):
    while(inicio <= fim):
        meio = int((inicio + fim)/2)
        if (buscado > dados[meio]):
            inicio = meio + 1
        elif (buscado < dados [meio]):
            fim = meio - 1
        else:
            return meio
    return -1

#programa principal
import random

#gerando 10 valores dentro de um intervalo de 0 aé 9 
dados = random.sample(range(10), 10)
dados.sort()
print(dados)
buscado = int(input("Digite o valor que deseja buscar: "))
achou = buscaBinaria(0, len(dados), dados, buscado)
if (achou == -1):
    print("Valor não encontrado.")
else:
    print("valor encontrado na posição {}" .format(achou))