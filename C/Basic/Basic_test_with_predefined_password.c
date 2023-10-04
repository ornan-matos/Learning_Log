#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*
O programa irá testar três vezes uma senha predefinida.
*/

int main(){

    char senha[8];
    int cont = 0;

    for (cont = 1; cont <= 3; cont++)
    {
        printf("\nDigite a senha predefinida: ");
        scanf("%s", &senha);
        getchar();

        if (strcmp(senha, "qwer4321") == 0)
        {
            printf("\nParabéns Acesso Liberado!\n");
            break;
        }
        else
        {
            printf("\nTente Novamente!\n");
        }
        
    }
    return 0;
}