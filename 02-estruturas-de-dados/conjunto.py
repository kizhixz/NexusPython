"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║              ESTRUTURA DE DADOS: CONJUNTO (SET)                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝

CARACTERÍSTICAS PRINCIPAIS:
  ✓ Elementos Únicos: NÃO permite duplicatas
  ✓ Não-Ordenado: Não tem ordem definida (pode variar entre execuções)
  ✓ Mutável: Pode ser modificado após criação
  ✓ Não-Indexável: Não acessa por índice
  ✓ Heterogêneo: Pode conter tipos diferentes (mas imutáveis)

REMOVEÇÃO AUTOMÁTICA DE DUPLICATAS:
  - {1, 2, 2, 3, 3, 3} automaticamente vira {1, 2, 3}
  - Essencial quando precisa de valores únicos

OPERAÇÕES MATEMÁTICAS:
  - União (|): Todos elementos de ambos os conjuntos
  - Interseção (&): Elementos em comum
  - Diferença (-): Elementos do primeiro não no segundo
  - Diferença Simétrica (^): Elementos que estão em UM ou OUTRO, mas não em ambos

PERFORMANCE:
  - Verificar pertencimento: O(1) - Muito rápido (vs O(n) em listas)
  - Adicionar: O(1) - Rápido
  - Remover: O(1) - Rápido
  - Operações de conjunto: O(n) - Depende do tamanho

QUANDO USAR:
  - Remover duplicatas de uma lista
  - Operações matemáticas (união, interseção)
  - Verificar se um valor pertence (mais rápido)
  - Encontrar elementos únicos
