# ---------------------------------------------------------------------------
# Simulador de fila de atendimento
# O programa gerencia uma fila simples de clientes, onde o usuário pode:
# - Adicionar clientes ao final da fila (F)
# - Atender o cliente no início da fila (A)
# - Encerrar o programa (S)
# ---------------------------------------------------------------------------

# Define o número do último cliente inicialmente na fila
ultimo = 10

# Cria a fila inicial com os clientes de 1 até 10
fila = list(range(1, ultimo + 1))

# Início do laço principal do programa (loop infinito até que o usuário digite 'S')
while True:
    # Exibe a quantidade de clientes e a fila atual
    print(f"\nExistem {len(fila)} clientes na fila")
    print("Fila atual:", fila)

    # Instruções para o usuário
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendido. S para sair.")

    # Lê a string de operações digitada pelo usuário
    op = input("Operação (F, A ou S):")

    # Inicializa variáveis de controle para cada loop
    x = 0  # Índice da string de operações
    novos = 0  # Contador de novos clientes adicionados
    atendimentos = 0  # Contador de clientes atendidos
    erros = 0  # Contador de erros (não utilizado)
    sair = False  # Flag para verificar se o programa deve ser encerrado

    # Loop interno para processar cada caractere da string de entrada
    while x < len(op):

        # Caso seja uma operação de atendimento (A) e haja alguém na fila
        if op[x:x+1] == "A" and len(fila) > 0:
            atendimentos += 1
            fila.pop(0)  # Remove o primeiro cliente da fila

        # Caso seja uma operação para adicionar cliente (F)
        elif op[x:x+1] == "F":
            novos += 1
            ultimo += 1  # Incrementa o número do último cliente
            fila.append(ultimo)  # Adiciona novo cliente ao fim da fila

        # Caso o usuário deseje sair (S)
        elif op[x:x+1] == "S":
            sair = True  # Marca que é hora de sair do programa
            break  # Interrompe o processamento da string de operações

        # Qualquer outro caractere é considerado inválido
        else:
            print(f"Opção inválida detectada na fila. Tente novamente!")
            break  # Sai do processamento da string de operações

        x += 1  # Avança para o próximo caractere

    # Exibe um resumo das operações realizadas
    print("-" * 10)
    print(f"Cliente(s) atendido(s): {atendimentos}")
    print(f"Cliente(s) novos adicionado(s): {novos}\n")

    # Se a fila estiver vazia, informa ao usuário
    if len(fila) < 1:
        print("Fila vazia, ninguém para atender!")

    # Se foi solicitada a saída, encerra o programa
    elif sair == True:
        print("Saindo do programa!")
        break  # Sai do loop principal
