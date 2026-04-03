"""
Arquivo: variaveis_documentacao.py
Descrição: Documentação completa sobre variáveis em Python
"""

# ==========================================
# 1. DECLARAÇÃO DE VARIÁVEIS
# ==========================================

# Em Python, não é necessário declarar explicitamente o tipo da variável.
# A variável é criada no momento em que recebe um valor.

nome = "João"        # string
idade = 25           # inteiro
altura = 1.75        # float
ativo = True         # booleano


# ==========================================
# 2. ATRIBUIÇÃO DE VALORES
# ==========================================

# A atribuição é feita com o operador '='

x = 10
x = x + 5            # reatribuição

# Também é possível fazer atribuições múltiplas

a, b, c = 1, 2, 3

# Troca de valores

a, b = b, a


# ==========================================
# 3. ARMAZENAMENTO DE DADOS
# ==========================================

# Variáveis armazenam referências para objetos na memória

lista = [1, 2, 3]
lista.append(4)

# Importante: algumas estruturas são mutáveis (podem mudar)
# e outras são imutáveis

texto = "Python"
# texto[0] = "J"  # ERRO: strings são imutáveis


# ==========================================
# 4. TIPAGEM DINÂMICA
# ==========================================

# Python utiliza tipagem dinâmica
# Ou seja, o tipo da variável pode mudar em tempo de execução

valor = 10
valor = "dez"
valor = 10.5

# Porém, isso exige cuidado para evitar erros

# Exemplo de erro comum:
# print(valor + 5)  # ERRO se valor for string


# ==========================================
# 5. NOMENCLATURA DE VARIÁVEIS
# ==========================================

# Regras básicas:
# - Deve começar com letra ou underscore (_)
# - Não pode começar com número
# - Não pode conter espaços
# - Não pode usar palavras reservadas (if, for, while, etc.)

# Exemplos válidos
nome_usuario = "Ana"
_id = 123
valorTotal = 100

# Exemplos inválidos
# 1nome = "Erro"
# nome-usuario = "Erro"
# class = "Erro"


# ==========================================
# 6. BOAS PRÁTICAS DE NOMENCLATURA
# ==========================================

# Use nomes descritivos
idade_usuario = 30
saldo_conta = 1500.50

# Utilize snake_case (padrão em Python)
numero_de_itens = 5

# Evite nomes genéricos
# x = 10  # ruim
contador_de_usuarios = 10  # melhor


# ==========================================
# 7. PADRÕES QUE TAMBÉM SE APLICAM A FUNÇÕES
# ==========================================

# A mesma lógica de nomenclatura deve ser aplicada a funções

# Exemplo de função bem nomeada

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Evite nomes ruins
# def f(a, b):
#     return a + b

# IMPORTANTE:
# A clareza do nome impacta diretamente na manutenção do código


# ==========================================
# 8. CONSIDERAÇÕES FINAIS
# ==========================================

# - Variáveis são fundamentais para armazenar dados
# - A tipagem dinâmica oferece flexibilidade, mas exige atenção
# - Bons nomes tornam o código mais legível e profissional
# - As regras de nomenclatura se aplicam a variáveis, funções,
#   classes e qualquer identificador no código

# Seguir boas práticas facilita manutenção, colaboração e entendimento


# ==========================================
# 9. TIPOS DE DADOS EM PYTHON (APROFUNDADO)
# ==========================================

# Python possui diversos tipos de dados embutidos.
# Os principais são: int, float, str e bool.


# ------------------------------------------
# 9.1 INTEIROS (int)
# ------------------------------------------

# Representam números inteiros (positivos ou negativos)

numero = 10
negativo = -5

# Inteiros não possuem limite fixo em Python
numero_grande = 999999999999999999999999

# Operações comuns
soma = 5 + 3
subtracao = 10 - 2
multiplicacao = 4 * 2
divisao_inteira = 10 // 3  # resultado inteiro


# ------------------------------------------
# 9.2 PONTO FLUTUANTE (float)
# ------------------------------------------

# Representam números decimais

altura = 1.75
peso = 70.5

# Também podem ser representados em notação científica
valor = 1.5e3  # 1500.0

# Atenção com precisão
resultado = 0.1 + 0.2
# Pode resultar em algo como 0.30000000000000004


# ------------------------------------------
# 9.3 STRINGS (str)
# ------------------------------------------

# Representam textos

nome = "Carlos"
frase = 'Olá, mundo!'