"""

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 1: CRIANDO CONJUNTOS
# ─────────────────────────────────────────────────────────────────────────────

# IMPORTANTE: {} cria dicionário vazio, use set() para conjunto vazio!

# Conjunto vazio (DEVE usar set(), não {})
conjunto_vazio = set()

# Conjunto com números
conjunto_numeros = {1, 2, 3, 4, 5}

# Conjunto com letras
conjunto_letras = {'a', 'b', 'c', 'd'}

# Conjunto misto com tipos diferentes (mas todos imutáveis)
conjunto_misto = {1, 'dois', 3.0, True}

print("=== CRIANDO CONJUNTOS ===")
print(f"Conjunto vazio: {conjunto_vazio}")
print(f"  → Tipo: {type(conjunto_vazio)}")
print(f"  → IMPORTANTE: set() não {{}}")

print(f"\nNúmeros: {conjunto_numeros}")
print(f"  → Tipo: {type(conjunto_numeros)}")

print(f"\nLetras: {conjunto_letras}")
print(f"  → Tipo: {type(conjunto_letras)}")

print(f"\nMisto: {conjunto_misto}")
print(f"  → Contém tipos diferentes (mas todos imutáveis)")

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 2: REMOVER DUPLICATAS - CASO DE USO COMUM
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== CONVERTENDO DE LISTA - REMOVER DUPLICATAS ===")

lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Lista com duplicatas: {lista}")
print(f"  → Tem elementos repetidos")

conjunto = set(lista)
print(f"\nConjunto (set()): {conjunto}")
print(f"  → Duplicatas foram AUTOMATICAMENTE removidas!")
print(f"  → Ordem também pode mudar (conjuntos não são ordenados)")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 3: ADICIONANDO ELEMENTOS
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== ADICIONANDO ELEMENTOS ===")

conjunto = {1, 2, 3}
print(f"Original: {conjunto}")

# Método: add(elemento) - adiciona UM elemento
conjunto.add(4)
print(f"\nApós add(4): {conjunto}")
print(f"  → Adicionou 4 ao conjunto")

# Tentar adicionar elemento duplicado
conjunto.add(2)
print(f"\nApós add(2) - elemento que já existe: {conjunto}")
print(f"  → Não mudou! Conjuntos não permitem duplicatas")

# Método: update(iterável) - adiciona MÚLTIPLOS elementos
conjunto.update([5, 6, 7])
print(f"\nApós update([5, 6, 7]): {conjunto}")
print(f"  → Adicionou cada elemento de [5, 6, 7]")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 4: REMOVENDO ELEMENTOS
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== REMOVENDO ELEMENTOS ===")

conjunto = {1, 2, 3, 4, 5}
print(f"Original: {conjunto}")

# Método 1: pop() - remove e retorna UM elemento aleatório
# (conjuntos não têm ordem, então não sabemos qual será removido)
removido = conjunto.pop()
print(f"\nApós pop(): {conjunto}")
print(f"  → Removeu elemento aleatório: {removido}")
print(f"  → Conjuntos não têm ordem, então pop() é imprevisível")

# Método 2: discard(elemento) - remove um elemento ESPECÍFICO
# NÃO gera erro se elemento não existir
conjunto.discard(2)
print(f"\nApós discard(2): {conjunto}")
print(f"  → Removeu 2 sem gerar erro")

# Tentar descartar elemento que não existe
conjunto.discard(999)
print(f"\nApós discard(999) - elemento que não existe: {conjunto}")
print(f"  → Nenhum erro, simplesmente não faz nada")

# Método 3: remove(elemento) - remove elemento ESPECÍFICO
# GERA erro se elemento não existir
conjunto.remove(3)
print(f"\nApós remove(3): {conjunto}")
print(f"  → Removeu 3")

# Tentar remover elemento que não existe
print(f"\nTentando remove(999) - elemento que não existe:")
try:
    conjunto.remove(999)
except KeyError as e:
    print(f"  ❌ ERRO: KeyError - {e}")
    print(f"  → remove() gera erro se elemento não existir")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 5: OPERAÇÕES DE CONJUNTO - MATEMÁTICA DE CONJUNTOS
# ─────────────────────────────────────────────────────────────────────────────

# Python permite operações matemáticas com conjuntos!

print("\n=== OPERAÇÕES DE CONJUNTO ===")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"A: {a}")
print(f"B: {b}\n")

# UNIÃO (|) - TODOS elementos de A OU de B
print(f"União (A | B): {a | b}")
print(f"  → Elementos que aparecem em A OU em B (ou em ambos)")
print(f"  → {1, 2, 3, 4, 5, 6}")

# INTERSEÇÃO (&) - Elementos COMUNS a A E B
print(f"\nInterseção (A & B): {a & b}")
print(f"  → Elementos que aparecem em A E em B simultaneamente")
print(f"  → {3, 4}")

# DIFERENÇA (-) - Elementos em A mas NÃO em B
print(f"\nDiferença (A - B): {a - b}")
print(f"  → Elementos de A que NÃO estão em B")
print(f"  → {1, 2}")

# DIFERENÇA SIMÉTRICA (^) - Elementos em UM ou OUTRO, mas não em AMBOS
print(f"\nDiferença Simétrica (A ^ B): {a ^ b}")
print(f"  → Elementos que estão em A OU em B, mas NÃO em ambos")
print(f"  → {1, 2, 5, 6}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 6: VERIFICAÇÕES - TESTAR RELAÇÕES ENTRE CONJUNTOS
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== VERIFICAÇÕES ===")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Verificar se ELEMENTO está no conjunto
print(f"3 em A: {3 in a}")
print(f"  → True porque 3 está em {a}")

print(f"\n10 em A: {10 in a}")
print(f"  → False porque 10 não está em {a}")

# Igualdade
print(f"\nA == B: {a == b}")
print(f"  → False porque têm elementos diferentes")

# SUBCONJUNTO (<=) - Todos elementos de A estão em B?
subconjunto_teste = {1, 2, 3, 4, 5}
print(f"\nA é subconjunto de {{1,2,3,4,5}}?: {a <= subconjunto_teste}")
print(f"  → True porque todos elementos de {a} estão em {subconjunto_teste}")

# SUPERCONJUNTO (>=) - A contém todos elementos de B?
print(f"\nA é superconjunto de {{1, 2}}?: {a >= {1, 2}}")
print(f"  → True porque {a} contém {1, 2}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 7: ITERAÇÃO - PERCORRER ELEMENTOS
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== ITERAÇÃO ===")

conjunto = {'a', 'b', 'c', 'd'}
print(f"Conjunto: {conjunto}")
print("Iterando sobre conjunto:")

for elemento in conjunto:
    print(f"  {elemento}")

print(f"  → Ordem pode variar (conjuntos não são ordenados)")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 8: COMPREENSÃO DE CONJUNTO
# ─────────────────────────────────────────────────────────────────────────────

# Sintaxe: {expressão for elemento in iterável if condição}
# Forma elegante de criar conjuntos

print("\n=== COMPREENSÃO DE CONJUNTO ===")

# Exemplo 1: Quadrados de números de 1 a 5
quadrados = {x**2 for x in range(1, 6)}
print(f"Quadrados: {quadrados}")
print(f"  → Expressão x² para cada x de 1 a 5")

# Note: Ordem pode ser diferente cada vez (conjuntos não são ordenados)
print(f"  → Ordem pode variar entre execuções")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 9: PROPRIEDADES - INFORMAÇÕES SOBRE O CONJUNTO
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== PROPRIEDADES ===")

conjunto = {10, 20, 30, 40, 50}
print(f"Conjunto: {conjunto}")

# len() - Número de elementos
print(f"\nComprimento (len): {len(conjunto)}")
print(f"  → Tem {len(conjunto)} elementos")

# min() - Menor valor
print(f"Mínimo (min): {min(conjunto)}")
print(f"  → Menor elemento: {min(conjunto)}")

# max() - Maior valor
print(f"Máximo (max): {max(conjunto)}")
print(f"  → Maior elemento: {max(conjunto)}")

# sum() - Soma de todos
print(f"Soma (sum): {sum(conjunto)}")
print(f"  → 10 + 20 + 30 + 40 + 50 = {sum(conjunto)}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 10: FROZENSET - CONJUNTO IMUTÁVEL
# ─────────────────────────────────────────────────────────────────────────────

# frozenset é um conjunto imutável (não pode ser modificado)
# Útil quando precisa usar um conjunto como chave em dicionário

print("\n=== FROZENSET (CONJUNTO IMUTÁVEL) ===")

# Criar frozenset
fset = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {fset}")
print(f"  → Tipo: {type(fset)}")

# Operações de leitura funcionam
print(f"  → 3 em frozenset: {3 in fset}")

# Tentar modificar
print(f"\nTentando add(6) em frozenset:")
try:
    fset.add(6)
except AttributeError as e:
    print(f"  ❌ ERRO: {e}")
    print(f"  → Frozensets não têm método add()")

print(f"\n✓ Frozensets não podem ser modificados após criação")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 11: CASO PRÁTICO - REMOVER DUPLICATAS
# ─────────────────────────────────────────────────────────────────────────────

# Um dos usos mais comuns de conjuntos

print("\n=== CASO PRÁTICO: REMOVER DUPLICATAS ===")

numeros = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
print(f"Lista com duplicatas: {numeros}")
print(f"  → Tem {len(numeros)} elementos")

# Converter para conjunto e de volta para lista
unicos = list(set(numeros))
print(f"\nApós set() e list(): {sorted(unicos)}")
print(f"  → Tem {len(unicos)} elementos únicos")

# Comparação
print(f"\nDiferença: {len(numeros) - len(unicos)} duplicatas removidas")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 12: LIMPANDO UM CONJUNTO
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== LIMPANDO CONJUNTO ===")

conjunto = {1, 2, 3}
print(f"Antes: {conjunto}")

# Método: clear() - remove TODOS os elementos
conjunto.clear()
print(f"Depois de clear(): {conjunto}")
print(f"  → Conjunto está vazio")
