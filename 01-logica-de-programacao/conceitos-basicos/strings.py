"""
Descrição: Documentação aprofundada sobre strings em Python
"""

# ==========================================
# 1. CONCEITO DE STRING
# ==========================================

# String (str) é uma sequência de caracteres.
# Pode conter letras, números, espaços, acentos e caracteres especiais.

texto = "Python é poderoso!"

# Strings podem ser definidas com aspas simples, duplas ou triplas
s1 = 'Olá'
s2 = "Mundo"
s3 = """Texto em múltiplas linhas
com várias quebras"""


# ==========================================
# 2. CARACTERÍSTICAS PRINCIPAIS
# ==========================================

# - Sequência ordenada de caracteres
# - Indexada (cada caractere possui posição)
# - Imutável (não pode ser alterada diretamente)

palavra = "Python"

# palavra[0] = 'J'  # ERRO: strings são imutáveis


# ==========================================
# 3. INDEXAÇÃO
# ==========================================

# Cada caractere possui um índice (posição)

texto = "Python"

primeira_letra = texto[0]   # 'P'
ultima_letra = texto[-1]    # 'n'

# Índices negativos contam do final


# ==========================================
# 4. FATIAMENTO (SLICING) - APROFUNDADO
# ==========================================

# Sintaxe: string[inicio:fim:passo]
# - inicio: índice inicial (inclusivo)
# - fim: índice final (exclusivo)
# - passo: intervalo de salto

texto = "Python"

# Visualização dos índices:
#  P   y   t   h   o   n
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

parte1 = texto[0:3]   # 'Pyt'
parte2 = texto[2:]    # 'thon'
parte3 = texto[:4]    # 'Pyth'

# Usando passo
parte4 = texto[::2]   # 'Pto'
parte5 = texto[1::2]  # 'yhn'

# Índices negativos
parte6 = texto[-4:-1]  # 'tho'

# Inverter string
invertida = texto[::-1]  # 'nohtyP'

# IMPORTANTE:
# O índice final NÃO é incluído no resultado


# ==========================================
# 4.1 PARTES DA STRING
# ==========================================

# Podemos extrair partes específicas de uma string

frase = "Aprendendo Python"

primeira_palavra = frase[:10]   # 'Aprendendo'
segunda_palavra = frase[11:]    # 'Python'


# ==========================================
# 4.2 ACESSO POR ÍNDICE
# ==========================================

# Acessar um único caractere

texto = "Python"

letra_p = texto[0]
letra_n = texto[-1]

# Tentativa de acessar índice inválido gera erro
# texto[10]  # IndexError


# ==========================================
# 5. CONCATENAÇÃO (OPERADOR +)
# ==========================================

# Sintaxe: string[inicio:fim:passo]

texto = "Python"

parte1 = texto[0:3]   # 'Pyt'
parte2 = texto[2:]    # 'thon'
parte3 = texto[:4]    # 'Pyth'
parte4 = texto[::2]   # 'Pto'

# Fatiamento com índices negativos
parte5 = texto[-4:-1]  # 'tho'

# Reverter string
invertida = texto[::-1]  # 'nohtyP'


# ==========================================
# 5. CONCATENAÇÃO
# ==========================================

# Juntar strings

nome = "Ana"
sobrenome = "Silva"

nome_completo = nome + " " + sobrenome

# Repetição
risada = "Ha" * 3  # 'HaHaHa'


# ==========================================
# 5.1 TAMANHO DA STRING (len)
# ==========================================

# A função len() retorna a quantidade de caracteres

texto = "Python"
tamanho = len(texto)  # 6

# Inclui espaços e caracteres especiais
frase = "Olá mundo"
tamanho_frase = len(frase)  # conta o espaço também

# Muito útil para validações
if len(texto) > 5:
    print("String longa")


# ==========================================
# 6. MÉTODOS IMPORTANTES
# ==========================================

texto = " Python "

# Remover espaços
sem_espaco = texto.strip()

# Caixa alta/baixa
maiusculo = texto.upper()
minusculo = texto.lower()

# Substituição
novo_texto = texto.replace("Python", "Java")

# Divisão
partes = "a,b,c".split(",")

# Junção
juncao = ",".join(partes)


# ==========================================
# 7. ITERAÇÃO EM STRINGS
# ==========================================

# Percorrer cada caractere

for letra in "Python":
    print(letra)


# ==========================================
# 8. COMPARAÇÃO DE STRINGS
# ==========================================

# Comparação é feita pelo valor (ordem Unicode)