# Strings podem conter:
# - letras
# - números
# - acentos
# - caracteres especiais
texto = "Python 3 é incrível! @#%"

# Strings são imutáveis
# nome[0] = "J"  # ERRO

# Operações comuns
concatenacao = "Olá" + " " + "Mundo"
repeticao = "Ha" * 3  # "HaHaHa"

# Métodos úteis
maiusculo = nome.upper()
minusculo = nome.lower()
tamanho = len(nome)


# ------------------------------------------
# 9.4 BOOLEANOS (bool)
# ------------------------------------------

# Representam valores lógicos: True ou False

ativo = True
inativo = False

# Geralmente usados em condições
idade = 18
maior_de_idade = idade >= 18  # True

# Operadores lógicos
resultado_and = True and False
resultado_or = True or False
resultado_not = not True


# ------------------------------------------
# 9.5 REGRAS IMPORTANTES SOBRE TIPOS
# ------------------------------------------

# 1. Tipagem dinâmica
# O tipo da variável é definido automaticamente

variavel = 10
variavel = "Agora sou texto"

# 2. Verificação de tipo

tipo = type(variavel)

# 3. Conversão de tipos (casting)

numero_str = "10"
numero_int = int(numero_str)
numero_float = float(numero_str)
texto = str(100)

# 4. Operações entre tipos diferentes podem causar erro

# print("10" + 5)  # ERRO

# Correto:
resultado = int("10") + 5


# ------------------------------------------
# 9.6 VERDADE EM PYTHON (TRUTHY / FALSY)
# ------------------------------------------

# Alguns valores são considerados False automaticamente:

# False
# 0
# 0.0
# "" (string vazia)
# None
# listas/coleções vazias

if "":
    print("Isso não será executado")

if 1:
    print("Isso será executado")


# ------------------------------------------
# 9.7 BOAS PRÁTICAS COM TIPOS DE DADOS
# ------------------------------------------

# - Use o tipo correto para cada situação
# - Evite misturar tipos sem necessidade
# - Sempre valide dados quando necessário
# - Tenha cuidado com floats (precisão)
# - Prefira clareza ao invés de atalhos


# ==========================================
# 10. OPERADORES EM PYTHON
# ==========================================

# Operadores são usados para realizar operações com valores e variáveis.


# ------------------------------------------
# 10.1 OPERADORES MATEMÁTICOS
# ------------------------------------------

# +  (adição)
# -  (subtração)
# *  (multiplicação)
# /  (divisão)
# // (divisão inteira)
# %  (resto da divisão)
# ** (potenciação)

soma = 10 + 5
sub = 10 - 5
mult = 10 * 5
div = 10 / 2
div_int = 10 // 3
resto = 10 % 3
potencia = 2 ** 3  # 8


# ------------------------------------------
# 10.2 OPERADORES DE ATRIBUIÇÃO
# ------------------------------------------

# =   atribuição simples
# +=  soma e atribui
# -=  subtrai e atribui
# *=  multiplica e atribui
# /=  divide e atribui
# //= divisão inteira e atribui
# %=  resto e atribui
# **= potência e atribui

x = 10
x += 5   # x = x + 5
x -= 2
x *= 3
x /= 2


# ------------------------------------------
# 10.3 OPERADORES LÓGICOS
# ------------------------------------------

# and  -> verdadeiro se ambos forem verdadeiros
# or   -> verdadeiro se pelo menos um for verdadeiro
# not  -> inverte o valor lógico

verdadeiro = True
falso = False

resultado_and = verdadeiro and falso
resultado_or = verdadeiro or falso
resultado_not = not verdadeiro


# ------------------------------------------
# 10.4 OPERADORES DE COMPARAÇÃO (EXTRA IMPORTANTE)
# ------------------------------------------

# ==  igual
# !=  diferente
# >   maior que
# <   menor que
# >=  maior ou igual
# <=  menor ou igual

comparacao1 = 10 == 10
comparacao2 = 10 != 5
comparacao3 = 10 > 5
comparacao4 = 5 < 10


# ------------------------------------------
# 10.5 CONSIDERAÇÕES SOBRE OPERADORES
# ------------------------------------------

# - Operadores seguem ordem de precedência
# - Parênteses podem ser usados para controlar a ordem
# - Misturar operadores exige atenção

resultado = (10 + 5) * 2  # 30

# Evite expressões confusas
# ruim:
# resultado = 10 + 5 * 2

# melhor:
resultado = 10 + (5 * 2)


# ==========================================
# FIM DA DOCUMENTAÇÃO
# ==========================================
