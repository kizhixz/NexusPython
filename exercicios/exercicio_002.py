"""

Exercício 2: Tratamento de Dados e Troca de Variáveis
Foco: Métodos de String (split, strip, upper), Atribuição Múltipla e Swap

O Problema:
Um sistema antigo exportou o nome e o sobrenome de um usuário em uma única string, 
tudo bagunçado, com espaços extras, letras maiúsculas e minúsculas misturadas, 
e na ordem errada (Sobrenome, Nome).

String de teste: registro = "   sIlVa, jOaO   "

Sua missão:

Limpe os espaços em branco das bordas da string.

Divida essa string em duas partes usando a vírgula como separador. 
Armazene o resultado em variáveis (você pode fazer isso direto na atribuição múltipla).

O primeiro valor será o sobrenome e o segundo será o nome. Limpe os espaços em 
branco que possam ter sobrado em cada variável isoladamente e deixe ambas totalmente em 
letras maiúsculas.

Use a técnica de troca de valores (a, b = b, a) do Python para inverter as variáveis, 
de modo que a variável do nome passe a guardar o sobrenome, 
e a do sobrenome passe a guardar o nome.

Junte as duas usando o método de string que une elementos (join) com um espaço entre elas, 
e imprima.

Resultado esperado: "JOAO SILVA"

"""

registro = "   sIlVa, jOaO   "

# Passo 1: Limpar os espaços em branco das bordas da string
nome_completo = registro.strip()  # Usando strip para remover os espaços extras
nome_completo = nome_completo.split(",")  # Passo 2: Dividir a string usando a vírgula como separador
nome_completo = [parte.strip().upper() for parte in nome_completo]  # Passo 3: Limpar espaços e converter para maiúsculas
nome_completo[0], nome_completo[1] = nome_completo[1], nome_completo[0]  # Passo 4: Trocar as variáveis
nome_completo = " ".join(nome_completo)  # Passo 5: Juntar as partes com um espaço entre elas

print(nome_completo)  # Imprimir o resultado final