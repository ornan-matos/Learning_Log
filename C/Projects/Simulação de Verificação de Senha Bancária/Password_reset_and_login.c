#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
O programa simulara um micro-processo de redefinição e verificação de senha em uma aplicação bancária.
*/

int main(){
    
    int cont = 0;
    int cont2 = 0;
    char senha[20]; // Usar constante para senha predefinida.
    char senhaUsr[20];
    char senhaUsr2[20];

    printf("\n________BANCO GITLAB_______");
    printf("\n\nAgencia:0001-1\nConta:3233-56");

    do //Estrutura de repetição de teste final para que tem o objetivo de simular a criação de uma nova senha.
    {
        printf("\n\n--REDEFINA SUA SENHA--\n");
        printf("\nNova senha: "); 
        scanf("%s", &senhaUsr);//a primeira sequencia de caracteres sera escaneada e salva nessa variável. 
        getchar();
        int tamanho = strlen(senhaUsr);

        if (tamanho <= 20 | tamanho >= 7);//Por segurança será medido o tamanho da senha. 
        {
            printf("\nRepita a nova senha: "); 
            scanf("%s", &senhaUsr2); //a segunda sequencia de caracteres sera escaneada e salva nessa variável.
            getchar();
        }

         if(strcmp(senhaUsr, senhaUsr2) != 0)//se as senhas forem diferente o programa irá avisar.
        {
            printf("\nSenhas diferentes.\n\nTente novamente!\n");
            cont2++; //adicionar um o contador de tentativas
        }

        if(cont2 >= 3 ) //Se numero de tentativas for maior que três o programa irá para em todas as instancias restantes.
        {
           printf("\nDesculpe, numero máximo de tentativas \npara criar uma nova senha foi esgotado.\nTente novamente mais tarde.\n");

           break;
        }
        

    } while (strcmp(senhaUsr, senhaUsr2) != 0); //Se as senhas forem diferentes o loop continuara.
    
    
    do
    {
        if (cont2 >= 3)
        {
            break;
        }
        
        
        printf("\n---- Novo Login ----\n");
        printf("\nSenha: "); 
        scanf("%s", &senha);
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

    if (cont >= 3 | cont2 >= 3) //Estrutura de decisão simples, sera exibida caso o contador de tentativas for igual ou maior que três.
    {
        printf("\nMáximo de tentativa alcançada.\nAcesso bloqueado.");
    }
    
    printf("\nFim do Processo...\n");

    return 0;    

}