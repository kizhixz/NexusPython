# 02 - Estruturas de Dados

Bem-vindo à seção de Estruturas de Dados! Aqui você vai aprender sobre as estruturas fundamentais usadas na programação Python.

## O que são Estruturas de Dados?

Estruturas de dados são formas organizadas de armazenar e gerenciar dados. Elas definem como os dados são organizados, armazenados e manipulados, afetando diretamente a eficiência e a performance dos programas.

## Estruturas de Dados Nativas do Python

### 1. **Lista (List)** 📋
- **Arquivo:** [lista.py](lista.py)
- **Características:**
  - Coleção **ordenada** de elementos
  - **Mutável** (pode ser modificada)
  - Permite elementos **duplicados**
  - Indexação começa em 0
  - Sintaxe: `[1, 2, 3, 4, 5]`

- **Operações principais:**
  - `append()` - adiciona um elemento
  - `remove()` - remove um elemento específico
  - `pop()` - remove e retorna um elemento
  - `insert()` - insere em posição específica
  - `sort()` - ordena a lista
  - Slicing: `lista[0:3]`, `lista[:3]`, `lista[-2:]`

- **Quando usar:**
  - Coleções que mudam tamanho
  - Dados que precisam ser reordenados
  - Quando precisa de indexação e slicing

```python
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)  # [1, 2, 3, 4, 5, 6]
```

---

### 2. **Tupla (Tuple)** 🔒
- **Arquivo:** [tupla.py](tupla.py)
- **Características:**
  - Coleção **ordenada** de elementos
  - **Imutável** (não pode ser modificada)
  - Permite elementos **duplicados**
  - Mais rápida que lista
  - Sintaxe: `(1, 2, 3, 4, 5)` ou `1, 2, 3`

- **Operações principais:**
  - `count()` - conta ocorrências
  - `index()` - encontra a posição
  - Slicing (igual à lista)
  - Desempacotamento: `a, b, c = (1, 2, 3)`

- **Quando usar:**
  - Dados que não devem mudar
  - Chaves de dicionários (listas não podem)
  - Retornar múltiplos valores de funções
  - Performance crítica

```python
coordenadas = (10, 20)
x, y = coordenadas  # Desempacotamento
print(x, y)  # 10 20
```

---

### 3. **Dicionário (Dictionary)** 📖
- **Arquivo:** [dicionario.py](dicionario.py)
- **Características:**
  - Coleção de pares **chave-valor**
  - **Mutável** (pode ser modificada)
  - Chaves devem ser **únicas**
  - Não há ordem garantida (Python 3.7+ mantém inserção)
  - Sintaxe: `{"chave": valor, "nome": "João"}`

- **Operações principais:**
  - `get()` - obtém valor (seguro)
  - `keys()` - retorna chaves
  - `values()` - retorna valores
  - `items()` - retorna pares chave-valor
  - `pop()` - remove e retorna
  - `update()` - atualiza múltiplos

- **Quando usar:**
  - Dados estruturados com identificadores
  - Mapeamento entre chaves e valores
  - Dados com muitos atributos
  - Configurações e settings

```python
pessoa = {"nome": "Maria", "idade": 30, "cidade": "São Paulo"}
print(pessoa["nome"])  # Maria
print(pessoa.get("email", "não informado"))  # não informado
```

---

### 4. **Conjunto (Set)** ⭐
- **Arquivo:** [conjunto.py](conjunto.py)
- **Características:**
  - Coleção de elementos **únicos**
  - **Mutável** (pode ser modificada)
  - **Não-ordenada**
  - Remove duplicatas automaticamente
  - Sintaxe: `{1, 2, 3, 4, 5}` (não confundir com dicionário)

- **Operações principais:**
  - `add()` - adiciona um elemento
  - `remove()` - remove um elemento
  - `union()` ou `|` - união
  - `intersection()` ou `&` - interseção
  - `difference()` ou `-` - diferença
  - `symmetric_difference()` ou `^` - diferença simétrica

- **Quando usar:**
  - Remover duplicatas
  - Operações matemáticas (união, interseção)
  - Verificar pertencimento (mais rápido)
  - Dados que precisam ser únicos

```python
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)  # {1, 2, 3} - duplicatas removidas

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5} - união
print(a & b)  # {3} - interseção
```

---

## Estruturas de Dados Especializadas

### 5. **Pilha (Stack)** 📚
- **Arquivo:** [pilha.py](pilha.py)
- **Princípio:** LIFO (Last In, First Out)
- **Último a entrar é o primeiro a sair**

