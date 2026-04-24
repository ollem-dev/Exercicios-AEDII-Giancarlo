class Descritor:
    def __init__(self, capacidade):
        self.ini = -1
        self.fim = -1
        self.n = 0
        self.max = capacidade
        self.maior = -float('inf')
        self.menor = float('inf')

class ListaComDescritor:
    def __init__(self, capacidade):
        # Operação: inicializa (tamanho)
        self.vetor = [None] * capacidade
        self.desc = Descritor(capacidade)

    def vazia(self):
        return self.desc.n == 0

    def cheia(self):
        return self.desc.n == self.desc.max

    def insere(self, dado, posicao):
        if self.cheia() or posicao < 1 or posicao > self.desc.n + 1:
            return False
        
        if self.vazia():
            self.desc.ini = 0
            self.desc.fim = 0
        else:
            # Deslocamento físico (Shifting)
            indice_alvo = self.desc.ini + posicao - 1
            for i in range(self.desc.fim, indice_alvo - 1, -1):
                self.vetor[i + 1] = self.vetor[i]
            self.desc.fim += 1

        self.vetor[self.desc.ini + posicao - 1] = dado
        self.desc.n += 1
        return True

    def remove(self, posicao):
        if self.vazia() or posicao < 1 or posicao > self.desc.n:
            return False

        indice_rem = self.desc.ini + posicao - 1
        
        # Shifting para a esquerda
        for i in range(indice_rem, self.desc.fim):
            self.vetor[i] = self.vetor[i + 1]
        
        self.vetor[self.desc.fim] = None
        self.desc.fim -= 1
        self.desc.n -= 1
        
        if self.desc.n == 0:
            self.desc.ini = -1
            self.desc.fim = -1
        return True

    def consulta(self, valor):
        """Retorna a posição de um valor (Busca por conteúdo)"""
        for i in range(self.desc.ini, self.desc.fim + 1):
            if self.vetor[i] == valor:
                return i - self.desc.ini + 1
        return -1

    def acessa(self, posicao):
        """Retorna o dado de uma posição (Busca por índice)"""
        if posicao < 1 or posicao > self.desc.n:
            return None
        return self.vetor[self.desc.ini + posicao - 1]