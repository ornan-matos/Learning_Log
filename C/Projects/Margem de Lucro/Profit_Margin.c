#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/*
O programa irá auxiliar no calculo da margem de lucro de produtos em lojas de varejo. 
*/

int main(){
    
    int forneCx; // Quantidade de Caixas.
    int forneQuantUniCx; //Quantidade de unidades em uma caixa.
    int procentLucro; //Margem de lucro do varejista.
    int menu; //Opção escolhida no menu.
    float fornePrecoCx; //Valor total de uma caixa.
    float precoFinal; //Preço final de varejo.
    float valorImaginario; //Valor imaginário do produto para calcular a porcentagem.
    float porcentagem; //Porcentagem de margem de lucro imaginada para o produto.
    char nomeProduto; //Nome do Produto.

    do 
    {
    printf("\n------ Menu Principal ------\n");
    printf("1 - CALCULAR VALOR UNITÁRIO DA MERCADORIA\n"); //Será dividido o valor unitário de cada mercadoria levando em consideração o valor total do caixa.
    printf("2 - CALCULAR PORCENTAGEM DA MARGEM DE LUCRO\n"); //Será calculado o valor da margem de lucro levando em consideração valor da mercadoria e valor aleatório escolhido pelo usuário.
    printf("3 - CALCULAR VALOR FINAL DO PRODUTO COM MARGEM DE LUCRO INCLUSA\n"); //Será calculado o valor final da mercadoria com a margem de lucro do varejista.
    printf("4 - SAIR\n\n"); //O programa obviamente será encerrado.

    printf("Insira a opção escolhida: ");
    scanf("%d", &menu); //Capturar a opção do menu.
    } while (menu == 0 || menu > 4);
    
    if(menu == 1)
    {

        printf("\n\n------ CALCULAR VALOR UNITÁRIO -------\n\n");
        printf("Insira o quantidade de caixas (ou pacotes): ");
        scanf("%d", &forneCx); //Capturar quantidade de caixas.
        printf("\nInsira o quantidade total desse produto: ");
        scanf("%d", &forneQuantUniCx); //Capturar quantidade total unidades de unidades desse produto.
        printf("\nInsira o valor monetário total da(s) caixa(s) (ou pacote): R$ ");
        scanf("%f", &fornePrecoCx); //Capturar valor monetário total de todas as caixas.

            if (forneCx > 1)//Se a quantidade for mais que 1 será necessário essa ação.
            {             
        
            float forneValTotalCx = (forneQuantUniCx * forneCx) / fornePrecoCx; //Será multiplicado a quantidade de unidades de cada caixa vezes a quantidade de unidades por caixa. Depois divido pelo preço total das caixas.
            float forneValUniCx = fornePrecoCx / forneCx; //Preço de cada caixa.
            printf("\n\n------------------------------------\n");
            printf("Quantidade de caixas (ou pacotes): %d\n", forneCx);
            printf("Valor de cada caixa (ou pacote): R$ %.2f\n", forneValUniCx);
            printf("Valor de cada unidade: R$ %.2f\n", forneValTotalCx);           
            }
            
            else
            {
            float forneValTotalCx = forneQuantUniCx / fornePrecoCx; //Calcular preço de cada unidade do fornecedor.
            printf("\n\n------------------------------------\n");
            printf("Quantidade de caixas (ou pacotes): %d\n", forneCx);
            printf("Valor de cada caixa (ou pacote): R$ %.2f\n", fornePrecoCx);
            printf("Valor de cada unidade: R$ %.2f\n", forneValTotalCx);
            }
        
    }
    else if (menu == 2)
    {
       
        printf("\n\n------ CALCULAR PORCENTAGEM DE MARGEM DE LUCRO -------\n\n");
        printf("Insira o quantidade de caixas (ou pacotes): ");
        scanf("%d", &forneCx); //Capturar quantidade de caixas.
        printf("\nInsira o quantidade total desse produto: ");
        scanf("%d", &forneQuantUniCx); //Capturar quantidade total unidades de unidades desse produto.
        printf("\nInsira o valor monetário total da(s) caixa(s) (ou pacote): R$ ");
        scanf("%f", &fornePrecoCx); //Capturar valor monetário total de todas as caixas.
        printf("\nInsira o valor estimado que você pretende vender cada unidade: R$ ");
        getchar(); // Limpa o buffer de entrada
        scanf("%f", &valorImaginario); //Capturar valor monetário total de todas as caixas.
        
        float forneValUniCx = fornePrecoCx / forneCx; //Preço de cada caixa.
        float forneValTotalCx = forneQuantUniCx / forneValUniCx; //Calcular preço de cada unidade do fornecedor.
        
        if(forneValTotalCx < valorImaginario)
        {
            float margemDeLucro = forneValTotalCx * 100 / valorImaginario; //Calcular margem de lucro
        
            printf("\n\nMargem de lucro estimada: %.0f%% \n", margemDeLucro);
        }

        else
        {
            printf("\nNão é possível realizar essa ação.\n");
        }
 
    }
    
    else if (menu == 3)
    {
        printf("\n\n------ CALCULAR VALOR FINAL DO PRODUTO COM MARGEM DE LUCRO INCLUSA -------\n\n");
        printf("Insira o quantidade de caixas (ou pacotes): ");
        scanf("%d", &forneCx); //Capturar quantidade de caixas.
        printf("\nInsira o quantidade total desse produto: ");
        scanf("%d", &forneQuantUniCx); //Capturar quantidade total unidades de unidades desse produto.
        getchar(); // Limpa o buffer de entrada
        printf("\nInsira o valor monetário total da(s) caixa(s) (ou pacote): R$ ");
        scanf("%f", &fornePrecoCx); //Capturar valor monetário total de todas as caixas.
        printf("\nInsira a porcentagem de margem de lucro: ");
        getchar(); // Limpa o buffer de entrada
        scanf("%f", &porcentagem); //Capturar valor monetário total de todas as caixas.

        float forneValUniCx = fornePrecoCx / forneCx; //Preço de cada caixa.
        float forneValTotalCx = forneQuantUniCx / forneValUniCx; //Calcular preço de cada unidade do fornecedor.

        if(porcentagem > 0)
        {
            float margemDeLucro = porcentagem / 100; //Calcular margem de lucro.
            float precoFinal = forneValTotalCx / (1 - margemDeLucro); //Calcular o valor final do produto.
            float lucroLiquido = precoFinal - forneValTotalCx;//Calcular Lucro liquido.
           
            printf("\n\nPreço de venda: R$ %.2f \n", precoFinal);
            printf("\nLucro liquido: R$ %.2f\n", lucroLiquido);
        }

        else
        {
            printf("\nNão é possível realizar essa ação.\n");
        }

    }

    else 
    {
        printf("\nSaindo...\n");
    }
            
return 0;

}