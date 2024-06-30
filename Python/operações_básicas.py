##################################################################

#Este programa permite ao usuário realizar operações 
#matemáticas básicas (adição, subtração, multiplicação e divisão)
#escolhendo a operação desejada e inserindo os números a serem 
#calculados.

##################################################################

print("\t\nMini Calculadora\n")  # Imprime o título da calculadora

# Exibe o menu de opções para o usuário
print("Qual operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

a = int(input())  # Lê a opção escolhida pelo usuário e converte para inteiro

# Verifica a opção escolhida e executa a operação correspondente
if a == 1:
    x = int(input("Insira o primeiro número: "))  # Lê o primeiro número
    y = int(input("Insira o segundo número: "))   # Lê o segundo número
    print("Total: ", x + y)  # Imprime o resultado da adição

elif a == 2:
    x = int(input("Insira o primeiro número: "))
    y = int(input("Insira o segundo número: "))
    print("Total: ", x - y)  # Imprime o resultado da subtração

elif a == 3:
    x = int(input("Insira o primeiro número: "))
    y = int(input("Insira o segundo número: "))
    print("Total: ", x * y)  # Imprime o resultado da multiplicação

elif a == 4:
    x = int(input("Insira o primeiro número: "))
    y = int(input("Insira o segundo número: "))
    print("Total: ", x / y)  # Imprime o resultado da divisão

# Caso a opção seja inválida, exibe uma mensagem de erro
else:
    print("Desculpe, opção invalida.")
