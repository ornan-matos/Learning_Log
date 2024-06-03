"""
Calculadora de Distância Percorrida pela Terra

Este script calcula a distância percorrida pela Terra em metros, dado um período de tempo em horas.

Funcionamento:

1. Entrada de Dados: O programa solicita ao usuário que insira a quantidade de horas desejada.
2. Cálculo da Distância:
   - A velocidade da Terra em sua órbita é considerada constante e aproximada para 30.000 km/s (quilômetros por segundo).
   - A velocidade é convertida para metros por segundo (m/s): 30.000 km/s * 1000 m/km = 30.000.000 m/s.
   - A distância percorrida em uma hora é calculada: 30.000.000 m/s * 60 s/min * 60 min/h = 108.000.000.000 m/h.
   - A distância total é obtida multiplicando a distância por hora pela quantidade de horas fornecida pelo usuário.
3. Saída de Dados: O programa exibe a distância percorrida em metros, formatada de maneira clara.
"""

print("\tDistância Percorrida Pela Terra em Metros\n")

#Entrada de dados
horas = int(input("Insira a quantidade de horas:"))

#Calculo da distância em metros
# 1km = 1000m
# 1 minuto = 60 segundos
# 1 hora = 60 minutos
distancia_final = ((30000 * 60) * 60) * horas

#Imprimindo resultado na tela
print(f"\nFoi percorrido em {horas}h a distância de {distancia_final}m")
