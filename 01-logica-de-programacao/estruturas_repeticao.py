"""
Descrição: Documentação sobre estruturas de repetição em Python
"""

# ==========================================
# 1. CONCEITO DE REPETIÇÃO
# ==========================================

# Estruturas de repetição permitem executar um bloco de código
# várias vezes, de forma controlada.

# São fundamentais para automatizar tarefas repetitivas.


# ==========================================
# 2. LOOP FOR (ESTRUTURA E REGRAS)
# ==========================================

# Estrutura básica do for:
# for variavel in sequencia:
#     bloco_de_codigo

# Explicação dos elementos:
# - variavel: recebe cada valor da sequência a cada repetição
# - in: operador que conecta a variável à sequência
# - sequencia: conjunto de valores (range, lista, string, etc.)
# - bloco_de_codigo: código que será repetido

# Exemplo:
for i in range(5):
    print(i)

# Fluxo de execução:
# i = 0 -> executa
# i = 1 -> executa
# i = 2 -> executa
# i = 3 -> executa
# i = 4 -> executa
# termina


# ------------------------------------------
# 2.1 O QUE É O "in"
# ------------------------------------------

# O "in" significa: "para cada elemento dentro de"

# Ele percorre (itera) uma sequência

for letra in "Python":
    print(letra)

# Interpretação:
# para cada letra dentro de "Python"

# Funciona com várias estruturas:

# Lista
for item in [1, 2, 3]:
    print(item)

# Range
for numero in range(3):
    print(numero)

# String
for caractere in "ABC":
    print(caractere)

# IMPORTANTE:
# O "in" NÃO é só de loop — ele também pode verificar existência

existe = 3 in [1, 2, 3]  # True


# ------------------------------------------
# 2.2 REGRAS DO FOR
# ------------------------------------------

# 1. Precisa de uma sequência (iterável)
# 2. A variável recebe um valor por vez
# 3. O loop termina quando a sequência acaba
# 4. A indentação define o bloco executado

# Exemplo detalhado:

for x in range(3):
    resultado = x * 2
    print(resultado)

# Execução:
# x=0 -> resultado=0
# x=1 -> resultado=2
# x=2 -> resultado=4


# ------------------------------------------
# 2.3 RANGE (MUITO USADO COM FOR)
# ------------------------------------------

# range(inicio, fim, passo)

for i in range(0, 5, 1):
    print(i)

# inicio: começa (inclusivo)
# fim: termina (exclusivo)
# passo: incremento

# Formas comuns:
range(5)        # 0 até 4
range(1, 5)     # 1 até 4
range(0, 10, 2) # de 2 em 2


# ==========================================
# 3. CONTADORES

# O for percorre uma sequência (lista, string, range, etc.)

for i in range(5):
    print(i)

# range(5) -> 0 até 4


# ==========================================
# 3. CONTADORES
# ==========================================

# Contador: variável que conta quantas vezes algo aconteceu

contador = 0

for i in range(5):
    contador += 1

print("Total:", contador)


# ==========================================
# 4. ACUMULADORES
# ==========================================

# Acumulador: variável que soma ou agrega valores

soma = 0

for i in range(5):
    soma += i

print("Soma:", soma)


# ==========================================
# 5. INTERRUPÇÃO DE LOOP (BREAK)
# ==========================================

# O break interrompe completamente o loop

for i in range(10):
    if i == 5:
        break
    print(i)


# ==========================================
# 6. CONTINUAÇÃO (CONTINUE)
# ==========================================

# O continue pula para a próxima iteração

for i in range(5):
    if i == 2:
        continue
    print(i)


# ==========================================
# 7. ELSE EM LOOPS
# ==========================================

# O else em loops executa quando o loop termina normalmente
# (sem ser interrompido por break)

for i in range(3):
    print(i)
else:
    print("Loop finalizado sem interrupção")


# ==========================================
# 8. REPETIÇÕES ALINHADAS (ANINHADAS)
# ==========================================

# Um loop dentro de outro loop

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# ==========================================
# 9. CONTROLE DA REPETIÇÃO
# ==========================================

# Estruturas que controlam o fluxo do loop:
# - break (interrompe)
# - continue (pula)
# - condição do loop


# ==========================================
# 10. BOAS PRÁTICAS
# ==========================================

# - Evite loops infinitos
# - Use nomes claros para variáveis
# - Prefira simplicidade
# - Controle bem quando parar o loop


# ==========================================
# 11. CONCEITO-CHAVE
# ==========================================

# Repetição é execução controlada de código
# Contadores e acumuladores são padrões comuns
# Controle de fluxo (break/continue) é essencial


# ==========================================
# FIM DA DOCUMENTAÇÃO
# ==========================================
