#---------------------------------------------------------------------------------------
# Este programa em Python valida uma sequência de parênteses fornecida pelo usuário.
# Ele verifica se todos os parênteses abertos têm um correspondente de fechamento, 
# garantindo que a expressão esteja corretamente balanceada.
#---------------------------------------------------------------------------------------

# Solicita ao usuário a sequência de parênteses a ser validada
expressão = input("Digite a sequência de parênteses a validar:")

# Inicializa um contador para percorrer a string e uma pilha vazia para armazenar os parênteses
x = 0
pilha = []

# Loop para percorrer cada caractere da expressão
while x < len(expressão):
    # Se encontrar um parêntese de abertura, empilha
    if expressão[x] == "(":
        pilha.append("(")
    
    # Se encontrar um parêntese de fechamento, verifica se há correspondente na pilha
    if expressão[x] == ")":
        if len(pilha) > 0:
            # Remove o parêntese correspondente da pilha
            topo = pilha.pop(-1)
        else:
            # Se não houver correspondente, força o erro empilhando um parêntese de fechamento
            pilha.append(")")
            break
    
    # Avança para o próximo caractere
    x = x + 1

# Se a pilha estiver vazia ao final, todos os parênteses foram balanceados
if len(pilha) == 0:
    print("OK")  # Sequência válida
else:
    print("Erro")  # Sequência inválida