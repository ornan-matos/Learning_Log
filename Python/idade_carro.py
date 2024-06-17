##############################################################################
#Este script simples em Python solicita ao
#usuário a idade do carro e determina se ele
#é novo ou velho, com base em um critério
#predefinido.
##############################################################################

# Solicita a idade do carro ao usuário
idade = int(input("Insira a idade do seu carro: "))

# Verifica se a idade é menor ou igual a 2 anos
if idade <= 2:
    print("Seu carro é novo")  # Imprime mensagem se for novo

# Verifica se a idade é maior que 2 anos (redundante, pois já foi verificado o contrário)
if idade > 2:
    print("Seu carro é velho")  # Imprime mensagem se for velho
