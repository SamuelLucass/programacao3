'''
### Enunciado: Com a finalidade de melhorar o atendimento e priorizar os casos mais urgentes, a direção de um hospital criou um sistema de triagem em que um profissional da saúde classifica a ordem de atendimento com base numa avaliação prévia do paciente, entregando-lhe um cartão numerado verde (V) ou amarelo (A), que define o menor ou maior grau de urgência da ocorrência, respectivamente. Para informatizar esse processo, a direção do hospital contratou você para desenvolver uma fila de chamada seguindo as seguintes regras:

- [x]  Pacientes com cartão numerado amarelo (A) são chamados antes dos pacientes com cartão numerado verde (V)
- [x]  Entre os pacientes com cartão numerado amarelo (A), os que tem numeração menor são atendidos antes.
- [x]  Entre os pacientes com cartão numerado verde (V), os que tem numeração menor são atendidos antes.
- [x]  As numerações dos cartões amarelos (A) iniciam em 201.
- [x]  As numerações dos cartões verdes (V) inicial em 1.

'''

# Classe criada que cria os elementos da Lista Encadeada simples e os instancia
class ElementoDaListaSimples:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

    def __repr__(self):
        return f'[{self.numero}, {self.cor}]'

#A. Deve-se implementar uma Lista Encadeada Simples em que: [EXIGÊNCIA DE CÓDIGO 1 de 7];
#   a. O Nodo representa um cartão numerado contendo: número, cor e um ponteiro para o próximo;
#   b. A lista contém um ponteiro para a cabeça da lista (head);

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(repr(nodo))
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

#B. Deve-se implementar a função inserirSemPrioridade(nodo) em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
#   a. Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo no final da lista.

    def inserirSemPrioridade(self, nodo): 
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        nodo_anterior = None
        while nodo_atual is not None and nodo_atual.numero < nodo.numero:
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.proximo
        
        if nodo_anterior is None:
            nodo.proximo = self.head
            self.head = nodo
        else:
            nodo.proximo = nodo_atual
            nodo_anterior.proximo = nodo

#C. Deve-se implementar a função inserirComPrioridade(nodo) em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
#   a. Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo após todos os nodos com cor “A” que estão na lista.
#   b. O nodo inserido deve sempre estar antes de todos os nodos com cor “V”.

    def inserirComPrioridade(self, nodo):
        if self.head is None or (self.head.cor == 'V' or (self.head.cor == 'A' and self.head.numero > nodo.numero)):
            nodo.proximo = self.head
            self.head = nodo
            return

        nodo_atual = self.head
        nodo_anterior = None
        while nodo_atual.proximo is not None and nodo_atual.proximo.cor == 'A' and nodo_atual.proximo.numero < nodo.numero:
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.proximo

        nodo.proximo = nodo_atual.proximo
        nodo_atual.proximo = nodo

#D. Deve-se implementar a função inserir() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
#   a. Deve-se solicitar ao usuário a cor (“A” ou “V”) e o número (inteiro).
#   b. Deve-se criar um nodo com a cor e o número fornecidos pelo usuário.
#   c. Se a lista estiver vazia, a cabeça (head) da lista deve apontar para o nodo criado.
#   d. Senão, se a cor do nodo for “V”, deve-se chamar a função inserirSemPrioridade(nodo).
#   e. Senão, se a cor do nodo for “A”, deve-se chamar a função inserirComPriordade(nodo).


    def inserir(self):
        cor = input('Digite a cor do cartão (A ou V): ').strip().upper()
        while cor not in ['A', 'V']:
            cor = input('Cor inválida! Digite a cor do cartão (A ou V): ').strip().upper()
        
        if cor == 'A':
            numero = int(input('Digite o número do cartão (mínimo 201): ').strip())
            while numero < 201:
                numero = int(input('Número inválido! Digite um número igual ou superior a 201: ').strip())
        else:
            numero = int(input('Digite o número do cartão (mínimo 1): ').strip())
            while numero < 1:
                numero = int(input('Número inválido! Digite um número igual ou superior a 1: ').strip())

        novo_nodo = ElementoDaListaSimples(numero, cor)

        if self.head is None:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)

#E. Deve-se implementar a função imprimirListaEspera() em que: [EXIGÊNCIA DE CÓDIGO 5 de 7];
#   a. Deve-se imprimir todos os cartões e seus respectivos números a partir do primeiro até o último da lista.

    def imprimirListaEspera(self):
        if self.head is None:
            print("A lista está vazia.")
        else:
            nodo = self.head
            while nodo is not None:
                print(f'Cartão número: {nodo.numero}, Cor: {nodo.cor}')
                nodo = nodo.proximo

#F. Deve-se implementar a função atenderPaciente() em que: [EXIGÊNCIA DE CÓDIGO 6 de 7];
#   a. Deve-se remover o primeiro paciente da fila e imprimir uma mensagem chamando o paciente para atendimento informando o número do seu cartão.

    def atenderPaciente(self):
        if self.head is None:
            print("A lista está vazia!")
        else:
            print(f'Chamando paciente com cartão número: {self.head.numero}')
            self.head = self.head.proximo

#G. Deve-se implementar um menu para utilização do sistema em que: [EXIGÊNCIA DE CÓDIGO 7 de 7];
#   a. Deve-se apresentar as opções (1 – adicionar paciente a fila, 2 – mostrar pacientes na fila, 3 – chamar paciente, 4 – sair)
#   b. Se escolhida a opção 1, chamar a função inserir().
#   c. Se escolhida a opção 2, chamar a função imprimirListaEspera().
#   d. Se escolhida a opção 3, chamar a função atenderPaciente().
#   e. Se escolhida a opção 4, encerrar o programa.
#   f. Se escolhida uma opção diferente as opções disponíveis, voltar ao item .a.

# Função programa que executa um menu de interação para o usuário
def programa():
    Teste = ListaEncadeadaSimples() #Durante as aulas o professor instanciou a Lista encadeada fora da função principal, não consegui entender o motivo e aqui achei mais correto instanciar
    #dentro da função principal.

    while True:
        print('1 - Adicionar paciente à fila')
        print('2 - Mostrar pacientes na fila')
        print('3 - Chamar paciente')
        print('4 - Sair')

        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Tente novamente.")
            continue

        if op == 1:
            Teste.inserir()
        elif op == 2:
            Teste.imprimirListaEspera()
        elif op == 3:
            Teste.atenderPaciente()
        elif op == 4:
            print('Encerrando...')
            break
        else:
            print("Selecione outra opção!\n")


# construtor em python que desencadeia toda a execução do programa
if __name__ == "__main__":
    programa()
