##################################################################################################
#Este programa solicita ao usuário que insira duas strings e, em seguida, compara essas strings
#para determinar se são iguais, diferentes, ou se uma é maior que a outra em ordem lexicográfica.
##################################################################################################

# Solicita ao usuário que insira a primeira string
string1 = input("Digite a primeira string: ")

# Solicita ao usuário que insira a segunda string
string2 = input("Digite a segunda string: ")

# Compara as duas strings para ver se são iguais
if string1 == string2:
    print("As duas strings são iguais.")
# Compara se a primeira string é maior que a segunda
elif string1 > string2:
    print("A primeira string é maior que a segunda.")
# Caso contrário, a segunda string é maior que a primeira
else:
    print("A segunda string é maior que a primeira.")
