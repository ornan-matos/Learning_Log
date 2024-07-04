####################################################
#Este programa conta quantas vezes um 
#caractere específico aparece em uma 
#frase inserida pelo usuário.
####################################################

print('____ Contagem de Caractere ____\n')

# Solicita ao usuário que insira a frase e o caractere a ser verificado
frase = input('Insira a frase: ')
cart = input('Insira o caractere a ser verificado:')

# Calcula o comprimento da frase
fim = len(frase) 

# Inicializa a variável resultado para contar as ocorrências do caractere
resultado = 0

# Inicializa o contador para percorrer a frase
num = 0

# Loop para percorrer cada caractere da frase
while num < fim:
    # Verifica se o caractere na posição num é igual ao caractere a ser verificado
    if frase[num] == cart:
       resultado = resultado + 1  # Incrementa o resultado se encontrar o caractere

    num = num + 1  # Avança para o próximo caractere na frase

# Imprime o resultado da contagem
print(f'\nO caractere "{cart}" apareceu na frase {resultado} vezes.')

