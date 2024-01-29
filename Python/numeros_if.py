a = int(input("Insira um número inteiro: "))
b = int(input("Insira um número inteiro: "))
c = int(input("Insira um número inteiro: "))

if a > c and b > c:
    print(a)
    print(b)
if b > a and c > a:
    print(b)
    print(c)
if c > a and a > b:
    print(c)
    print(a)
