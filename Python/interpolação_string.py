#-----------------------------------------------------------------------------------------------------
# Este código realiza as seguintes operações:
# 1. Solicita ao usuário que insira um nome e uma letra para verificar se a letra está presente no nome.
# 2. Exibe uma mensagem informando se a letra está ou não presente no nome.
# 3. Mostra o preço de um produto formatado usando interpolação de string.
# 4. Converte um número inteiro fornecido pelo usuário em formato hexadecimal e exibe o resultado.
#-----------------------------------------------------------------------------------------------------

# Solicita ao usuário que insira um nome.
nome = input('Insira o nome: ')

# Solicita ao usuário que insira uma letra para verificação.
letra = input('Qual letra você quer verificar: ')

# Verifica se o nome está vazio e exibe uma mensagem de erro, se for o caso.
if nome == '':
    print('\nErro!')
# Verifica se a letra está presente no nome e exibe a mensagem correspondente.
elif letra in nome:
    print(f'\n"{letra} está presente em {nome}"')
# Caso a letra não esteja no nome, exibe uma mensagem indicando a ausência da letra.
else:
    print(f'\n"{letra} não está presente em {nome}"')

# Imprime uma linha de separação para melhor legibilidade.
print('-' * 20)

# Define o preço de um produto.
preco = 23.500890

# Exibe uma introdução para a interpolação de string.
print('\nInterpolação de string\n')

# Utiliza interpolação de string para formatar e exibir o preço da mercadoria com duas casas decimais.
interpolacao = '\n%s, o preço da mercadoria é R$ %.2f' % (nome, preco)
print(interpolacao) 

# Imprime uma linha de separação para melhor legibilidade.
print('-' * 20)

# Exibe uma introdução para a conversão para hexadecimal.
print('\nHexadecimal\n')

# Solicita ao usuário que insira um número inteiro para conversão em hexadecimal.
x = int(input('Qual número inteiro você quer converter em hexadecimal: '))

# Converte o número inteiro para hexadecimal e exibe o resultado.
print('\nO hexadecimal de %d é %x' % (x, x))

