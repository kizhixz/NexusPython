"""
Descrição: Estruturas em tempo de execução e rastreamento de código
"""

# ==========================================
# 1. CONCEITO DE EXECUÇÃO DE PROGRAMA
# ==========================================

# Um programa em Python é executado linha por linha.
# A ordem das instruções é fundamental.

x = 10
x = x + 5

# Resultado final: x = 15


# ==========================================
# 2. PROGRAMA NÃO É ESTÁTICO
# ==========================================

# Diferente de um texto (que não muda),
# um programa é dinâmico: valores mudam durante a execução.

valor = 5
valor = valor * 2
valor = valor - 3

# valor evolui ao longo do tempo


# ==========================================
# 3. ORDEM DE EXECUÇÃO IMPORTA
# ==========================================

# A mesma operação em ordem diferente gera resultados diferentes

x = 10
x = x + 5
x = x * 2  # (10 + 5) * 2 = 30

# Comparação:

y = 10
y = y * 2
y = y + 5  # (10 * 2) + 5 = 25


# ==========================================
# 4. RELAÇÃO ENTRE VARIÁVEIS
# ==========================================

# Variáveis podem depender umas das outras

a = 10
b = a + 5
c = b * 2

# Existe uma cadeia de dependência
# a -> b -> c


# ==========================================
# 5. EVOLUÇÃO DE VALORES
# ==========================================

# Uma variável pode ter diferentes estados ao longo do tempo

contador = 0

contador += 1  # 1
contador += 2  # 3
contador *= 2  # 6

# Estado inicial -> alterações -> estado final


# ==========================================
# 6. RASTREAMENTO DE CÓDIGO (TRACE)
# ==========================================

# Técnica para entender o que o código faz
# Acompanhar linha por linha e anotar valores

x = 2
y = 3

# Passo 1: x = 2
# Passo 2: y = 3

z = x + y
# Passo 3: z = 5

z = z * 2
# Passo 4: z = 10


# ==========================================
# 7. TÉCNICA PASSO A PASSO
# ==========================================

# Como rastrear corretamente:

# 1. Leia o código linha por linha
# 2. Anote os valores das variáveis
# 3. Atualize a cada nova instrução
# 4. Observe dependências entre variáveis
# 5. Identifique o resultado final


# ==========================================
# 8. EXEMPLO COMPLETO DE RASTREAMENTO
# ==========================================

# Código:

a = 5
b = 2

a = a + b
b = a * 2

# Rastreamento:
# a = 5
# b = 2
# a = 7
# b = 14


# ==========================================
# 9. CRUZAMENTO DE VALORES
# ==========================================

# Variáveis podem trocar ou reutilizar valores

x = 1
y = 2

x, y = y, x

# Agora:
# x = 2
# y = 1


# ==========================================
# 10. MODULARIZAÇÃO E CONTROLE
# ==========================================

# Separar lógica ajuda a entender execução

# Exemplo simples:
valor_inicial = 10
incremento = 5

resultado = valor_inicial + incremento

# Facilita rastrear origem dos valores


# ==========================================
# 11. TEXTO VS PROGRAMA
# ==========================================

# Texto: linear, não muda
# Programa: dinâmico, valores mudam com execução

# Texto:
# "10 + 5"

# Programa:
resultado = 10 + 5  # executa e gera valor


# ==========================================
# 12. CONCEITO-CHAVE
# ==========================================

# Programação é sobre transformação de estado
# Variáveis mudam ao longo do tempo
# Entender isso é essencial para:
# - depuração
# - lógica
# - resolução de problemas


# ==========================================
# FIM DA DOCUMENTAÇÃO
# ==========================================