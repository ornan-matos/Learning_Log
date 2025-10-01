##################################
# Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.
# A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.
# A saída contém apenas um valor inteiro.
# Exemplo de Entrada	Exemplo de Saída

# Entrada
# 3 2
# 3 -1 0 -2 2

# Saída
# 7
# 7
n = 0
a = 0
soma = 0

L = input().split()
a = int(L[0])

for e in L[1:]:
    if int(e) > 0:
        n = int(e)
        break

for i in range(n):
    soma += a + i

print(soma)
