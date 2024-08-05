#---------------------------------------------------------------------------------------------
# Um palíndromo é uma palavra, frase, número ou outra sequência de caracteres que
# pode ser lido da mesma forma de frente para trás e de trás para frente. 
# O programa e irá verificar se a string inserida em formato de número é um palíndromo ou não.
#---------------------------------------------------------------------------------------------

# Solicita ao usuário que insira um número
string = input('Insira um número: ')

# Inicializa os índices para a comparação dos caracteres
i = 0
f = len(string) - 1

# Loop para comparar os caracteres das extremidades em direção ao centro
while f > i and string[i] == string[f]:
    # Move os índices em direção ao centro
    i += 1
    f -= 1

    # Se ainda restam caracteres para comparar
    if string[i] == string[f]:
        # Se todos os caracteres coincidem, a string é um palíndromo
        print(f'O número {string} é um palíndromo')
        break
else:
    # Se algum par de caracteres não coincide, a string não é um palíndromo
    print(f'O número {string} não é um palíndromo')

