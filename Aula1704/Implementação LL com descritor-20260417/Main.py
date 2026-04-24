from TAD_LL_descritor import ListaComDescritor

# Criando a lista (Operação inicializa)
minha_lista = ListaComDescritor(10)

print("--- Testando Inserções ---")
minha_lista.insere(10, 1)
minha_lista.insere(15, 2)
minha_lista.insere(12, 2) # Insere no meio
minha_lista.insere(1, 4) # Insere no Final
minha_lista.insere(3, 1) # Insere no Inicio

print(f"Vetor Físico: {minha_lista.vetor}")
print(f"Quantidade de elementos (n): {minha_lista.desc.n}")

print("\n--- Testando Acesso e Consulta ---")
dado = minha_lista.acessa(2)
print(f"Dado na posição 2: {dado}") # Deve ser 'B'

pos = minha_lista.consulta("C")
print(f"O valor 'C' está na posição: {pos}") # Deve ser 3

print("\n--- Testando Remoção ---")
minha_lista.remove(1) # Remove 'A'
print(f"Vetor após remover posição 1: {minha_lista.vetor}")
print(f"Novo Início: {minha_lista.desc.ini}, Novo Fim: {minha_lista.desc.fim}")

