#------------------------------------------------------------------------------------------------------
# Este código verifica se um número inteiro fornecido pelo usuário está presente em uma lista fixa.
# Se o número for encontrado, uma mensagem indicando sua presença é exibida; caso contrário, 
# uma mensagem indicando sua ausência é mostrada.
#------------------------------------------------------------------------------------------------------

# Lista fixa de números
L = [2, 5, 8, 9]

# Solicita ao usuário um número inteiro entre 0 e 10 para verificação
P = int(input('Insira um número inteiro entre 0 e 10 para ser verificado: '))

# Variável para indicar se o número foi encontrado
achou = False

# Variável para iterar sobre a lista
x = 0

# Loop para percorrer a lista
while x < len(L):
    # Verifica se o número atual na lista é igual ao número fornecido pelo usuário
    if L[x] == P:
        # Marca que o número foi encontrado e encerra o loop
        achou = True
        break
    # Incrementa o índice para verificar o próximo número
    x += 1

# Exibe mensagem com base na verificação
if achou:
    print(f'O número {P} foi encontrado na lista.')
else:
    print(f'O número {P} não foi encontrado na lista.')

