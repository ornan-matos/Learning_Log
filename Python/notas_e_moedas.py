# Notas e Moedas
#
# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
#
# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
#
# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
#
# Obs: Utilize ponto (.) para separar a parte decimal.


valor = float(input())

resto = valor

print("NOTAS:")

print(f"{int(valor // 100)} nota(s) de R$ 100.00")
resto %= 100

print(f"{int(resto // 50)} nota(s) de R$ 50.00")
resto %= 50

print(f"{int(resto // 20)} nota(s) de R$ 20.00")
resto %= 20

print(f"{int(resto // 10)} nota(s) de R$ 10.00")
resto %= 10

print(f"{int(resto // 5)} nota(s) de R$ 5.00")
resto %= 5

print(f"{int(resto // 2)} nota(s) de R$ 2.00")
resto %= 2

if resto < 2:
    print("MOEDAS:")

    resto *= 100
    print(f"{int(resto // 100)} moeda(s) de R$ 1.00")
    resto %= 100

    print(f"{int(resto // 50)} moeda(s) de R$ 0.50")
    resto %= 50

    print(f"{int(resto // 25)} moeda(s) de R$ 0.25")
    resto %= 25

    print(f"{int(resto // 10)} moeda(s) de R$ 0.10")
    resto %= 10

    print(f"{int(resto // 5)} moeda(s) de R$ 0.05")
    resto %= 5

    print(f"{int(resto // 1)} moeda(s) de R$ 0.01")
