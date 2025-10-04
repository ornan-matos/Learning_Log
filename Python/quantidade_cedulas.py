# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
#
# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
#
# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
#

valor = int(input())
resto = valor
notas = 0
print(valor)

print(f"{resto // 100} nota(s) de R$ 100,00")
resto %= 100


print(f"{resto // 50} nota(s) de R$ 50,00")
resto %= 50


print(f"{resto // 20} nota(s) de R$ 20,00")
resto %= 20


print(f"{resto // 10} nota(s) de R$ 10,00")
resto %= 10


print(f"{resto // 5} nota(s) de R$ 5,00")
resto %= 5


print(f"{resto // 2} nota(s) de R$ 2,00")
resto %= 2


print(f"{resto // 1} nota(s) de R$ 1,00")
