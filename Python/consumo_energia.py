#############################################################################
#O programa calcula o valor da conta de energia elétrica com base no 
#tipo de instalação (residencial, comercial ou industrial) e no consumo 
#mensal em kWh (quilowatt-hora). As tarifas variam dependendo do tipo de
#instalação e do consumo, com tarifas mais altas para consumos mais elevados.
#############################################################################

print('Calculo de Energia Eletrica\n')

# Solicita o tipo de instalação ao usuário
print('Tipos de instalação:\n(R) Residencia\n(C) Comercio\n(I) Industria')
instalacao = (input(''))  # Lê a entrada do usuário

# Solicita o consumo mensal em kWh
consumo = int(input('\nValor de KWh consumidos por mês: '))

# Verifica o tipo de instalação e calcula a conta de acordo com as tarifas
if instalacao == 'R':  # Instalação Residencial
    if consumo <= 500:
        conta = 0.45 * consumo  # Tarifa de R$0,45 por kWh para consumo até 500 kWh
    else:
        conta = 0.65 * consumo  # Tarifa de R$0,65 por kWh para consumo acima de 500 kWh

    print(f'\nInstalação: Residencial\nConsumo mensal: {consumo}KWh\nTotal a pagar: R${conta:.2f}')  # Exibe o resultado formatado

elif instalacao == 'C':  # Instalação Comercial
    if consumo <= 1000:
        conta = 0.55 * consumo  # Tarifa de R$0,55 por kWh para consumo até 1000 kWh
    else:
        conta = 0.60 * consumo  # Tarifa de R$0,60 por kWh para consumo acima de 1000 kWh

    print(f'\nInstalação: Comercial\nConsumo mensal: {consumo}KWh\nTotal a pagar: R${conta:.2f}')  # Exibe o resultado formatado

elif instalacao == 'I':  # Instalação Industrial
    if consumo <= 5000:
        conta = 0.55 * consumo  # Tarifa de R$0,55 por kWh para consumo até 5000 kWh
    else:
        conta = 0.60 * consumo  # Tarifa de R$0,60 por kWh para consumo acima de 5000 kWh

    print(f'\nInstalação: Industrial\nConsumo mensal: {consumo}KWh\nTotal a pagar: R${conta:.2f}')  # Exibe o resultado formatado

else:  # Opção inválida
    print('\nDesculpe, opção não encontrada. Tente novamente.')
