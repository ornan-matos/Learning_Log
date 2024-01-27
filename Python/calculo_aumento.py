print("Calculo aumento de salário\n")

salario = float(input("Valor atual do salário: "))
#Use o caractere % junto com o valor
aumento = float(input("Qual porcetangem voce quer incrementar: ")[:-1])

valor_final = salario + (salario * (aumento / 100))

print(f"\nSalário reajustado: R${valor_final}")
