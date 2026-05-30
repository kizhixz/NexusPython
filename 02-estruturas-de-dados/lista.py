"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                  ESTRUTURA DE DADOS: LISTA (LIST)                            ║
╚═══════════════════════════════════════════════════════════════════════════════╝

CARACTERÍSTICAS PRINCIPAIS:
  ✓ Ordenada: Mantém a ordem dos elementos (índice 0, 1, 2, ...)
  ✓ Mutável: Pode ser modificada após criação (adicionar, remover, alterar)
  ✓ Heterogênea: Pode conter elementos de tipos diferentes
  ✓ Indexável: Acesso direto via índice (lista[0], lista[1], etc)
  ✓ Permite Duplicatas: Pode conter o mesmo elemento múltiplas vezes

PERFORMANCE:
  - Acesso por índice: O(1) - Rápido
  - Busca linear: O(n) - Lento em listas grandes
  - Inserção no final: O(1) - Rápido
  - Inserção no início: O(n) - Lento (precisa reorganizar)
  - Remoção: O(n) - Lento dependendo da posição

QUANDO USAR:
  - Quando precisa de uma coleção que muda tamanho
  - Dados que precisam de ordem específica
  - Quando precisa adicionar/remover elementos frequentemente
  - Iteração sobre uma coleção
"""

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 1: CRIANDO LISTAS
# ─────────────────────────────────────────────────────────────────────────────

# Lista vazia - É criada sem nenhum elemento
lista_vazia = []

# Lista com números - Todos do mesmo tipo (int)
lista_numeros = [1, 2, 3, 4, 5]

# Lista mista - Contém diferentes tipos de dados (int, str, float, bool, None)
# Isso é permitido em Python (linguagem dinamicamente tipada)
lista_mista = [1, "Python", 3.14, True, None]

print("=== CRIANDO LISTAS ===")
print(f"Lista vazia: {lista_vazia}")
print(f"  → Comprimento: {len(lista_vazia)} (sem elementos)")
print(f"\nLista de números: {lista_numeros}")
print(f"  → Tipos: {[type(x).__name__ for x in lista_numeros]}")
print(f"Lista mista: {lista_mista}")
print(f"  → Tipos: {[type(x).__name__ for x in lista_mista]}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 2: ACESSANDO ELEMENTOS POR ÍNDICE
# ─────────────────────────────────────────────────────────────────────────────

# Em Python, a indexação começa em 0 (zero-based indexing)
# Índices positivos: 0, 1, 2, 3, 4... (começam do início)
# Índices negativos: -1, -2, -3, -4... (começam do final)

print("\n=== ACESSANDO ELEMENTOS ===")
# Índice 0 = primeiro elemento
print(f"Primeiro elemento (índice 0): {lista_numeros[0]}")
print(f"  → lista_numeros[0] = {lista_numeros[0]}")

# Índice negativo -1 = último elemento
print(f"\nÚltimo elemento (índice -1): {lista_numeros[-1]}")
print(f"  → lista_numeros[-1] = {lista_numeros[-1]}")
print(f"  → Nota: Índices negativos contam de trás para frente")

# Índice 2 = terceiro elemento
print(f"\nTerceiro elemento (índice 2): {lista_numeros[2]}")
print(f"  → lista_numeros[2] = {lista_numeros[2]}")

# Demonstração visual de índices
print(f"\nDemonstração de índices para {lista_numeros}:")
for i, valor in enumerate(lista_numeros):
    indice_negativo = i - len(lista_numeros)
    print(f"  Posição {i} (ou {indice_negativo}): {valor}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 3: SLICING (FATIAMENTO) - EXTRAIR PARTES DA LISTA
# ─────────────────────────────────────────────────────────────────────────────

# Slicing permite extrair múltiplos elementos usando a sintaxe: lista[início:fim:passo]
# início: índice inicial (incluído) - padrão: 0
# fim: índice final (EXCLUÍDO) - padrão: len(lista)
# passo: incremento entre índices - padrão: 1

print("\n=== SLICING (FATIAMENTO) ===")

# Exemplo: lista_numeros = [1, 2, 3, 4, 5]
#          índices:        0  1  2  3  4

# Do índice 0 até 2 (o índice 3 NÃO é incluído)
print(f"elementos de índice 0 a 2 [0:3]: {lista_numeros[0:3]}")
print(f"  → Pega 0, 1, 2 (3 NÃO é incluído)")

# Começar do início até índice 3 (equivalente a [0:3])
print(f"\nPrimeiros 3 elementos [:3]: {lista_numeros[:3]}")
print(f"  → Começa do 0 por padrão")

# Últimos 2 elementos (começando de -2)
print(f"\nÚltimos 2 elementos [-2:]: {lista_numeros[-2:]}")
print(f"  → Vai até o final por padrão")

# Com passo de 2 (pega todo segundo elemento)
print(f"\nA cada 2 elementos [::2]: {lista_numeros[::2]}")
print(f"  → Posições 0, 2, 4")

# Reverter a lista (passo -1)
print(f"\nReversa [::-1]: {lista_numeros[::-1]}")
print(f"  → Passo -1 inverte a ordem")

# Combinações mais complexas
print(f"\nDe 1 até 4 com passo 2 [1:4:2]: {lista_numeros[1:4:2]}")
print(f"  → Posições 1 e 3")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 4: MÉTODOS DE MANIPULAÇÃO DA LISTA
# ─────────────────────────────────────────────────────────────────────────────

# Os métodos abaixo modificam a lista original (in-place)
# Alguns retornam valores, outros retornam None

print("\n=== MÉTODOS DE MANIPULAÇÃO ===")

# Método: append(item) - ADICIONA um elemento NO FINAL da lista
# Sintaxe: lista.append(valor)
# Retorna: None (modifica a lista no lugar)
lista = [1, 2, 3]
print(f"Lista original: {lista}")
lista.append(4)
print(f"Após append(4): {lista}")
print(f"  → Novo elemento adicionado no final")

# Método: extend(iterável) - ADICIONA MÚLTIPLOS elementos do iterável
# Sintaxe: lista.extend([a, b, c, ...])
# Diferença com append: extend adiciona cada elemento, append adiciona como lista
lista.extend([5, 6])
print(f"\nApós extend([5, 6]): {lista}")
print(f"  → Adicionou 5 e 6 como elementos individuais")

# Método: insert(índice, item) - INSERE um elemento em posição específica
# Sintaxe: lista.insert(posição, valor)
# Retorna: None
lista.insert(0, 0)
print(f"\nApós insert(0, 0): {lista}")
print(f"  → Inseriu 0 na posição 0, deslocando outros elementos")

# Método: pop(índice) - REMOVE e RETORNA o elemento em índice específico
# Sintaxe: lista.pop(posição) ou lista.pop() para remover último
# Retorna: O elemento removido
removido = lista.pop()
print(f"\nApós pop() (remove o último): {lista}")
print(f"  → Elemento removido e retornado: {removido}")

# Método: remove(valor) - REMOVE a PRIMEIRA ocorrência de um valor
# Sintaxe: lista.remove(valor)
# Retorna: None
# ATENÇÃO: Gera erro se o valor não existir
lista.remove(3)
print(f"\nApós remove(3): {lista}")
print(f"  → Removeu a primeira ocorrência de 3")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 5: ITERAÇÃO - PERCORRER OS ELEMENTOS DA LISTA
# ─────────────────────────────────────────────────────────────────────────────

# Iteração significa passar por cada elemento da lista
# É uma operação muito comum em Python

print("\n=== ITERAÇÃO ===")

# Forma 1: Iteração simples com for
# A variável 'numero' assume o valor de cada elemento, um por vez
print("Iterando sobre lista com for:")
for numero in lista:
    print(f"  {numero}")

# Forma 2: Iteração com enumerate() - quando precisa do ÍNDICE também
# enumerate() retorna tuplas (índice, valor)
print("\nCom índice (enumerate):")
for i, numero in enumerate(lista):
    print(f"  Índice {i}: {numero}")
    # i = posição na lista (0, 1, 2, ...)
    # numero = valor naquela posição


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 6: COMPREENSÃO DE LISTA - FORMA ELEGANTE E RÁPIDA DE CRIAR LISTAS
# ─────────────────────────────────────────────────────────────────────────────

# Sintaxe: [expressão for elemento in iterável if condição]
# É equivalente a um loop for, mas em uma linha
# Mais rápida e mais legível que loops tradicionais

print("\n=== COMPREENSÃO DE LISTA ===")

# Exemplo 1: Criar quadrados de números de 1 a 5
# Forma tradicional:
# quadrados = []
# for x in range(1, 6):
#     quadrados.append(x**2)
# Forma com compreensão:
quadrados = [x**2 for x in range(1, 6)]
print(f"Quadrados de 1 a 5: {quadrados}")
print(f"  → Expressa: x² para cada x de 1 a 5")

# Exemplo 2: Filtrar números pares com condição IF
# Filtra só elementos que satisfazem a condição
pares = [x for x in range(10) if x % 2 == 0]
print(f"\nNúmeros pares de 0 a 9: {pares}")
print(f"  → Retorna x onde x é divisível por 2")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 7: PROPRIEDADES E OPERAÇÕES DE QUERY (BUSCA/ANÁLISE)
# ─────────────────────────────────────────────────────────────────────────────

# Essas operações NÃO modificam a lista, apenas retornam informações

print("\n=== PROPRIEDADES ===")
lista_teste = [1, 2, 3, 2, 1]
print(f"Lista de teste: {lista_teste}")

# len(lista) - Retorna a QUANTIDADE de elementos
print(f"\nComprimento (len): {len(lista_teste)}")
print(f"  → Tem {len(lista_teste)} elementos")

# lista.count(valor) - Retorna QUANTAS VEZES um valor aparece
print(f"\nContagem de 2 (count): {lista_teste.count(2)}")
print(f"  → O número 2 aparece {lista_teste.count(2)} vezes")

# lista.index(valor) - Retorna o ÍNDICE da primeira ocorrência
print(f"\nÍndice de 3 (index): {lista_teste.index(3)}")
print(f"  → O número 3 está na posição {lista_teste.index(3)}")

# min(lista) - Retorna o VALOR MÍNIMO
print(f"\nMínimo (min): {min(lista_teste)}")
print(f"  → Menor valor: {min(lista_teste)}")

# max(lista) - Retorna o VALOR MÁXIMO
print(f"\nMáximo (max): {max(lista_teste)}")
print(f"  → Maior valor: {max(lista_teste)}")

# sum(lista) - Retorna a SOMA de todos os elementos
print(f"\nSoma (sum): {sum(lista_teste)}")
print(f"  → {lista_teste[0]} + {lista_teste[1]} + {lista_teste[2]} + {lista_teste[3]} + {lista_teste[4]} = {sum(lista_teste)}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 8: ORDENAÇÃO - ORGANIZAR ELEMENTOS EM ORDEM ESPECÍFICA
# ─────────────────────────────────────────────────────────────────────────────

# Existem duas formas de ordenar:
# 1. sorted() - função built-in que RETORNA uma nova lista ordenada
# 2. lista.sort() - método que MODIFICA a lista original no lugar

print("\n=== ORDENAÇÃO ===")
lista_desord = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista original: {lista_desord}")

# sorted(lista) - Retorna nova lista sem modificar a original
lista_ord = sorted(lista_desord)
print(f"\nsorted() - nova lista ordenada: {lista_ord}")
print(f"Original ainda é: {lista_desord}")
print(f"  → sorted() NÃO modifica a lista original")

# sorted(lista, reverse=True) - Ordena em ordem DECRESCENTE
lista_reversa = sorted(lista_desord, reverse=True)
print(f"\nOrdenada em ordem decrescente (reverse=True): {lista_reversa}")
print(f"  → Maior para menor")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 9: CÓPIA - IMPORTANTE ENTENDER REFERÊNCIAS E CÓPIAS
# ─────────────────────────────────────────────────────────────────────────────

# IMPORTANTE: Em Python, atribuição NÃO cria cópia, cria REFERÊNCIA

print("\n=== CÓPIA ===")
original = [1, 2, 3]
print(f"Lista original: {original}")

# Forma errada: Atribuição simples (cria referência, não cópia)
alias = original
alias[0] = 999
print(f"\nAlias após modificação: {alias}")
print(f"Original também foi alterada: {original}")
print(f"  → Ambas apontam para o MESMO objeto na memória!")

# Forma correta: Usar .copy() para criar cópia
original = [1, 2, 3]
copia_superficial = original.copy()
copia_superficial[0] = 999
print(f"\nApós .copy() e modificar cópia:")
print(f"Original: {original}")
print(f"Cópia: {copia_superficial}")
print(f"  → Agora são objetos DIFERENTES na memória")
