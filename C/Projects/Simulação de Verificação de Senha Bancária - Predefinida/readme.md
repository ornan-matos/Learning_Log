# Simulação de Verificação de Senha Bancária Predefinida

Este projeto consiste em um programa em linguagem C que simula um micro-processo de verificação de senha em uma aplicação bancária. O código utiliza uma senha predefinida e permite ao usuário tentar inserir a senha correta por até três vezes. O objetivo é fornecer acesso à aplicação bancária somente se a senha inserida for a correta.

## Funcionamento Detalhado

O programa é implementado da seguinte forma:

1. O código inclui as bibliotecas padrão `stdio.h`, `stdlib.h` e `string.h`.

2. A senha predefinida é armazenada como uma constante `char` array chamada `senha` com o valor `"Wst3_54#"`. Usar uma constante para armazenar a senha é uma boa prática, pois protege a senha de ser modificada acidentalmente no código.

3. O programa entra na função principal `main()`.

4. São declaradas as variáveis necessárias, como `cont` para contar o número de tentativas de senha e `senhaUsr` para armazenar a senha inserida pelo usuário.

5. O programa exibe informações básicas sobre a agência e a conta bancária.

6. Entra em um loop `do-while`, que permite ao usuário inserir a senha até três vezes, ou até a senha correta ser inserida.

7. O usuário é solicitado a inserir a senha usando `printf()` e `scanf()`. A função `getchar()` é usada para capturar o caractere de nova linha após a entrada da senha.

8. A senha inserida pelo usuário é comparada com a senha predefinida usando a função `strcmp()` da biblioteca `string.h`.

9. Se a comparação resultar em valores diferentes de zero (ou seja, senhas diferentes), uma mensagem de senha incorreta é exibida e o contador `cont` é incrementado.

10. Se a senha inserida for idêntica à senha predefinida, o programa exibe uma mensagem de acesso liberado e sai do loop usando a instrução `break`.

11. Após o loop, uma estrutura condicional `if` verifica se o contador `cont` é maior ou igual a 3 (indicando que o usuário excedeu o número máximo de tentativas permitidas).

12. Se o contador for maior ou igual a 3, uma mensagem informando que o máximo de tentativas foi alcançado é exibida, e o acesso é bloqueado.

13. Finalmente, o programa exibe uma mensagem de encerramento.

## Como Executar

Para executar o programa em sua máquina local, siga estas etapas:

1. Certifique-se de ter um compilador C instalado em seu sistema (por exemplo, GCC).

2. Abra um terminal e navegue até o diretório onde o arquivo `.c` está localizado.

3. Compile o código usando o seguinte comando: `gcc Predefined_Password_Test.c -o Password_Test`.

4. Execute o programa com o comando: `./Password_Test`.

## Conclusão

Este projeto demonstra a implementação de um processo simples de verificação de senha em uma aplicação bancária simulada. Ele utiliza conceitos fundamentais de manipulação de strings, loops e estruturas condicionais em linguagem C. O código oferece aos usuários três tentativas para inserir a senha correta antes de bloquear o acesso.

## Observações

- Certifique-se de usar um ambiente de teste adequado para a execução do programa.
- Este programa é uma simulação didática e não deve ser usado para fins de segurança real.
- O código pode ser otimizado e aprimorado para melhor legibilidade e eficiência.


**Ornan Matos**  
**ornanmatos@outlook.com**  
**ornan.dev**