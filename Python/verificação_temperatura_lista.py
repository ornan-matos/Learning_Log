#------------------------------------------------------------------------------------------------------
# Este código encontra a temperatura máxima, mínima e calcula a temperatura média a partir de 
# uma lista de valores. A lista T contém temperaturas em graus Celsius. O código percorre a 
# lista, identifica os valores extremos (máximo e mínimo) e, ao final, calcula a média das temperaturas.
#------------------------------------------------------------------------------------------------------

T = [-10, -8, 0, 1, 2, 23, 5, -15, -2, -4]  # Lista de temperaturas em graus Celsius

maximo = T[0]  # Inicializa a variável maximo com o primeiro valor da lista
minimo = T[0]  # Inicializa a variável minimo com o primeiro valor da lista
soma = 0  # Inicializa a soma das temperaturas com 0

# Percorre cada valor x na lista T
for x in T:
    
    if x > maximo:  # Se x for maior que o valor atual de maximo, atualiza maximo
        maximo = x
    if x < minimo:  # Se x for menor que o valor atual de minimo, atualiza minimo
        minimo = x
    
    soma = soma + x  # Soma o valor de x à soma total das temperaturas

# Exibe a temperatura máxima, mínima e a média
print(f'Temperatura Máxima: {maximo}°C')
print(f'Temperatura Minima: {minimo}°C')
# A média é calculada dividindo a soma pelo número de temperaturas
print(f'Temperatura Média: {soma / len(T)}°C')  


