###########################################
#Este código em Python recebe um número inteiro 
#do usuário e exibe todos os números ímpares de
#um até esse número. Ele utiliza um laço while 
#para iterar sobre os números e uma estrutura 
#condicional if para verificar se o número é 
#ímpar antes de exibi-lo.
###########################################

# Solicita ao usuário para inserir o último número a ser exibido e converte para inteiro
fim = int(input('Insira o ultimo número a ser exibido: '))

# Inicializa a variável x com valor 1
x = 1

# Inicia um laço while que continua enquanto x for menor ou igual ao valor de fim
while x <= fim:
    # Verifica se o valor de x é ímpar (se o resto da divisão por 2 for diferente de zero)
    if x % 2 != 0:
        # Se x for ímpar, imprime o valor de x
        print(x)
    # Incrementa o valor de x em 1
    x = x + 1


