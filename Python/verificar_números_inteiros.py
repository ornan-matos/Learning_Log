###################################################################
#O programa solicita ao usuário para inserir um número e verifica
#se o número é positivo, negativo ou zero.
###################################################################

# Solicita ao usuário para inserir um número
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    # Se o número for maior que zero, ele é positivo
    print("O número é positivo.")
elif numero < 0:
    # Se o número for menor que zero, ele é negativo
    print("O número é negativo.")
else:
    # Se o número não for maior nem menor que zero, ele é zero
    print("O número é zero.")
