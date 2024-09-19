#-----------------------------------------------------------
# Este código verifica se dois números fornecidos pelo usuário 
# (p e v) estão presentes em uma lista (L1).
# O programa informa qual número foi encontrado primeiro e, 
# se o segundo número também estiver na lista,
# informa sua presença. O código utiliza um loop while para percorrer
# os elementos da lista.
#-----------------------------------------------------------

L1 = [1, 3, 5, 7, 9]  # Lista de números a serem verificados

# Solicita ao usuário o primeiro número
p = int(input('\nPrimeiro Número: '))

# Solicita ao usuário o segundo número
v = int(input('\nSegundo Número: '))

x = 0  # Inicializa o índice para percorrer a lista

# Loop para percorrer a lista enquanto o índice x for menor que o comprimento da lista
while x < len(L1):
    
    # Verifica se o primeiro número (p) está na lista
    if L1[x] == p:
        print(f'\nO número {p} foi encontrado.\nO P foi encontrado primeiro.\nE está na posição {x}')
        
        # Loop para verificar se o segundo número (v) também está na lista a partir do índice atual
        while x < len(L1):
            if L1[x] == v:
                print(f'\nO número {v} também foi encontrado.\nE está na posição {x}')
                break  # Sai do loop se o número v for encontrado
            x += 1  # Avança para o próximo índice
        
        break  # Sai do loop principal

    # Verifica se o segundo número (v) está na lista
    elif L1[x] == v:
        print(f'\nO número {v} foi encontrado.\n O V foi encontrado primeiro.\nE está na posição {x}')
        
        # Loop para verificar se o primeiro número (p) também está na lista a partir do índice atual
        while x < len(L1):
            if L1[x] == p:
                print(f'\nO número {p} também foi encontrado.\nE está na posição {x}')
                break  # Sai do loop se o número p for encontrado
            x += 1  # Avança para o próximo índice
        
        break  # Sai do loop principal
    
    x += 1  # Avança para o próximo índice se nenhum número foi encontrado

