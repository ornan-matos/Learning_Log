#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
O programa simulara um micro-processo de verificação de senha em uma aplicação bancária.
*/

int main(){
    
    int cont = 0;
    char const senha[9] = "Wst3_54#"; // Usar constante para senha predefinida.
    char senhaUsr[20];

    printf("\n________BANCO GITLAB_______");
    printf("\n\nAgencia:0001-1\nConta:3233-56");

    do
    {
        printf("\nSenha: "); 
        scanf("%s", &senhaUsr);
        getchar();

        if (strcmp(senha, senhaUsr) != 0)//Comparação entre strings com strcmp.
        {
            printf("\n\nSenha incorreta, tente novamente!\n\n");

            cont++;
        }

        else {
            printf("\n\nAcesso liberado! Bem-vindo!\n\n");
            break; //Parada loop caso as senhas forem iguais.
        }
  
    } while (cont < 3); // Estrutura de repetição de teste final, irá se repetir enquanto o contado estiver abaixo de três tentativas.

    if (cont >= 3) //Estrutura de decisão simples, sera exibida caso o contador de tentativas for igual ou maior que três.
    {
        printf("\nMáximo de tentativa alcançada.\nAcesso bloqueado.");
    }
    
    printf("\n\nFim do Processo...\n");

    return 0;    

}