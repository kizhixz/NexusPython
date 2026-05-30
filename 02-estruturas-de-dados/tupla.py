"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                  ESTRUTURA DE DADOS: TUPLA (TUPLE)                           ║
╚═══════════════════════════════════════════════════════════════════════════════╝

CARACTERÍSTICAS PRINCIPAIS:
  ✓ Ordenada: Mantém a ordem dos elementos
  ✓ IMUTÁVEL: NÃO pode ser modificada após criação (não adiciona/remove/altera)
  ✓ Heterogênea: Pode conter elementos de tipos diferentes
  ✓ Indexável: Acesso via índice (como listas)
  ✓ Permite Duplicatas: Pode conter o mesmo elemento múltiplas vezes

IMUTABILIDADE: A diferença mais importante com listas!
  - Não pode fazer: tupla[0] = novo_valor
  - Não pode fazer: tupla.append(valor)
  - Não pode fazer: tupla.remove(valor)
  → Gera erro AttributeError ou TypeError

PERFORMANCE VS LISTA:
  - Acesso: Similar a listas O(1)
  - Criação: Tuplas são mais rápidas (imutáveis)
  - Memória: Tuplas usam menos memória
  - Iteração: Similar a listas

QUANDO USAR:
  - Dados que NÃO devem ser modificados
  - Chaves de dicionários (listas não podem!)
  - Retornar múltiplos valores de funções
  - Quando precisa de performance crítica
  - Proteger dados contra modificação acidental
