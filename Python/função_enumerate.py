#--------------------------------------------------------------------------------
# Este código demonstra o uso da função enumerate para iterar sobre uma lista, 
# além de gerar e imprimir múltiplos de três em um intervalo específico.
#--------------------------------------------------------------------------------

print('\n-----------------\n')

print('Função Enumerate')

# Lista de números pares
L = [2, 4, 6, 8]

# Utilizando enumerate para obter o índice (x) e o valor (e) de cada elemento na lista
for x, e in enumerate(L):
    print(f"{x} é a posição de {e}")  # Imprime a posição e o valor correspondente

print('\n-----------------\n')

print('Multiplos de três')

# Gera e imprime múltiplos de 3 entre 3 e 30
for v in range(3, 33, 3):
    print(v, end=",")  # Imprime os valores em uma única linha, separados por vírgula
print()  # Adiciona uma nova linha ao final da impressão
