#include <stdio.h>  // Biblioteca padrão de entrada e saída
#include <stdlib.h> // Biblioteca padrão para funções de alocação de memória e utilitários
#include <math.h>   // Biblioteca padrão para funções matemáticas (não necessária aqui, mas pode ser útil para futuras alterações)

/*
 Este programa calcula a área de um retângulo com base nas dimensões fornecidas pelo usuário.
 Ele solicita ao usuário que insira a largura e o comprimento do retângulo, calcula a área
 multiplicando essas duas dimensões, e exibe o resultado formatado com duas casas decimais.
 */

// Função principal do programa
int main()
{
    // Declaração da variável para armazenar a largura
    float larg;

    // Solicita ao usuário para inserir as informações necessárias
    printf("Para calcular a area. Insira as seguintes informações.\n");
    printf("\n");

    // Declaração da variável para armazenar o comprimento
    float com;

    // Solicita ao usuário para inserir a largura
    printf("Largura:");
    printf("\n");

    // Lê o valor da largura inserido pelo usuário e o armazena na variável 'larg'
    scanf("%f", &larg);

    // Solicita ao usuário para inserir o comprimento
    printf("Comprimento:");
    printf("\n");

    // Lê o valor do comprimento inserido pelo usuário e o armazena na variável 'com'
    scanf("%f", &com);

    // Calcula a área multiplicando a largura pelo comprimento
    float area = larg * com;

    // Imprime um espaço em branco para melhorar a legibilidade
    printf(" \n");

    // Exibe o resultado da área calculada
    printf("Area: ");
    printf("%.2f", area); // Formata a saída para exibir duas casas decimais
    printf("²\n"); // Exibe o símbolo de unidade quadrada

    // Retorna 0 indicando que o programa terminou com sucesso
    return 0;
}
