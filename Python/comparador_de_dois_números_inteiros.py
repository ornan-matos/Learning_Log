##############################################################################

#Comparador de Dois Números Inteiros
#Este script compara dois números inteiros
#fornecidos pelo usuário e informa qual deles
#é o maior ou se são iguais.

##############################################################################


# Entrada de dados
x = int(input("Insira o primeiro valor: "))  # Lê o primeiro valor e o converte para inteiro
y = int(input("Insira o segundo valor: "))  # Lê o segundo valor e o converte para inteiro

# Comparação
if x > y:  # Verifica se x é maior que y
    print("\n\tO primeiro valor é maior\n")  # Imprime mensagem se x for maior
if x < y:  # Verifica se x é menor que y
    print("\n\tO segundo valor é maior\n")  # Imprime mensagem se x for menor
# (Opcional) Poderia ser adicionado um terceiro if para o caso de igualdade (x == y)
