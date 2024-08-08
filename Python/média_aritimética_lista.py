#-------------------------------------------------------------
# Programa para calcular a média aritmética escolar
# O programa solicita ao usuário que insira 7 notas e calcula
# a média aritmética dessas notas.
#-------------------------------------------------------------

print('\n-- Calcular média aritmética escolar --')

# Inicializa o índice e a soma das notas
x = 0
soma = 0

# Lista com os rótulos das notas
titulo = ['primeira', 'segunda', 'terceira', 'quarta', 'quinta', 'sexta', 'sétima']

# Lista para armazenar as notas
nota = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Loop para entrada das notas
while x < 7:
    # Solicita ao usuário a nota correspondente e converte para float
    nota[x] = float(input(f'\nInsira a {titulo[x]} nota:'))
    
    # Adiciona a nota à soma total
    soma += nota[x]
    
    # Incrementa o índice para a próxima iteração
    x += 1

# Calcula e exibe a média aritmética das notas
print(f'\nA média aritmética do aluno é {soma / x:.2f} pontos')