"""

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 1: CRIANDO TUPLAS
# ─────────────────────────────────────────────────────────────────────────────

# Tupla vazia - Sem nenhum elemento
tupla_vazia = ()

# Tupla com números
tupla_numeros = (1, 2, 3, 4, 5)

# Tupla mista - Diferentes tipos de dados
tupla_mista = (1, "Python", 3.14, True)

# Tupla com um ÚNICO elemento - A VÍRGULA É ESSENCIAL!
# Sem vírgula: (42) = apenas um número
# Com vírgula: (42,) = tupla com um elemento
tupla_um_elemento = (42,)

# Parênteses são opcionais, mas recomendados para clareza
tupla_sem_parentes = 1, 2, 3  # Isso também é uma tupla!

print("=== CRIANDO TUPLAS ===")
print(f"Tupla vazia: {tupla_vazia}")
print(f"  → Tipo: {type(tupla_vazia)}, Comprimento: {len(tupla_vazia)}")

print(f"\nTupla de números: {tupla_numeros}")
print(f"  → Tipo: {type(tupla_numeros)}, Comprimento: {len(tupla_numeros)}")

print(f"\nTupla mista: {tupla_mista}")
print(f"  → Tipos dentro: {[type(x).__name__ for x in tupla_mista]}")

print(f"\nTupla com um elemento: {tupla_um_elemento}")
print(f"  → IMPORTANTE: A vírgula torna isso uma tupla!")
print(f"  → Sem vírgula (42) seria apenas um int")

print(f"\nTupla sem parênteses: {tupla_sem_parentes}")
print(f"  → Parênteses são opcionais em tuplas")

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 2: ACESSANDO ELEMENTOS
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== ACESSANDO ELEMENTOS ===")
print(f"Tupla para referência: {tupla_numeros}")

# Acesso é idêntico a listas
print(f"\nPrimeiro elemento (índice 0): {tupla_numeros[0]}")
print(f"Último elemento (índice -1): {tupla_numeros[-1]}")

# Slicing também funciona igual
print(f"\nSlicing [1:3]: {tupla_numeros[1:3]}")
print(f"  → Do índice 1 até 3 (3 não incluído)")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 3: ITERAÇÃO - PERCORRER ELEMENTOS
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== ITERAÇÃO ===")

# Iteração simples com for
print("Iterando sobre tupla:")
for numero in tupla_numeros:
    print(f"  {numero}")

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 4: DESEMPACOTAMENTO (UNPACKING) - RECURSO PODEROSO DE TUPLAS!
# ─────────────────────────────────────────────────────────────────────────────

# Desempacotamento permite extrair elementos de uma tupla e atribuir a variáveis
# SIMULTANEAMENTE, em uma única linha

print("\n=== DESEMPACOTAMENTO ===")

tupla = (1, 2, 3)
# Desempaca os valores para 3 variáveis diferentes
a, b, c = tupla

print(f"Tupla: {tupla}")
print(f"Após desempacotar: a={a}, b={b}, c={c}")
print(f"  → Cada elemento foi atribuído a uma variável")

# Casos práticos de desempacotamento
print("\n--- Casos Práticos de Desempacotamento ---")

# Caso 1: Trocar valores de duas variáveis (o clássico uso!)
x, y = 10, 20
print(f"\nAntes: x={x}, y={y}")
x, y = y, x  # Troca em uma linha!
print(f"Depois de x, y = y, x: x={x}, y={y}")
print(f"  → Forma elegante de trocar valores")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 5: TUPLAS EM FUNÇÕES - RETORNAR MÚLTIPLOS VALORES
# ─────────────────────────────────────────────────────────────────────────────

# Uma forma comum de usar tuplas: retornar múltiplos valores de uma função

print("\n=== TUPLAS EM FUNÇÕES ===")

# Função que retorna múltiplos valores como tupla
def coordenadas():
    """Retorna coordenadas x e y como uma tupla"""
    return (10, 20)

# Forma 1: Receber como tupla
resultado = coordenadas()
print(f"Resultado: {resultado}")
print(f"  → Tipo: {type(resultado)}")

# Forma 2: Desempacotar diretamente na atribuição
x, y = coordenadas()
print(f"\nCom desempacotamento: x={x}, y={y}")
print(f"  → Muito mais elegante e legível!")

# Outro exemplo: Função que retorna múltiplos valores
def divmod_customizado(dividendo, divisor):
    """Retorna quociente e resto como tupla"""
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto  # Retorna tupla sem parênteses

q, r = divmod_customizado(17, 5)
print(f"\n17 ÷ 5:")
print(f"  Quociente: {q}, Resto: {r}")
print(f"  → Verificação: {q} × 5 + {r} = {q*5 + r}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 6: MÉTODOS DE TUPLAS (LIMITADOS - porque são imutáveis!)
# ─────────────────────────────────────────────────────────────────────────────

# Tuplas têm APENAS 2 métodos, diferente de listas que têm muitos
# Isso é porque não podem ser modificadas

print("\n=== MÉTODOS ===")
tupla_teste = (1, 2, 3, 2, 1)
print(f"Tupla: {tupla_teste}")

# Método 1: count(valor) - Conta quantas vezes um valor aparece
quantidade = tupla_teste.count(2)
print(f"\ncontagem de 2: {quantidade}")
print(f"  → O número 2 aparece {quantidade} vezes")

# Método 2: index(valor) - Retorna o índice da primeira ocorrência
indice = tupla_teste.index(3)
print(f"\nÍndice de 3: {indice}")
print(f"  → O número 3 está na posição {indice}")
print(f"  → Gera erro se o valor não existir")

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 7: PROPRIEDADES - FUNÇÕES BUILT-IN
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== PROPRIEDADES ===")

# len() - Quantos elementos?
print(f"Comprimento: {len(tupla_teste)}")
print(f"  → Tem {len(tupla_teste)} elementos")

# min() - Qual o MENOR valor?
print(f"\nMínimo: {min(tupla_teste)}")

# max() - Qual o MAIOR valor?
print(f"Máximo: {max(tupla_teste)}")

# sum() - Qual a SOMA de todos?
print(f"Soma: {sum(tupla_teste)}")
print(f"  → {tupla_teste[0]} + {tupla_teste[1]} + {tupla_teste[2]} + {tupla_teste[3]} + {tupla_teste[4]} = {sum(tupla_teste)}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 8: IMUTABILIDADE - A CARACTERÍSTICA FUNDAMENTAL DE TUPLAS
# ─────────────────────────────────────────────────────────────────────────────

# IMUTÁVEL = NÃO PODE SER MODIFICADA!

print("\n=== IMUTABILIDADE ===")
print(f"Tupla original: {tupla_numeros}")

# Tentativa 1: Modificar um elemento
print("\nTentando modificar: tupla_numeros[0] = 10")
try:
    tupla_numeros[0] = 10
except TypeError as e:
    print(f"  ❌ ERRO: {e}")
    print(f"  → Tuplas não suportam atribuição de item")

# Tentativa 2: Adicionar elemento
print("\nTentando adicionar: tupla_numeros.append(6)")
try:
    tupla_numeros.append(6)
except AttributeError as e:
    print(f"  ❌ ERRO: {e}")
    print(f"  → Tuplas não têm método append()")

# Tentativa 3: Remover elemento
print("\nTentando remover: tupla_numeros.remove(1)")
try:
    tupla_numeros.remove(1)
except AttributeError as e:
    print(f"  ❌ ERRO: {e}")
    print(f"  → Tuplas não têm método remove()")

print("\n✓ Tuplas não podem ser modificadas após criação!")
print("✓ Isso as torna seguras para usar como chaves em dicionários")
print("✓ E é mais eficiente em termos de memória e performance")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 9: TUPLAS ANINHADAS (TUPLAS DENTRO DE TUPLAS)
# ─────────────────────────────────────────────────────────────────────────────

# Tuplas podem conter outras tuplas, formando estruturas multidimensionais

print("\n=== TUPLAS ANINHADAS ===")

# Matriz representada como tupla de tuplas
matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"Matriz: {matriz}")
print(f"  → É uma tupla com 3 elementos")
print(f"  → Cada elemento é uma tupla com 3 números")

# Acessando elementos aninhados
print(f"\nPrimeira linha (matriz[0]): {matriz[0]}")
print(f"  → Essa é a primeira tupla dentro da tupla")

print(f"\nElemento [1][2] (segunda linha, terceira coluna): {matriz[1][2]}")
print(f"  → matriz[1] = {matriz[1]}")
print(f"  → matriz[1][2] = {matriz[1][2]}")

# Iterando sobre matriz
print(f"\nIterando sobre a matriz:")
for i, linha in enumerate(matriz):
    print(f"  Linha {i}: {linha}")
    for j, valor in enumerate(linha):
        print(f"    [{i}][{j}] = {valor}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 10: CONVERSÃO - TRANSFORMAR ENTRE LISTA E TUPLA
# ─────────────────────────────────────────────────────────────────────────────

# Às vezes precisa converter de um tipo para outro

print("\n=== CONVERSÃO ===")

# Lista para Tupla com tuple()
lista = [1, 2, 3]
tupla = tuple(lista)
print(f"Lista para tupla:")
print(f"  Lista original: {lista} (tipo: {type(lista).__name__})")
print(f"  Tupla resultante: {tupla} (tipo: {type(tupla).__name__})")

# Tupla para Lista com list()
tupla2 = (4, 5, 6)
lista2 = list(tupla2)
print(f"\nTupla para lista:")
print(f"  Tupla original: {tupla2} (tipo: {type(tupla2).__name__})")
print(f"  Lista resultante: {lista2} (tipo: {type(lista2).__name__})")

# Quando usar?
print(f"\nQuando converter:")
print(f"  ✓ Lista → Tupla: Quando quer proteger dados contra modificação")
print(f"  ✓ Tupla → Lista: Quando precisa adicionar/remover elementos")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 11: NAMED TUPLES - TUPLAS COM CAMPOS NOMEADOS
# ─────────────────────────────────────────────────────────────────────────────

# Named tuples são uma versão "melhorada" de tuplas
# Permitem acessar elementos por NOME em vez de apenas por índice

print("\n=== NAMED TUPLES ===")

from collections import namedtuple

# Criar um tipo de namedtuple chamado 'Ponto'
# com campos 'x' e 'y'
Ponto = namedtuple('Ponto', ['x', 'y'])

# Criar uma instância
p = Ponto(3, 4)

print(f"Ponto criado: {p}")
print(f"  → Tipo: {type(p)}")
print(f"  → É uma tupla especial com campos nomeados")

# Acessar por ÍNDICE (como tupla normal)
print(f"\nAcesso por índice:")
print(f"  p[0] = {p[0]}")
print(f"  p[1] = {p[1]}")

# Acessar por NOME (muito mais legível!)
print(f"\nAcesso por nome (muito melhor!):")
print(f"  p.x = {p.x}")
print(f"  p.y = {p.y}")

# Usar em cálculos
distancia = (p.x**2 + p.y**2)**0.5
print(f"\nDistância da origem: {distancia:.2f}")
print(f"  → Cálculo: √({p.x}² + {p.y}²) = {distancia:.2f}")

# Named tuple com mais campos
print(f"\n--- Outro Exemplo ---")
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'cidade'])
pessoa1 = Pessoa('Alice', 30, 'São Paulo')

print(f"Pessoa: {pessoa1}")
print(f"  Nome: {pessoa1.nome}")
print(f"  Idade: {pessoa1.idade}")
print(f"  Cidade: {pessoa1.cidade}")

