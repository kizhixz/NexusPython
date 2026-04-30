"""
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