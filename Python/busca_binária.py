# ------------------------------------------------------------------
# Programa para verificar se o DDD inserido corresponde a algum código
# de área de uma capital do Nordeste do Brasil. O código utiliza uma
# busca binária em uma lista de DDDs para encontrar a correspondência.
# Se encontrado, exibe a cidade correspondente; caso contrário, informa
# que o DDD não foi encontrado.
# ------------------------------------------------------------------

# Mensagem de introdução para o usuário
print('-- Verifique se o DDD escolhido corresponde ao código de área de alguma capital do Nordeste do Brasil -- ')

# Lista de códigos de área (DDDs) das capitais do Nordeste do Brasil
lista = [71, 79, 81, 82, 83, 84, 85, 86, 98]

# Solicita ao usuário que insira um número (DDD)
item = int(input('\nInsira um número: '))

# Inicializa as variáveis para a busca binária
baixo = 0
alto = len(lista) - 1

# Inicia a busca binária
while baixo <= alto:

    # Calcula o índice do meio da lista
    meio = (baixo + alto) // 2
    # Obtém o valor do DDD no índice do meio
    chute = lista[meio] 

    # Verifica se o usuário inseriu 0 para finalizar o programa
    if item == 0:
        print('\nPrograma finalizado!')
        break

    # Verifica se o DDD inserido corresponde ao DDD no meio da lista
    if chute == item:
        print('\nAchamos o DDD!\n')
        
        # Exibe a cidade correspondente ao DDD encontrado
        if item == 71:
            print(f'O DDD ({item}) corresponde a Salvador - BA')
        elif item == 82:
            print(f'O DDD ({item}) corresponde a Maceió - AL')
        elif item == 85:
            print(f'O DDD ({item}) corresponde a Fortaleza - CE')
        elif item == 86:
            print(f'O DDD ({item}) corresponde a Teresina - PI')
        elif item == 98:
            print(f'O DDD ({item}) corresponde a São Luís - MA')
        elif item == 84:
            print(f'O DDD ({item}) corresponde a Natal - RN')
        elif item == 83:
            print(f'O DDD ({item}) corresponde a João Pessoa - PB')
        elif item == 79:
            print(f'O DDD ({item}) corresponde a Aracaju - SE')
        elif item == 81:
            print(f'O DDD ({item}) corresponde a Recife - PE')
        
        # Encerra o loop ao encontrar o DDD
        break

    # Ajusta os limites da busca binária conforme o valor do DDD
    elif chute > item:
        alto = meio - 1
    else:
        baixo = meio + 1

# Se o loop termina sem encontrar o DDD, exibe mensagem de não encontrado
else:
    print('\nItem não encontrado!')


