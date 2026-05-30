"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    ESTRUTURA DE DADOS: FILA (QUEUE)                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝

PRINCÍPIO: FIFO (First In, First Out)
  → O PRIMEIRO a ENTRAR é o PRIMEIRO a SAIR
  → Como uma fila de banco: você sai na ordem que entrou

OPERAÇÕES PRINCIPAIS:
  - enqueue(): Adiciona um elemento NO FINAL
  - dequeue(): Remove e retorna o elemento DO INÍCIO
  - peek(): Visualiza o elemento DO INÍCIO sem remover
  - is_vazia(): Verifica se está vazia

CARACTERÍSTICAS:
  - Ordenada: Mantém ordem de chegada
  - Mutável: Pode ser modificada
  - Acesso Restrito: Acessa início (dequeue) e fim (enqueue)

CASOS DE USO:
  ✓ Fila de Atendimento (banco, loja, etc)
  ✓ Fila de Impressão - Documentos para imprimir
  ✓ Processamento de Tarefas - Executar por ordem de chegada
  ✓ BFS (Breadth-First Search) - Algoritmo de busca em grafos
  ✓ Simulação de Sistemas - Simulação de eventos
  ✓ Cache LRU (Least Recently Used)
  ✓ Fila de Requisições HTTP

COMPLEXIDADE:
  - enqueue: O(1) - Muito rápido
  - dequeue: O(1) - Muito rápido (com deque)
  - peek: O(1) - Muito rápido

OBSERVAÇÃO IMPORTANTE:
  - Usar list.pop(0) é O(n) - evitar!
  - Usar collections.deque é O(1) - recomendado!
