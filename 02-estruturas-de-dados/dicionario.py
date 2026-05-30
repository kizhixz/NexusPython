"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║               ESTRUTURA DE DADOS: DICIONÁRIO (DICTIONARY)                    ║
╚═══════════════════════════════════════════════════════════════════════════════╝

CARACTERÍSTICAS PRINCIPAIS:
  ✓ Chave-Valor: Armazena pares de (chave, valor)
  ✓ Mutável: Pode ser modificado após criação
  ✓ Desordenado (3.7+): Mantém ordem de inserção
  ✓ Chaves Únicas: Não pode haver chaves duplicadas
  ✓ Chaves Imutáveis: Chaves devem ser strings, números, tuplas, etc.
  ✓ Valores Variados: Valores podem ser de qualquer tipo

CHAVES VS VALORES:
  - Chaves: Devem ser IMUTÁVEIS (string, número, tupla)
  - Valores: Podem ser QUALQUER tipo (lista, dict, função, etc.)

PERFORMANCE:
  - Acesso por chave: O(1) - Muito rápido
  - Busca por valor: O(n) - Lento
  - Inserção: O(1) - Rápido
  - Remoção: O(1) - Rápido

QUANDO USAR:
  - Armazenar dados com identificadores
  - Configurações e settings
  - Estruturas de dados complexas
  - Mapeamento entre dois conjuntos de valores
