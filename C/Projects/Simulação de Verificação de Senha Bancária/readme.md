# Simulação de Verificação de Senha Bancária

Este é um projeto em linguagem C que simula um processo de verificação de senha em uma aplicação bancária básica. O programa permite que os usuários redefinam suas senhas e realizem login após a redefinição. O objetivo é demonstrar conceitos simples de manipulação de strings, estruturas de repetição e decisões em C.

## Funcionamento

O programa possui dois loops principais: um para redefinir a senha e outro para realizar o login. O processo é detalhado abaixo:

### Redefinindo a Senha

1. O programa começa exibindo as informações da agência e conta fictícias do "Banco GitLab".

2. O usuário é solicitado a definir uma nova senha.

3. A senha é escaneada e armazenada na variável `senhaUsr`.

4. O programa verifica se o tamanho da senha está dentro dos limites (entre 7 e 20 caracteres). Essa verificação é feita usando a função `strlen()` para obter o tamanho da senha.

5. Se a senha estiver dentro dos limites, o usuário é solicitado a repeti-la para confirmação. A segunda senha é escaneada e armazenada em `senhaUsr2`.

6. As duas senhas (senhaUsr e senhaUsr2) são comparadas usando a função `strcmp()`. Se elas forem diferentes, o programa informa ao usuário e incrementa o contador `cont2`.

7. Se `cont2` atingir o valor de 3 (ou seja, o usuário tentou confirmar a nova senha incorretamente três vezes), o programa informa que o número máximo de tentativas foi alcançado e sai do loop.

8. O loop continua enquanto as senhas forem diferentes (`strcmp(senhaUsr, senhaUsr2) != 0`).

### Realizando o Login

1. O usuário é solicitado a inserir a senha criada anteriormente para fazer login.

2. A senha inserida é armazenada na variável `senha`.

3. A senha inserida é comparada com a senha definida anteriormente (senhaUsr) usando `strcmp()`. Se as senhas forem diferentes, o programa informa ao usuário e incrementa o contador `cont`.

4. Se a senha inserida for igual à senha definida anteriormente, o programa permite o acesso e exibe uma mensagem de boas-vindas.

5. O loop de login continuará até que o contador `cont` atinja o valor de 3 (ou seja, o usuário inseriu a senha incorreta três vezes).

### Encerramento

1. Após a conclusão dos loops ou atingir o número máximo de tentativas, o programa exibirá uma mensagem de término.

2. Se o usuário tiver excedido o número máximo de tentativas para redefinir a senha ou fazer login, uma mensagem de acesso bloqueado será exibida.

## Compilação e Execução

Para compilar e executar o programa, você pode seguir as etapas abaixo:

1. Certifique-se de ter um compilador C instalado em seu sistema (por exemplo, GCC).

2. Abra um terminal Linux.

3. Navegue até o diretório onde o arquivo do programa (por exemplo, `Password_reset_and_login.c`) está localizado.

4. Execute o seguinte comando para compilar o programa:
   ```
   gcc Password_reset_and_login.c -o password_reset main.c
   ```

5. Após a compilação bem-sucedida, execute o programa:
   ```
   ./password_reset
   ```

## Observações

- Certifique-se de usar um ambiente de teste adequado para a execução do programa.
- Este programa é uma simulação didática e não deve ser usado para fins de segurança real.
- O código pode ser otimizado e aprimorado para melhor legibilidade e eficiência.

---
*Este projeto foi desenvolvido por [Ornan Matos] e está disponível em [https://gitlab.com/ornan-matos/leraning-log]*