"""

# ─────────────────────────────────────────────────────────────────────────────
# IMPLEMENTAÇÃO: CLASSE FILA
# ─────────────────────────────────────────────────────────────────────────────

class Fila:
    """
    Implementação de uma fila usando lista como estrutura interna.
    
    A fila armazena elementos em uma lista e fornece
    os métodos típicos de fila (enqueue, dequeue, peek, etc).
    
    NOTA: Use collections.deque para melhor performance em produção!
    """
    
    def __init__(self):
        """Inicializa uma fila vazia"""
        self.items = []  # Lista para armazenar os elementos
    
    def enqueue(self, item):
        """
        Adiciona um item NO FINAL da fila.
        
        Args:
            item: Qualquer valor a ser adicionado
        """
        self.items.append(item)  # Adiciona no final (final da fila)
    
    def dequeue(self):
        """
        Remove e retorna o item DO INÍCIO da fila.
        
        Returns:
            O elemento do início, ou None se vazia
            
        Nota: pop(0) é O(n) porque deve reorganizar a lista
        """
        if not self.is_vazia():
            return self.items.pop(0)  # Remove do início
        return None
    
    def peek(self):
        """
        Retorna o item DO INÍCIO SEM REMOVER.
        
        Returns:
            O elemento do início, ou None se vazia
        """
        if not self.is_vazia():
            return self.items[0]  # [0] é o primeiro elemento
        return None
    
    def is_vazia(self):
        """
        Verifica se a fila está vazia.
        
        Returns:
            True se vazia, False caso contrário
        """
        return len(self.items) == 0
    
    def tamanho(self):
        """
        Retorna quantos elementos tem na fila.
        
        Returns:
            Número de elementos
        """
        return len(self.items)
    
    def __str__(self):
        """Representação da fila como string"""
        return str(self.items)

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 1: FILA COM LISTA (SIMPLES)
# ─────────────────────────────────────────────────────────────────────────────

print("=== FILA COM LISTA ===")

fila_lista = []  # Lista vazia funciona como fila

# Adicionar elementos (enqueue)
fila_lista.append("A")
fila_lista.append("B")
fila_lista.append("C")
print(f"Fila: {fila_lista}")
print(f"  → Ordem: A chegou primeiro, C chegou por último")

# Remover elemento (dequeue) - sai o primeiro que entrou
print(f"\nDequeue: {fila_lista.pop(0)}")  # Remove A
print(f"Fila: {fila_lista}")
print(f"  → A foi o primeiro a sair (primeiro a entrar)")

print(f"\nDequeue: {fila_lista.pop(0)}")  # Remove B
print(f"Fila: {fila_lista}")

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 2: FILA COM CLASSE
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== FILA COM CLASSE ===")

fila = Fila()
print(f"Fila vazia?: {fila.is_vazia()}")

# Adicionar elementos
fila.enqueue("Cliente 1")
fila.enqueue("Cliente 2")
fila.enqueue("Cliente 3")
fila.enqueue("Cliente 4")
print(f"\nFila: {fila}")
print(f"Tamanho: {fila.tamanho()}")

# Visualizar primeiro (sem remover)
print(f"\nPrimeiro (peek): {fila.peek()}")
print(f"  → Apenas visualizou, fila não mudou")

# Atender clientes (remover da fila)
print(f"\nAtendendo clientes:")
while not fila.is_vazia():
    print(f"  Atendendo: {fila.dequeue()}")

print(f"\nFila vazia?: {fila.is_vazia()}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 3: CASO PRÁTICO - FILA DE ATENDIMENTO
# ─────────────────────────────────────────────────────────────────────────────

# Simula um sistema de fila de atendimento (banco, farmácia, etc)

class FilaAtendimento:
    """
    Simula um sistema de fila de atendimento com numeração.
    
    Gera números sequenciais para cada cliente e os processa
    em ordem FIFO (primeiro a chegar, primeiro a ser atendido).
    """
    
    def __init__(self):
        """Inicializa a fila e o contador de números"""
        self.fila = Fila()
        self.numero_chamada = 0  # Contador de números
    
    def adicionar_cliente(self, nome):
        """
        Adiciona um cliente à fila.
        
        Args:
            nome: Nome do cliente
        """
        self.numero_chamada += 1  # Incrementa o número
        # Armazena tupla (número, nome)
        self.fila.enqueue((self.numero_chamada, nome))
        print(f"Número {self.numero_chamada}: {nome} adicionado à fila")
    
    def chamar_proximo(self):
        """Chama o próximo cliente para atendimento"""
        if not self.fila.is_vazia():
            numero, nome = self.fila.dequeue()
            print(f"Chamando: Número {numero} - {nome}")
        else:
            print("Fila vazia!")
    
    def proximos(self):
        """Mostra qual é o próximo cliente"""
        if not self.fila.is_vazia():
            print(f"Próximo: {self.fila.peek()[1]}")
        else:
            print("Fila vazia!")

print("\n=== CASO PRÁTICO: FILA DE ATENDIMENTO ===")

atendimento = FilaAtendimento()

print("Adicionando clientes:\n")
atendimento.adicionar_cliente("João")
atendimento.adicionar_cliente("Maria")
atendimento.adicionar_cliente("Pedro")

print("\nAtendendo:\n")
atendimento.proximos()
atendimento.chamar_proximo()
atendimento.chamar_proximo()
atendimento.proximos()


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 4: CASO PRÁTICO - PROCESSAMENTO DE TAREFAS
# ─────────────────────────────────────────────────────────────────────────────

# Sistema que processa tarefas na ordem que chegam

class ProcessadorTarefas:
    """
    Processa tarefas em FIFO.
    
    As tarefas são processadas na ordem em que chegaram.
    Cada tarefa processada é movida para lista de completadas.
    """
    
    def __init__(self):
        """Inicializa o processador"""
        self.tarefas = Fila()      # Fila de tarefas a processar
        self.completadas = []      # Lista de tarefas completadas
    
    def adicionar_tarefa(self, descricao, prioridade=1):
        """
        Adiciona uma nova tarefa à fila.
        
        Args:
            descricao: Descrição da tarefa
            prioridade: Nível de prioridade (não afeta ordem FIFO básica)
        """
        self.tarefas.enqueue({"desc": descricao, "prior": prioridade})
    
    def processar_proxima(self):
        """
        Processa a próxima tarefa da fila.
        
        Remove da fila e adiciona à lista de completadas.
        """
        if not self.tarefas.is_vazia():
            tarefa = self.tarefas.dequeue()
            print(f"Processando: {tarefa['desc']}")
            self.completadas.append(tarefa)
        else:
            print("Sem tarefas para processar!")
    
    def processar_todas(self):
        """Processa todas as tarefas pendentes"""
        while not self.tarefas.is_vazia():
            self.processar_proxima()

print("\n=== CASO PRÁTICO: PROCESSAMENTO DE TAREFAS ===")

processador = ProcessadorTarefas()

print("Adicionando tarefas:\n")
processador.adicionar_tarefa("Ler emails")
processador.adicionar_tarefa("Responder mensagens")
processador.adicionar_tarefa("Fazer backup")

print("\nProcessando tarefas (na ordem adicionada):\n")
processador.processar_todas()


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 5: FILA COM DEQUE - IMPLEMENTAÇÃO EFICIENTE
# ─────────────────────────────────────────────────────────────────────────────

# collections.deque (double-ended queue) é otimizado para operações
# rápidas em ambos os extremos

print("\n=== FILA COM DEQUE (RECOMENDADO) ===")
from collections import deque

fila_deque = deque()

# Adicionar elementos
fila_deque.append(1)
fila_deque.append(2)
fila_deque.append(3)
fila_deque.append(4)
print(f"Fila: {fila_deque}")
print(f"  → Adicionou 1, 2, 3, 4 com append()")

# Remover elementos
print(f"\nRemovendo com popleft():")
print(f"  Dequeue: {fila_deque.popleft()}")  # Remove 1
print(f"  Dequeue: {fila_deque.popleft()}")  # Remove 2
print(f"Fila: {fila_deque}")

print(f"\n✓ deque.popleft() é O(1), muito mais eficiente que list.pop(0)")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 6: CASO PRÁTICO - BFS (BUSCA EM LARGURA) EM GRAFO
# ─────────────────────────────────────────────────────────────────────────────

# BFS (Breadth-First Search) usa fila para explorar um grafo
# Visita todos os nós do nível atual antes de ir para o próximo nível

def bfs_grafo(grafo, inicio):
    """
    Busca em largura em um grafo usando fila.
    
    Visita vértices por nível (distância do início).
    
    Args:
        grafo: Dicionário representando o grafo (chave: vértice, valor: lista de vizinhos)
        inicio: Vértice inicial para começar a busca
    
    Returns:
        Lista de vértices visitados em ordem BFS
    """
    visitados = set()  # Conjunto de vértices já visitados
    fila = deque()     # Fila para controlar ordem de visita
    
    # Começar com vértice inicial
    fila.append(inicio)
    visitados.add(inicio)
    
    print(f"Ordem de visitação começando de '{inicio}':")
    
    # Enquanto houver vértices na fila
    while fila:
        vertice = fila.popleft()  # Remove primeiro (FIFO)
        print(f"  {vertice}")
        
        # Adicionar vizinhos não visitados
        for vizinho in grafo.get(vertice, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

print("\n=== CASO PRÁTICO: BFS EM GRAFO ===")

# Definir um grafo
grafo = {
    'A': ['B', 'C'],         # A conecta a B e C
    'B': ['A', 'D', 'E'],    # B conecta a A, D e E
    'C': ['A', 'F'],         # C conecta a A e F
    'D': ['B'],              # D conecta a B
    'E': ['B', 'F'],         # E conecta a B e F
    'F': ['C', 'E']          # F conecta a C e E
}

print("Grafo:")
for vertice, vizinhos in grafo.items():
    print(f"  {vertice}: {vizinhos}\n")

# Executar BFS
bfs_grafo(grafo, 'A')

print("\n✓ BFS usa fila para explorar por NÍVEIS")