"""

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 1: CRIANDO DICIONÁRIOS
# ─────────────────────────────────────────────────────────────────────────────

# Dicionário vazio - Sem elementos iniciais
dicionario_vazio = {}

# Dicionário com dados de uma pessoa
dicionario_pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Dicionário com valores numéricos (chave: string, valor: number)
dicionario_numeros = {"um": 1, "dois": 2, "três": 3}

print("=== CRIANDO DICIONÁRIOS ===")
print(f"Dicionário vazio: {dicionario_vazio}")
print(f"  → Tipo: {type(dicionario_vazio)}")

print(f"\nPessoa: {dicionario_pessoa}")
print(f"  → Chaves: {list(dicionario_pessoa.keys())}")
print(f"  → Valores: {list(dicionario_pessoa.values())}")

print(f"\nNúmeros: {dicionario_numeros}")
print(f"  → Cada chave é uma string que mapeia para um número")

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 2: ACESSANDO VALORES
# ─────────────────────────────────────────────────────────────────────────────

# Em dicionários, acessamos por CHAVE, não por índice

print("\n=== ACESSANDO VALORES ===")

# Acesso direto com dicionario['chave']
print(f"Nome: {dicionario_pessoa['nome']}")
print(f"  → Usa a chave 'nome' para acessar o valor")

print(f"Idade: {dicionario_pessoa['idade']}")
print(f"Cidade: {dicionario_pessoa['cidade']}")

print(f"\nUm: {dicionario_numeros['um']}")
print(f"Dois: {dicionario_numeros['dois']}")

# ATENÇÃO: Se a chave não existir, gera erro KeyError
print(f"\nTentando acessar chave inexistente: dicionario_pessoa['email']")
try:
    print(dicionario_pessoa['email'])
except KeyError as e:
    print(f"  ❌ ERRO: KeyError - {e}")
    print(f"  → A chave 'email' não existe neste dicionário!")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 3: MÉTODO get() - ACESSO SEGURO
# ─────────────────────────────────────────────────────────────────────────────

# get() é mais seguro que acesso direto porque não gera erro se chave não existe

print("\n=== MÉTODO GET - ACESSO SEGURO ===")

# Forma 1: Acessar chave que existe
print(f"Nome com get: {dicionario_pessoa.get('nome')}")
print(f"  → Retorna o valor normalmente")

# Forma 2: Acessar chave que NÃO existe com valor padrão
email = dicionario_pessoa.get('email', 'não informado')
print(f"\nEmail (não existe): {email}")
print(f"  → Como 'email' não existe, retorna 'não informado'")

# Comparação: acesso direto vs get()
print(f"\nComparação - Acessar 'telefone':")

print(f"  Forma 1 - Acesso direto []: ", end="")
try:
    print(dicionario_pessoa['telefone'])
except KeyError:
    print("❌ ERRO - KeyError!")

print(f"  Forma 2 - get() com padrão: {dicionario_pessoa.get('telefone', 'N/A')}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 4: ADICIONANDO E MODIFICANDO ELEMENTOS
# ─────────────────────────────────────────────────────────────────────────────

# Dicionários são MUTÁVEIS, então podemos adicionar e modificar elementos

print("\n=== ADICIONANDO E MODIFICANDO ===")

dicionario = {"a": 1, "b": 2}
print(f"Dicionário original: {dicionario}")

# Adicionar nova chave-valor
dicionario["c"] = 3
print(f"\nApós adicionar 'c': {dicionario}")
print(f"  → Sintaxe: dicionario['chave'] = valor")

# Modificar valor existente
dicionario["a"] = 10
print(f"\nApós modificar 'a' (era 1, agora é 10): {dicionario}")
print(f"  → Se a chave existe, substitui o valor")

# Método update() - adiciona/modifica múltiplos elementos de uma vez
dicionario.update({"d": 4, "e": 5})
print(f"\nApós update({{'d': 4, 'e': 5}}): {dicionario}")
print(f"  → Adiciona múltiplas chaves-valores")

# Modificar com update() - sobrescreve valores existentes
dicionario.update({"a": 100, "f": 6})
print(f"Após update({{'a': 100, 'f': 6}}): {dicionario}")
print(f"  → 'a' foi modificado de 10 para 100")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 5: REMOVENDO ELEMENTOS
# ─────────────────────────────────────────────────────────────────────────────

# Existem várias formas de remover pares chave-valor

print("\n=== REMOVENDO ELEMENTOS ===")

dicionario = {"a": 1, "b": 2, "c": 3}
print(f"Original: {dicionario}")

# Método 1: pop(chave) - remove e retorna o valor
removido = dicionario.pop("b")
print(f"\nApós pop('b'): {dicionario}")
print(f"  → Elemento removido e retornado: {removido}")
print(f"  → Gera erro se a chave não existir")

# Método 2: popitem() - remove um item aleatório (par chave-valor)
chave, valor = dicionario.popitem()
print(f"\nApós popitem(): {dicionario}")
print(f"  → Removeu: {chave}: {valor}")

# Método 3: del - remove uma chave específica
del dicionario["a"]
print(f"\nApós del ['a']: {dicionario}")
print(f"  → Gera erro se a chave não existir")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 6: ITERAÇÃO - PERCORRER ELEMENTOS DO DICIONÁRIO
# ─────────────────────────────────────────────────────────────────────────────

# Em dicionários, temos 3 formas principais de iterar

print("\n=== ITERAÇÃO ===")

pessoa = {"nome": "Maria", "idade": 25, "profissão": "Engenheira"}

# Forma 1: Iterar sobre CHAVES (padrão)
print("Iterando sobre chaves (for chave in dicio):")
for chave in pessoa:
    print(f"  {chave}: {pessoa[chave]}")
print(f"  → Quando itera sozinho, pega só as chaves")

# Forma 2: Iterar sobre ITEMS (chave e valor juntos)
print("\nIterando sobre items (for chave, valor in dicio.items()):")
for chave, valor in pessoa.items():
    print(f"  {chave}: {valor}")
print(f"  → items() retorna tuplas (chave, valor)")

# Forma 3: Iterar sobre VALORES
print("\nIterando sobre valores (for valor in dicio.values()):")
for valor in pessoa.values():
    print(f"  {valor}")
print(f"  → Quando só precisa dos valores")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 7: OPERAÇÕES COM DICIONÁRIOS
# ─────────────────────────────────────────────────────────────────────────────

# Diversas operações para inspecionar e trabalhar com dicionários

print("\n=== OPERAÇÕES ===")

dicio = {"x": 1, "y": 2, "z": 3}
print(f"Dicionário: {dicio}")

# keys() - Retorna TODAS as chaves
print(f"\nChaves (keys): {list(dicio.keys())}")
print(f"  → Retorna um objeto dict_keys, convertemos para lista")

# values() - Retorna TODOS os valores
print(f"Valores (values): {list(dicio.values())}")
print(f"  → Retorna um objeto dict_values")

# items() - Retorna todos os pares (chave, valor)
print(f"Items (items): {list(dicio.items())}")
print(f"  → Cada item é uma tupla (chave, valor)")

# len() - Número de pares chave-valor
print(f"\nComprimento (len): {len(dicio)}")
print(f"  → Tem {len(dicio)} pares chave-valor")

# in - Verificar se CHAVE existe
print(f"\n'x' existe?: {'x' in dicio}")
print(f"'w' existe?: {'w' in dicio}")
print(f"  → Verifica se a CHAVE está no dicionário")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 8: COMPREENSÃO DE DICIONÁRIO
# ─────────────────────────────────────────────────────────────────────────────

# Sintaxe: {chave: valor for ... in ...}
# Forma elegante e rápida de criar dicionários

print("\n=== COMPREENSÃO DE DICIONÁRIO ===")

# Exemplo 1: Criar dicionário de quadrados
# Forma normal:
# quadrados = {}
# for x in range(1, 6):
#     quadrados[x] = x**2
# Forma com compreensão:
quadrados = {x: x**2 for x in range(1, 6)}
print(f"Quadrados: {quadrados}")
print(f"  → Chave = número, Valor = número ao quadrado")

# Exemplo 2: Compreensão com FILTRO (IF)
# Criar dicionário só com pares
pares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"\nPares elevados ao quadrado: {pares}")
print(f"  → Só inclui números pares (x % 2 == 0)")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 9: DICIONÁRIOS ANINHADOS - ESTRUTURAS COMPLEXAS
# ─────────────────────────────────────────────────────────────────────────────

# Dicionários podem conter outros dicionários, formando estruturas complexas

print("\n=== DICIONÁRIOS ANINHADOS ===")

# Dicionário de funcionários, cada um tem seus dados
empresa = {
    "funcionario1": {"nome": "Ana", "cargo": "Dev", "salario": 3000},
    "funcionario2": {"nome": "Bruno", "cargo": "DBA", "salario": 4000},
    "funcionario3": {"nome": "Carlos", "cargo": "QA", "salario": 2500}
}

print(f"Estrutura empresa:")
print(f"  Tem {len(empresa)} funcionários\n")

# Acessar dados aninhados
print(f"Nome do funcionário 1: {empresa['funcionario1']['nome']}")
print(f"  → empresa['funcionario1'] = {empresa['funcionario1']}")
print(f"  → empresa['funcionario1']['nome'] = {empresa['funcionario1']['nome']}")

print(f"\nCargo do funcionário 2: {empresa['funcionario2']['cargo']}")

# Iterar sobre estrutura aninhada
print(f"\nTodos os funcionários:")
for id_func, dados in empresa.items():
    print(f"  {id_func}:")
    print(f"    Nome: {dados['nome']}")
    print(f"    Cargo: {dados['cargo']}")
    print(f"    Salário: R$ {dados['salario']:.2f}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 10: CÓPIA - IMPORTANTE PARA EVITAR BUGS
# ─────────────────────────────────────────────────────────────────────────────

# Assim como listas, dicionários precisam de cuidado com cópia vs referência

print("\n=== CÓPIA ===")

original = {"a": 1, "b": 2}
print(f"Original: {original}")

# Forma ERRADA: Atribuição simples (cria referência)
alias = original
alias["a"] = 999
print(f"\nAntes de .copy():")
print(f"  Original: {original}")
print(f"  ❌ Original foi alterado também!")

# Forma CORRETA: Usar .copy()
original = {"a": 1, "b": 2}
copia = original.copy()
copia["a"] = 999
print(f"\nDepois de .copy():")
print(f"  Original: {original}")
print(f"  Cópia: {copia}")
print(f"  ✓ Agora são objetos diferentes")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 11: SETDEFAULT - OBTER COM VALOR PADRÃO
# ─────────────────────────────────────────────────────────────────────────────

# setdefault() é como get(), mas ADICIONA a chave se não existir

print("\n=== SETDEFAULT ===")

dicio = {"a": 1}
print(f"Dicionário inicial: {dicio}")

# setdefault com chave que EXISTE
valor = dicio.setdefault('a', 100)
print(f"\nsetdefault('a', 100): {valor}")
print(f"  → Retorna o valor existente (1)")
print(f"  → Não altera nada")

# setdefault com chave que NÃO EXISTE
valor = dicio.setdefault('b', 200)
print(f"\nsetdefault('b', 200): {valor}")
print(f"  → Chave 'b' não existia, então:")
print(f"  → Adiciona 'b': 200 ao dicionário")
print(f"  → E retorna 200")

print(f"\nDicionário final: {dicio}")
print(f"  → 'b' foi adicionado automaticamente")
