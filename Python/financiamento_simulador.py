############################################################################
#O código simula a aprovação de um financiamento imobiliário, verificando se 
#a parcela mensal se encaixa dentro de um limite percentual da renda
#do solicitante. Caso a parcela seja igual ou inferior a 30% da renda,
#o financiamento é aprovado, e o valor da parcela e a duração são 
#exibidos. Caso contrário, o financiamento é negado.
#############################################################################

print('-- Financiamento de Imovel --\n')  # Título do programa

# Solicitação de dados do usuário
salario = float(input('Insira o valor da sua renda mensal R$ '))
casa = float(input('Insira o valor do imovel R$ '))
meses = int(input('Isira a quantidade de meses na qual deseja parcelar: '))

# Cálculo da porcentagem da parcela em relação à renda
porcentagem = ((casa / meses) / salario) * 100

# Verificação de aprovação do financiamento
if porcentagem <= 30:
    # Financiamento aprovado: exibe mensagem de sucesso e detalhes do financiamento
    print(f'\nParabéns! Você está autorizado a realizar o financiamento do imovel.\nPagando apenas suaves prestções de R${casa / meses:.3f} \nDurante {meses} meses')
else:
    # Financiamento negado: exibe mensagem de insucesso
    print('\nQue pena... Você não atende os requisitos minimos para realizar o financiamento.\nTente novamente em outra oportunidade.')
