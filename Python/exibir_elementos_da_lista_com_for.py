#----------------------------------------------------------------------------------------------------
# Este código cria uma lista vazia e permite que o usuário insira números para adicioná-los à lista. 
# O loop continua até que o usuário insira 0, momento em que a lista é exibida e o programa termina.
#----------------------------------------------------------------------------------------------------

L = []  # Inicializa uma lista vazia
x = 0   # Contador de elementos na lista

while True:  # Inicia um loop infinito
    n = int(input('\nInsira um número para adicionar a lista:'))  # Solicita ao usuário um número
    if n == 0:  # Verifica se o número inserido é 0
        print('\nLista finalizada\n')  # Informa que a lista foi finalizada
        break  # Encerra o loop
    L.append(n)  # Adiciona o número à lista
    x += 1  # Incrementa o contador

# Exibe os números armazenados na lista
for e in L:  # Itera sobre cada elemento na lista
    print(e)  # Imprime o elemento atual

