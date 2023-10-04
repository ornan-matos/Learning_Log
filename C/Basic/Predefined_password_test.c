#include <stdlib.h>
#include <stdio.h>

/*
O programa testa uma senha predefinida.

Senha = 7835
*/

int main()
{
    int senhaReal = 7835;
    int senhaIns;
    printf("\nInsira a senha: ");
    scanf("%d", &senhaIns);
    printf("\n");
    if (senhaReal == senhaIns)
    {
        printf("Acesso liberado!\n\n");
    }
    else
    {
        printf("Acesso negado!\n\n");
    }

    return 0;
}