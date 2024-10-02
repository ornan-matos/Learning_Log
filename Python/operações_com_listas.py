#---------------------------------------------------------------------------------------------
# Este código encontra o maior e o menor valor em uma lista de números inteiros.
# A lista é percorrida duas vezes: a primeira para encontrar o maior valor e a 
# segunda para encontrar o menor valor.
#---------------------------------------------------------------------------------------------

# Lista de números inteiros
L = [2, 10, 4, 1, 6, 8]

# Inicializa as variáveis 'max' e 'min' com o primeiro elemento da lista
max = L[0]
min = L[0]

# Percorre a lista para encontrar o maior valor
for e in L:
    if e > max:
        max = e  # Atualiza 'max' se encontrar um valor maior

# Percorre a lista para encontrar o menor valor
for d in L:
    if d < min:
        min = d  # Atualiza 'min' se encontrar um valor menor

# Exibe o maior valor encontrado
print(f'\nMaior valor da lista: {max}')

# Exibe o menor valor encontrado
print(f'\nMenor valor da lista: {min}')
