#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
O programa realiza uma pesquisa com os residentes do município de Giropops, coletando dados sobre gênero, número de filhos e salário.
Funcionamento:
1. O usuário é questionado se reside em Giropops. Se a resposta for negativa, o programa encerra.
2. O usuário deve confirmar se é maior de idade (+18). Se a resposta for negativa, o programa encerra.
3. O usuário deve aceitar os termos de uso e privacidade para participar da pesquisa. Se a resposta for negativa, o programa encerra.
4. O programa coleta dados de gênero, número de filhos e salário dos participantes até que o usuário escolha parar.
5. Ao final, são calculadas e exibidas as seguintes estatísticas:
   - Percentual de participantes por gênero.
   - Média de filhos por família.
   - Média de salários e maior salário registrado.
*/

int main(){
  
  int numFilhos, somaFilhos = 0, mediaFilhos, contFilhos = 0;
  float salario, maiorSalario = 0, contSalario = 0;
  int somaSalario = 0;
  int idade, somaIdade = 0, mediaIdade, contIdade = 0;
  int menu = 0;
  int sexo, sexoMasculino, sexoContM = 0, sexoFeminino, sexoContF = 0, sexoOutros, sexoContO = 0; //Gênero do chefes de família.
  char op;

  printf("\n     ---------- COLETA DE DADOS -------------\n");
  printf("\n    -------- Município de Giropops -----------\n\n");
  printf("    Siga as instruções, respondendo as perguntas.\n");
  printf("  ------------------------------------------------\n\n");
  
  
  
  do //Primeiro Menu, server para selecionar candidatos que elegíveis para pesquisa. 
  {
    printf("\nVocê mora atualmente em Giropops?\n| 1 - Sim | 2 - Não |\n");
    scanf("%d", &menu);

    if (menu == 2)
    {
      printf("\nDesculpe você não é elegível para essa pesquisa\n");
      return 0 ;
      exit;
  
    }
    
    if (menu !=1 )
    {
      printf("\nResposta invalida... Tente novamente!\n\n");
    }

  } while (menu =! 1);

  do //Segundo Menu, server para selecionar candidatos que elegíveis para pesquisa.   
  {   
    printf("\nVocê é maior de idade (+18)?\n| 1 - Sim | 2 - Não |\n");
    scanf("%d", &menu);
 
     if (menu == 2)
    {
      printf("\nDesculpe você não é elegível para essa pesquisa\n");
      return 0;
      exit;
  
    }  

    if (menu !=1 )
    {
      printf("\nResposta invalida... Tente novamente!\n\n");
    }

  } while (menu != 1);

  do //Terceiro Menu, server para selecionar candidatos que elegíveis para pesquisa.   
  {   
    printf("\n\nVocê aceita os termos de uso de dados e privacidade\nsobre a pesquisa disponíveis em ornan.dev/contrato\n| 1 - Sim | 2 - Não |\n");
    scanf("%d", &menu);
 
     if (menu == 2)
    {
      printf("\nDesculpe você não é elegível para essa pesquisa\n");
      return 0;
      exit;
  
    }  

    if (menu !=1 )
    {
      printf("\nResposta invalida... Tente novamente!\n\n");
    }

  } while (menu != 1);


  while (1)
  {
   
    do //INPUT Sexo
    {
      printf("\n\nEscolha seu gênero:\n| 1 - Masculino | 2 - Feminino | 3 - Outros |\n ");
      scanf("%d", &sexo);
      
      switch (sexo)
      {
      case 1:
         ++sexoContM;
        break;

      case 2:
        ++sexoContF;
        break;

      case 3:
        ++sexoContO;
        break;

      default:

        if(sexo == 0 || sexo >= 4)
        {
          printf("\nDesculpe gênero não identificado.Tente novamente!\n");
        }        
      }


    } while (sexo == 0 || sexo >= 4);
    
      
    //INPUT Filhos 
    printf("\n\nQuantos filhos você possui?\n");
    scanf("%d", &numFilhos);
    somaFilhos += numFilhos;
    ++contFilhos;

    //INPUT Salario
    printf("\n\nQual o seu salário mensal?\n");
    scanf("%f", &salario);
    ++contSalario;
    if(salario > maiorSalario)
    {
      maiorSalario = salario;
    }
    somaSalario += salario;
    
    fflush(stdin);
    
    printf("\n\n----- Deseja registrar outra pessoa (s/n)? -----\n");
    
    scanf(" %c", &op);
    
    if (op != 's' && op != 'S')
    {
        break;
    }    
    
  }
  
  //CALCULO DE RESULTADOS

  //Sexo
  float sexoTotal = sexoContF + sexoContM + sexoContO;
  sexoMasculino = (sexoContM / sexoTotal) * 100;
  sexoFeminino =  (sexoContF / sexoTotal) * 100;
  sexoOutros  = (sexoContO / sexoTotal) * 100;

  //Filhos

  mediaFilhos = somaFilhos / contFilhos;

  //Salario
  float mediaSalario = somaSalario / contSalario;


  //RESULTADOS
  printf("\n\n------------ Resultados da Pesquisa ---------------\n\n");


  printf("\nParticipantes - Sexo\n");
  printf("Masculino: %d%%\n", sexoMasculino);
  printf("Feminino: %d%%\n", sexoFeminino);
  printf("Outros: %d%%\n", sexoOutros);

  printf("\nMedia de Filhos\n");
  printf("Numero de famílias: %d\n", contFilhos);
  printf("Media de filhos por família: %d\n", mediaFilhos);

  printf("\nSalários\n");
  printf("Media de salários: %.3f\n", mediaSalario);
  printf("Maior salário registrado: %.3f\n", maiorSalario);

  printf("\n\nA prefeitura de Giropops agradece a todos\nque participaram da pesquisa.\n");

  printf("\nFim!\n");
  
  return 0;

}