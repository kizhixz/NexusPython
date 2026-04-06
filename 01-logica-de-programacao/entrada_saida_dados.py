"""
Descrição: Documentação sobre entrada e saída de dados em Python
"""

# ==========================================
# 1. CONCEITO DE ENTRADA E SAÍDA
# ==========================================

# Entrada de dados: quando o programa recebe informações (input)
# Saída de dados: quando o programa exibe informações (print)


# ==========================================
# 2. FUNÇÃO INPUT()
# ==========================================

# A função input() permite que o usuário digite algo

nome = input("Digite seu nome: ")

# IMPORTANTE:
# O valor retornado pelo input() SEMPRE será do tipo string (str)


# ==========================================
# 3. CONVERSÃO DE TIPOS (CASTING)
# ==========================================

# Como o input sempre retorna string,
# muitas vezes precisamos converter o valor

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

# Outras conversões possíveis
numero_str = str(10)


# ==========================================
# 4. FUNÇÃO PRINT()
# ==========================================

# A função print() exibe informações na tela

print("Olá, mundo!")

# Pode exibir variáveis
nome = "Ana"
print(nome)


# ==========================================
# 5. COMBINANDO TEXTO E VARIÁVEIS
# ==========================================

nome = "Carlos"
idade = 25

# Concatenação (menos recomendado)
print("Nome: " + nome + ", Idade: " + str(idade))

# f-string (recomendado)
print(f"Nome: {nome}, Idade: {idade}")

# Método format
print("Nome: {}, Idade: {}".format(nome, idade))


# ==========================================
# 6. MÚLTIPLOS VALORES NO PRINT
# ==========================================

# O print aceita múltiplos argumentos

print("Nome:", nome, "Idade:", idade)

# Separador padrão é espaço
# Pode ser alterado com sep
print("A", "B", "C", sep="-")  # A-B-C

# Pode controlar o final com end
print("Olá", end=" ")
print("Mundo")


# ==========================================
# 7. CUIDADOS IMPORTANTES
# ==========================================

# 1. Sempre validar entrada do usuário
# input não impede erros de digitação

# 2. Conversões podem gerar erro
# int("abc")  # ValueError

# 3. Sempre lembrar que input retorna string


# ==========================================
# 8. EXEMPLO COMPLETO
# ==========================================

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá {nome}, você tem {idade} anos.")


# ==========================================
# FIM DA DOCUMENTAÇÃO
# ==========================================
