# Tipos Primitivos e Saída de Dados

## Tipos Primitivos

Os Tipos primitivos no Python são nomenclaturas usadas para representar tipos de dados. De forma mais simples os tipos primitivos no Python são a representação de um tipo de dado, esses tipos primitivos mostram ao Python qual é o tipo de dado que ele está lidando, dentro da nossa linguagem Python os tipo primitivos mais básicos são int, float, bool e str, cada um desses tipos podem ser utilizados dentro do Python. Na pratica fica mais fácil de entender:

`int`: O tipo primitivo int representa os números inteiros (ex: 8, -2, 0, 476396), qualquer valor inteiro é visto pelo Python como int, dentro da linguagem a aparição mais comum dos tipos primitivos incluindo o int, é na entrada de dados no comando input.

&ensp;&ensp;&ensp; `num = int(input("Digite um número: "))`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Retorno: Digite um número:

Como podemos ver no exemplo o tipo primitivo aparece primeiro em conjunto com o uso dos parenteses (`int()`) para sinalizar ao Python que o dado fornecido pelo usuário sera um inteiro.

`float`: O tipo primitivo float comumente conhecido como ponto flutuante, representa números com ponto (.) depois do número de origem, dentro do Python a vírgula que é comumente usada no Brasil para representar números quebrados (números não inteiros que possuem vírgula) não é reconhecida pela linguagem Python, por tanto utilizamos o ponto para representar números não inteiros (ex: 4.5, 0.078, -38.283, 9.0).

&ensp;&ensp;&ensp; `num = float(input("Digite um número quebrado: "))`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Retorno: Digite um número quebrado:

`bool`: O tipo primitivo bool comumente conhecido como booleano, aceita apenas dois valores True e False, dentro do Python o True e False vem com letras maiúsculas mesmo, o valor é facilmente reconhecido pela linguagem e também é utilizado muitas vezes de maneira direta.

&ensp;&ensp;&ensp; `ativo = True`<br>

Esse exemplo aborda uma variável (`ativo`) é verdadeira, nesse caso poderiamos utilizar essa variável em uma estrutura de verdadeiro e falso (`if` e `else`), caso a variável estiver ativa `if ativo:` execute `print(bem-vindo(a))`.

`str` = O tipo primitivo str representa as strings, como vimos anteriormente no resumo [primeiros-passos.md](primeiros-passos.md) as strings são um conjunto de caracteres, números, simbolos ou sequências alfanúmericas que estão entre aspas ("" ou ''), as strings são usadas em diversas estruturas porem o tipo primitivo mais especificamente o comando str é utilizado comumente na estrutura input.

&ensp;&ensp;&ensp; `num = str(input("Digite seu nome: "))`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Retorno: Digite seu nome:

Nesse exemplo o `input` é delimitado a interpretar dentro dessa entrada de dados apenas strings, então se o usuário colocar qualquer tipo de dado ai, o Python irá reconhecer esse dado como uma string.

## Saída de dados

Dentro do Python o print é um dos comandos mais utilizados, porém apesar de parecer bem simples o print tem variações. As variações do print são bem simples e faceis de entender, na pratica cada um escolhe a maneira mais confortavel de formatar seu print.

`Modo moderno`: O modo mais usado e considerado o moderno é o que usa o f antes das aspas e chaves (`{}`).

&ensp;&ensp;&ensp; `nome = pedrozo`<br>
&ensp;&ensp;&ensp; `print(f"Olá {nome} tudo bem")`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Retorno: Olá pedrozo tudo bem

`Modo simples`: O modo simples é o modo apresentado no resumo anterior a esse ([primeiros-passos.md](primeiros-passos.md)), ele utiliza a vírgula para separar a variável do texto.

&ensp;&ensp;&ensp; `nome = pedrozo`<br>
&ensp;&ensp;&ensp; `print(f"Olá", nome, "tudo bem")`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Retorno: Olá pedrozo tudo bem

`Modo Antigo`: O modo antigo é um modo que usa o `.format` para sinalizar as variáveis e o `{}` para sinalizar a posição das vaiáveis.

&ensp;&ensp;&ensp; `nome = pedrozo`<br>
&ensp;&ensp;&ensp; `print(f"Olá {} tudo bem".format(nome))`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Retorno: Olá pedrozo tudo bem

`Modo Legado`: O modo legado é um modo que não deve ser utilizado em projetos novos, pois é um modo obsoleto utilizado muito antigamente, apesar dele funcionar hoje, o motivo dele ainda estar em funcionamento é para não comprometer sistemas antigos que ainda utilizam esse formato. O modo que ele utiliza é marcando o local da variável com `%s` e sinalizando e separando a string e a variável com `%`.

&ensp;&ensp;&ensp; `nome = pedrozo`<br>
&ensp;&ensp;&ensp; `print(f"Olá %s tudo bem" % nome)`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Retorno: Olá pedrozo tudo bem

## Exercícios Relacionados 

- [Exercício 003](../exercicios/aula%206%20exercicio%2003.py)
- [Exercício 004](../exercicios/aula%206%20exercicio%2004.py)