- **Operações principais:**
  - `push()` - adiciona no topo
  - `pop()` - remove do topo
  - `peek()` - visualiza o topo
  - `is_vazia()` - verifica se está vazia

- **Casos de uso:**
  - Função desfazer (Undo)
  - Verificar parênteses balanceados
  - Inverter strings ou listas
  - Algoritmos de backtracking
  - Avaliação de expressões

```python
pilha = []
pilha.append(1)     # push
pilha.append(2)
pilha.append(3)
print(pilha.pop())  # 3 (saiu último a entrar)
```

---

### 6. **Fila (Queue)** 🚶
- **Arquivo:** [fila.py](fila.py)
- **Princípio:** FIFO (First In, First Out)
- **Primeiro a entrar é o primeiro a sair**

- **Operações principais:**
  - `enqueue()` - adiciona ao final
  - `dequeue()` - remove do início
  - `peek()` - visualiza o início
  - `is_vazia()` - verifica se está vazia

- **Casos de uso:**
  - Fila de atendimento
  - Fila de impressão
  - Processamento de tarefas
  - BFS (Breadth-First Search)
  - Sistemas de simulação

```python
from collections import deque

fila = deque()
fila.append(1)          # enqueue
fila.append(2)
fila.append(3)
print(fila.popleft())   # 1 (saiu primeiro a entrar)
```

---

## Comparação Resumida

| Estrutura | Ordenada | Mutável | Duplicatas | Acesso | Melhor uso |
|-----------|----------|---------|-----------|--------|-----------|
| Lista | ✅ | ✅ | ✅ | Índice | Coleções que mudam |
| Tupla | ✅ | ❌ | ✅ | Índice | Dados imutáveis |
| Dicionário | ✅* | ✅ | ❌** | Chave | Pares chave-valor |
| Conjunto | ❌ | ✅ | ❌ | Pertencimento | Elementos únicos |
| Pilha | ✅ | ✅ | ✅ | LIFO | Undo, recursão |
| Fila | ✅ | ✅ | ✅ | FIFO | Processamento sequencial |

*Python 3.7+ mantém a ordem de inserção
**Chaves deve ser únicas

---

## Métodos e Funções Úteis

### Funções Built-in
```python
len()        # Tamanho
min()        # Mínimo
max()        # Máximo
sum()        # Soma
sorted()     # Ordena
reversed()   # Reverte ordem
enumerate()  # Índice e elemento
zip()        # Combina sequências
```

### Compreensões
```python
# Compreensão de lista
[x**2 for x in range(10)]

# Compreensão de conjunto
{x for x in range(10) if x % 2 == 0}

# Compreensão de dicionário
{x: x**2 for x in range(1, 6)}
```

---

## Como Usar os Arquivos

1. **Execute os exemplos:**
   ```bash
   python lista.py
   python tupla.py
   python dicionario.py
   python conjunto.py
   python pilha.py
   python fila.py
   ```

2. **Modifique e experimente:**
   - Crie suas próprias estruturas
   - Teste as operações
   - Combine estruturas
   - Crie casos de uso práticos

3. **Aprenda os padrões:**
   - Entenda quando usar cada estrutura
   - Otimize para seu caso de uso
   - Considere performance e memória

---

## Dicas e Melhores Práticas

1. **Performance:**
   - Conjuntos são mais rápidos para verificar pertencimento
   - Tuplas são mais rápidas que listas
   - Use `collections.deque` para filas eficientes

2. **Escolha da Estrutura:**
   - Use lista quando precisar de flexibilidade
   - Use tupla para dados imutáveis
   - Use dicionário para pares chave-valor
   - Use conjunto para elementos únicos

3. **Iteração:**
   - Use `for item in estrutura` quando possível
   - Use `enumerate()` quando precisa do índice
   - Use `items()` para dicionários

4. **Compreensão:**
   - São mais rápidas que loops
   - Melhoram a legibilidade
   - Funcionam com listas, conjuntos e dicionários

---

## Próximos Passos

Após dominar estas estruturas:
- Aprenda sobre estruturas mais complexas (heaps, árvores, grafos)
- Estude algoritmos que usam essas estruturas
- Pratique com exercícios de codificação
- Explore otimização de performance

---

## Recursos Adicionais

- [Documentação Python - Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Documentação Python - Collections](https://docs.python.org/3/library/collections.html)
- Livro: "Python Data Structures" - Renan Jolivét

---

**Bom aprendizado!** 🚀
