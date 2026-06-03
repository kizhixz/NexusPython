"""
Descrição: Documentação e exemplos sobre operadores em Python.
"""

# ==========================================
# 1. TIPOS DE OPERADORES EM PYTHON
# ==========================================

# 1.1 - Operadores aritméticos
# São usados para cálculos matemáticos básicos.
valor = 10 + 5      # adição
valor = 10 - 5      # subtração
valor = 10 * 5      # multiplicação
valor = 10 / 5      # divisão verdadeira (float)
valor = 10 // 3     # divisão inteira
valor = 10 % 3      # resto da divisão
valor = 2 ** 3      # potência

# 1.2 - Operadores de comparação
# Comparam valores e retornam True ou False.
a = 10
b = 5
#resultado = a == b   # igual
#resultado = a != b   # diferente
resultado = a > b    # maior
resultado = a < b    # menor
resultado = a >= b   # maior ou igual
resultado = a <= b   # menor ou igual

# 1.3 - Operadores lógicos
# Usados para combinar expressões booleanas.
condicao1 = True
condicao2 = False
resultado_and = condicao1 and condicao2  # True se ambas forem True
resultado_or = condicao1 or condicao2    # True se ao menos uma for True
resultado_not = not condicao1            # inverte o valor booleano

# 1.4 - Operadores de atribuição
# Atribuem valores a variáveis, podendo atualizar o valor atual.
x = 10
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
x //= 2  # x = x // 2
x %= 3   # x = x % 3
x **= 2  # x = x ** 2

# 1.5 - Operadores bit a bit
# Trabalham com bits dos números inteiros.
a = 6   # binário: 0b110
b = 3   # binário: 0b011
bit_and = a & b   # 0b010 => 2
bit_or = a | b    # 0b111 => 7
bit_xor = a ^ b   # 0b101 => 5
bit_not = ~a      # complemento bit a bit
bit_left = a << 1 # desloca bits para a esquerda
bit_right = a >> 1# desloca bits para a direita

# 1.6 - Operadores de associação (membership)
# Verificam se um valor está em uma sequência.
frutas = ["maçã", "banana", "laranja"]
existe_banana = "banana" in frutas        # True
nao_existe_uva = "uva" not in frutas     # True

# 1.7 - Operadores de identidade
# Verificam se duas variáveis apontam para o mesmo objeto.
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]
mesmo_objeto = lista1 is lista2    # True
objetos_diferentes = lista1 is lista3 # False

# ==========================================
# 2. EXEMPLOS PRÁTICOS DE OPERADORES LÓGICOS
# ==========================================

idade = 20
renda = 2500
possui_cnh = True

if idade >= 18 and possui_cnh:
    print("Pode dirigir")

if renda > 2000 or idade >= 65:
    print("Tem acesso a crédito especial")

if not possui_cnh:
    print("Não possui carteira de motorista")

# Exemplo misturando comparação e operadores lógicos
nota = 8.5
frequencia = 92

if nota >= 7 and frequencia >= 75:
    print("Aprovado")
else:
    print("Reprovado")

# ==========================================
# 3. PRIORIDADE ENTRE OPERADORES
# ==========================================

# A ordem de avaliação em Python segue a precedência:
# 1. Parênteses
# 2. Exponenciação
# 3. Multiplicação, divisão, resto, divisão inteira
# 4. Adição e subtração
# 5. Operadores bit a bit
# 6. Comparação
# 7. Operadores lógicos (not, and, or)

expressao = 3 + 4 * 2 == 11 and not False
print("Resultado da expressão:", expressao)

# ==========================================
# 4. DICAS IMPORTANTES
# ==========================================

# - Use operadores lógicos para criar condições compostas.
# - Teste cada condição separadamente antes de combinar.
# - Evite expressões excessivamente complexas; prefira clareza.
# - Em Python, 'and' e 'or' retornam o último valor avaliado,
#   não apenas True ou False.

valor1 = 0
valor2 = 5
print("and retorna:", valor1 and valor2)
print("or retorna:", valor1 or valor2)
