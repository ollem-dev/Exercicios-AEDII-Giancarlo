class Nodo:
    def __init__(self, dado):
        self.info = dado
        self.proximo = None
class ListEnc:
    def __init__(self):
        self.inicio = None

    def vazia(self):
        return self.inicio is None
    
    def insere_inicio(self, dado):
        novo_Nodo = Nodo(dado)
        novo_Nodo.proximo = self.inicio
        self.inicio = novo_Nodo

    def exibir(self):
        atual = self.inicio

        while atual is not None:
            print(atual.info, end=' -> ')
            atual = atual.proximo

        print("None")

    def insere_na_posicao_k(self, dado, k):
        novo_Nodo = Nodo(dado)

        if self.vazia():
            self.insere_inicio(dado)
            return True
        
        aux = self.inicio
        cont = 0

        while aux.proximo is not None and cont < k - 1:
            aux = aux.proximo
            cont += 1
        novo_Nodo.proximo = aux.proximo
        aux.proximo = novo_Nodo

        if aux is None:
            print('Posição inválida')
            return False

        return True