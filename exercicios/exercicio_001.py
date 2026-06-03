# Exercício 001\n# Escreva sua solução aqui\n\n
"""
Foco: Slicing (Fatiamento), Índices, e Tamanho (len)

O Problema:
Você recebeu uma string que contém uma mensagem secreta,
mas ela está misturada com caracteres inúteis e de trás para frente.
String de teste: codigo = "x!o!d!n!i!l! !o!t!i!u!m! !e! !n!o!h!t!y!p"

Sua missão:

Usando apenas fatiamento (slicing), extraia a mensagem real.
Perceba que a mensagem está nos índices pares ou ímpares? 
E ela está invertida. Você precisará usar o parâmetro de passo do slicing e a inversão.

Descubra o tamanho da string original e o tamanho da string decodificada
 usando a função adequada e armazene em variáveis.

Imprima o resultado final usando f-strings no seguinte formato:
Resultado esperado: "A mensagem é '[MENSAGEM DECODIFICADA]' 
(reduzida de X para Y caracteres)."

"""

codigo = "x!o!d!n!i!l! !o!t!i!u!m! !e! !n!o!h!t!y!p"

n1 = len(codigo) # 41
n2 = codigo[::2][::-1] # "python é muito lindo"

print(f"A mensagem é '{n2}' (reduzida de {n1} para {len(n2)} caracteres).")