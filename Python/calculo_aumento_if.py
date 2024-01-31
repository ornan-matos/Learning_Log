salario = float(input("Insira o valor do sálario: R$ "))

if salario > 1.250:

    aumento = (salario * (10 / 100)) + salario
    print(f"\nSeu novo salário será: R$ {aumento:6.2f}")

else:

    aumento = (salario * (15 / 100)) + salario
    
    print(f"\nSeu novo salário será: R$ {aumento:6.2f}")


