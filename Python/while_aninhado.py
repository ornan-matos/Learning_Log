# Este programa calcula e exibe a soma de todos os pares de números (i, j)
# dentro de um intervalo definido pelo usuário. Usamos dois loops while aninhados
# para calcular a soma de cada par de números.

# Solicita ao usuário para definir o intervalo
menor_valor = int(input("Digite o menor valor do intervalo: "))
maior_valor = int(input("Digite o maior valor do intervalo: "))

# Inicializamos o contador para o valor i
i = menor_valor

# Loop externo: percorre o intervalo definido pelo usuário para o valor i
while i <= maior_valor:
    # Inicializamos o contador para o valor j
    j = menor_valor
    
    # Loop interno: percorre o intervalo definido pelo usuário para o valor j
    while j <= maior_valor:
        # Calcula a soma dos pares (i, j)
        soma = i + j
        
        # Exibe a soma do par (i, j)
        print(f"Soma dos números {i} e {j}: {soma}")
        
        # Incrementa o contador de j
        j += 1
    
    # Incrementa o contador de i
    i += 1
