Aqui está o README formatado em Markdown para o projeto em Go que você forneceu:

# Monitor Web HTTP em Go

Este é um projeto de Monitoramento Web HTTP em linguagem Go, que permite verificar o status de um site fornecido e registrar logs simples. Ele fornece um menu de opções para escolher entre iniciar o monitoramento HTTP, registrar logs ou sair do programa.

## Funcionalidades

- Monitoramento HTTP: Verifica o status de um site para determinar se ele está operacional.
- Registro de Logs: Permite registrar informações relevantes do programa.

## Requisitos

- Go (versão 1.11 ou superior recomendada)

## Como Usar

1. Clone este repositório para o seu sistema local:

```bash
$ git clone https://gitlab.com/ornan-matos/leraning-log.git
```

2. Navegue até o diretório clonado:

```bash
$ cd ~/leraning-log/GO/Projects/request (http)/
```

3. Compile e execute o programa:

```bash
$ go run request\ \(http\).go
```

4. Siga as instruções no terminal para interagir com o programa:
   - Informe o seu primeiro e segundo nome.
   - Escolha uma das opções no menu principal:
     - **1:** Iniciar o monitoramento HTTP.
     - **2:** Registrar Logs.
     - **3:** Sair.

## Detalhes do Código

### Estrutura do Código

O projeto consiste em um único arquivo `request (http).go` contendo diversas funções que são utilizadas para exibir informações, coletar entrada do usuário, realizar o monitoramento HTTP e gerenciar o menu.

- `boasVindas()`: Exibe uma mensagem de boas-vindas e a versão do programa.
- `coletarInfo()`: Coleta informações sobre o usuário (primeiro nome) a partir da entrada do terminal.
- `menu()`: Exibe um menu de opções e retorna a escolha do usuário.
- `monitoramentoHttp()`: Inicia o monitoramento HTTP, verifica o status de um site e exibe os resultados.

### Bibliotecas Utilizadas

- `fmt`: Utilizada para formatação e exibição de mensagens no terminal.
- `os`: Utilizada para interagir com o sistema operacional, como sair do programa.
- `net/http`: Utilizada para realizar requisições HTTP e verificar o status do site.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests para melhorias ou correções.

---
## Observações

- Certifique-se de usar um ambiente de teste adequado para a execução do programa.
- Este programa é uma simulação didática e não deve ser usado para fins de segurança real.
- O código pode ser otimizado e aprimorado para melhor legibilidade e eficiência.

**Ornan Matos**  
**ornanmatos@outlook.com**  
**ornan.dev**
