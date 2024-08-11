
#include <stdio.h>

/* 
O programa calcula a média de uma série de números inseridos pelo usuário.
O usuário insere a quantidade de números que deseja fornecer e, em seguida,
insere cada um desses números. O programa usa um loop para coletar os números,
soma-os e calcula a média, exibindo o resultado ao final.
*/

int main() {
    int n;  // Variável para armazenar a quantidade de números
    double sum = 0.0;  // Variável para armazenar a soma dos números
    double number;  // Variável para armazenar o número atual inserido pelo usuário

    // Solicita ao usuário que insira a quantidade de números
    printf("Quantos números você deseja inserir? ");
    scanf("%d", &n);

    // Loop para coletar os números inseridos pelo usuário
    for (int i = 1; i <= n; i++) {
        printf("Digite o número %d: ", i);
        scanf("%lf", &number);
        sum += number;  // Adiciona o número à soma total
    }

    // Calcula a média dos números inseridos
    double average = sum / n;

    // Exibe a média
    printf("A média dos números inseridos é: %.2f\n", average);

    return 0;  // Indica que o programa terminou com sucesso
}
