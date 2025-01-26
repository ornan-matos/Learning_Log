using System;

class format{
  static void Main(){
    //"\n" -> quebra a linha.
    Console.WriteLine("Primeira linha \nSegunda linha \nTerceira linha");
    //"\t" -> tabulação horizontal.
    Console.WriteLine("Maça...: \tR$0.75");
    Console.WriteLine("Uva...: \tR$1.00");
    Console.WriteLine("Banana...: \tR$2.40");
    //Apas simples e aspas duplas.
    Console.WriteLine("\"Por que ela tem esse \'jeitinho\'?\"");
    //Barra invertida.
    Console.WriteLine("C:\\Users\\Documentos\\arquivo.txt");
    //\0 Representa o caractere nulo (null), usado para indicar o fim de uma string em algumas linguagens ou contextos.
    Console.WriteLine("Hello\0World!");
    //Emite um som de alerta (beep) no sistema.
    Console.WriteLine("Alerta!\a");
    //Move o cursor uma posição para trás (backspace).
    Console.WriteLine("<- <- \b<-");
    //Representa o caractere de escape (ESC), usado em sequências de controle de terminal.
    Console.WriteLine("\e[31mTexto em vermelho\e[0m");
    //Representa um avanço de formulário (form feed), usado para limpar a tela ou avançar para a próxima página em impressoras.
    Console.WriteLine("Hello\fWorld!");
    //Move o cursor para o início da linha atual.
    Console.WriteLine("Hello\r\nWorld!");
    // "\v" -> tabulação vertical
    Console.WriteLine("Nome:\vJoão\vIdade:\v25 anos");
  }
}
