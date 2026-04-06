"""
Descrição: Documentação sobre estruturas condicionais em Python
"""

# ==========================================
# 1. CONCEITO DE CONDICIONAIS
# ==========================================

# Estruturas condicionais permitem que o programa
# tome decisões com base em condições.

# Ou seja, o fluxo do programa pode mudar.


# ==========================================
# 2. ESTRUTURA IF
# ==========================================

# Executa um bloco de código se a condição for verdadeira

idade = 18

if idade >= 18:
    print("Maior de idade")


# ==========================================
# 3. IF / ELSE
# ==========================================

# Permite executar um caminho alternativo

idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# ==========================================
# 4. IF / ELIF / ELSE
# ==========================================

# Permite múltiplas condições

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Reprovado")


# ==========================================
# 5. CONDIÇÕES ALINHADAS (ANINHADAS)
# ==========================================

# Nem sempre o programa é simples.
# Podemos ter um if dentro de outro if.

idade = 20
possui_carteira = True

if idade >= 18:
    if possui_carteira:
        print("Pode dirigir")
    else:
        print("Precisa tirar carteira")
else:
    print("Não pode dirigir")


# ==========================================
# 6. IMPORTÂNCIA DO ALINHAMENTO
# ==========================================

# Em Python, a indentação define os blocos de código
# Isso é fundamental para o funcionamento correto

# Exemplo incorreto:
# if True:
# print("Erro")  # erro de indentação


# ==========================================
# 7. CONDIÇÕES COM OPERADORES LÓGICOS
# ==========================================

idade = 25
renda = 3000

if idade >= 18 and renda > 2000:
    print("Aprovado")


# ==========================================
# 8. EXEMPLO PRÁTICO (CONTA DE CELULAR)
# ==========================================

consumo = 120

if consumo <= 100:
    valor = 50
else:
    excesso = consumo - 100
    valor = 50 + (excesso * 2)

print("Valor da conta:", valor)


# ==========================================
# 9. EXEMPLO PRÁTICO (EMPRESA)
# ==========================================

salario = 3000
anos_empresa = 3

if anos_empresa >= 5:
    bonus = salario * 0.2
elif anos_empresa >= 2:
    bonus = salario * 0.1
else:
    bonus = salario * 0.05

print("Bônus:", bonus)


# ==========================================
# 10. BOAS PRÁTICAS
# ==========================================

# - Evite muitas condições aninhadas (código complexo)
# - Prefira clareza
# - Use nomes de variáveis claros
# - Teste diferentes cenários


# ==========================================
# 11. CONCEITO-CHAVE
# ==========================================

# Condicionais controlam o fluxo do programa
# Permitem diferentes caminhos de execução
# São fundamentais para lógica e tomada de decisão


# ==========================================
# FIM DA DOCUMENTAÇÃO
# ==========================================
