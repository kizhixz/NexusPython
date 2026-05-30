"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    ESTRUTURA DE DADOS: PILHA (STACK)                         ║
╚═══════════════════════════════════════════════════════════════════════════════╝

PRINCÍPIO: LIFO (Last In, First Out)
  → O ÚLTIMO a ENTRAR é o PRIMEIRO a SAIR
  → Como uma pilha de pratos: você tira o que está no topo

OPERAÇÕES PRINCIPAIS:
  - push(): Adiciona um elemento NO TOPO
  - pop(): Remove e retorna o elemento DO TOPO
  - peek(): Visualiza o elemento DO TOPO sem remover
  - is_vazia(): Verifica se está vazia

CARACTERÍSTICAS:
  - Ordenada: Mantém ordem de inserção
  - Mutável: Pode ser modificada
  - Acesso Restrito: Só acessa pelo topo

CASOS DE USO:
  ✓ Função Desfazer (Undo) - Histórico de ações
  ✓ Verificar Parênteses Balanceados
  ✓ Avaliar Expressões (notação pós-fixa)
  ✓ Algoritmos de Backtracking
  ✓ Navegação do Navegador (voltar/avançar)
  ✓ Gerenciar Chamadas de Função (call stack)

COMPLEXIDADE:
  - push: O(1) - Muito rápido
  - pop: O(1) - Muito rápido
  - peek: O(1) - Muito rápido
"""

# ─────────────────────────────────────────────────────────────────────────────
# IMPLEMENTAÇÃO: CLASSE PILHA
# ─────────────────────────────────────────────────────────────────────────────

class Pilha:
    """
    Implementação de uma pilha usando lista como estrutura interna.
    
    A pilha armazena elementos em uma lista Python e fornece
    os métodos típicos de pilha (push, pop, peek, etc).
    """
    
    def __init__(self):
        """Inicializa uma pilha vazia"""
        self.items = []  # Lista para armazenar os elementos
    
    def push(self, item):
        """
        Adiciona um item NO TOPO da pilha.
        
        Args:
            item: Qualquer valor a ser adicionado
        """
        self.items.append(item)  # append adiciona no final
    
    def pop(self):
        """
        Remove e retorna o item DO TOPO da pilha.
        
        Returns:
            O elemento do topo, ou None se vazia
        """
        if not self.is_vazia():
            return self.items.pop()  # pop() remove do final
        return None
    
    def peek(self):
        """
        Retorna o item DO TOPO SEM REMOVER.
        
        Returns:
            O elemento do topo, ou None se vazia
        """
        if not self.is_vazia():
            return self.items[-1]  # [-1] é o último elemento
        return None
    
    def is_vazia(self):
        """
        Verifica se a pilha está vazia.
        
        Returns:
            True se vazia, False caso contrário
        """
        return len(self.items) == 0
    
    def tamanho(self):
        """
        Retorna quantos elementos tem na pilha.
        
        Returns:
            Número de elementos
        """
        return len(self.items)
    
    def __str__(self):
        """Representação da pilha como string"""
        return str(self.items)

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 1: PILHA COM LISTA (SIMPLES E DIRETO)
# ─────────────────────────────────────────────────────────────────────────────

print("=== PILHA COM LISTA ===")
pilha_lista = []  # Lista vazia funciona como pilha

# Adicionar elementos (push)
pilha_lista.append(1)
pilha_lista.append(2)
pilha_lista.append(3)
print(f"Pilha: {pilha_lista}")
print(f"  → Ordem: 1 foi adicionado primeiro, 3 por último")

# Remover elemento (pop) - sai o último adicionado
print(f"\nPop: {pilha_lista.pop()}")  # Remove 3
print(f"Pilha: {pilha_lista}")
print(f"  → 3 foi o primeiro a sair (último a entrar)")

print(f"\nPop: {pilha_lista.pop()}")  # Remove 2
print(f"Pilha: {pilha_lista}")

# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 2: PILHA COM CLASSE
# ─────────────────────────────────────────────────────────────────────────────

print("\n=== PILHA COM CLASSE ===")

pilha = Pilha()
print(f"Pilha vazia?: {pilha.is_vazia()}")

# Adicionar elementos
pilha.push("Python")
pilha.push("Java")
pilha.push("C++")
print(f"\nPilha após adicionar 3 linguagens: {pilha}")
print(f"Tamanho: {pilha.tamanho()}")

# Visualizar topo sem remover
print(f"\nTopo (peek): {pilha.peek()}")
print(f"  → Apenas visualizou, pilha não mudou")

# Remover elementos
print(f"\nRemovendo elementos:")
while not pilha.is_vazia():
    print(f"  Pop: {pilha.pop()}")

print(f"\nPilha vazia?: {pilha.is_vazia()}")
 


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 3: CASO PRÁTICO - VERIFICAR PARÊNTESES BALANCEADOS
# ─────────────────────────────────────────────────────────────────────────────

# Problema: Verificar se uma expressão tem parênteses, colchetes e chaves
# balanceados corretamente

def verificar_parenteses(expressao):
    """
    Verifica se os parênteses, colchetes e chaves estão balanceados.
    
    Usa pilha para rastrear abertura e verificar fechamento.
    
    Args:
        expressao: String com a expressão a verificar
    
    Returns:
        True se balanceado, False caso contrário
    """
    pilha = Pilha()
    
    # Mapeamento entre abertura e fechamento
    pares = {'(': ')', '[': ']', '{': '}'}
    
    # Percorrer cada caractere
    for char in expressao:
        # Se é abertura, adiciona à pilha
        if char in pares:
            pilha.push(char)
        # Se é fechamento
        elif char in pares.values():
            # Se pilha vazia, sem abertura correspondente
            if pilha.is_vazia():
                return False
            # Verificar se a abertura no topo corresponde ao fechamento
            if pares[pilha.pop()] != char:
                return False
    
    # No final, pilha deve estar vazia
    return pilha.is_vazia()

print("\n=== CASO PRÁTICO: PARÊNTESES BALANCEADOS ===")

testes = [
    "()[]{}",      # Balanceado
    "([{}])",      # Balanceado
    "([)]",        # Desbalanceado - chaves cruzadas
    "{[}]",        # Desbalanceado - ordem errada
    "((()))",      # Balanceado - aninhamento correto
]

print("Verificando expressões:\n")
for teste in testes:
    resultado = verificar_parenteses(teste)
    status = "✓ Balanceado" if resultado else "❌ Desbalanceado"
    print(f"  {teste:12} → {status}")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 4: CASO PRÁTICO - INVERTER UMA STRING
# ─────────────────────────────────────────────────────────────────────────────

# Problema: Inverter uma string usando pilha

def inverter_string(s):
    """
    Inverte uma string usando pilha.
    
    Adiciona cada caractere à pilha, depois remove na ordem inversa.
    
    Args:
        s: String a inverter
    
    Returns:
        String invertida
    """
    pilha = Pilha()
    
    # Adicionar cada caractere (push)
    for char in s:
        pilha.push(char)
    
    # Remover na ordem inversa (pop)
    invertida = ""
    while not pilha.is_vazia():
        invertida += pilha.pop()
    
    return invertida

print("\n=== CASO PRÁTICO: INVERTER STRING ===")

palavras = ["Python", "Estrutura", "Pilha"]
print("Invertendo palavras:\n")

for palavra in palavras:
    invertida = inverter_string(palavra)
    print(f"  {palavra} → {invertida}")
    print(f"    → Push: P, y, t, h, o, n... Pop na ordem inversa")


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 5: CASO PRÁTICO - FUNÇÃO DESFAZER (UNDO)
# ─────────────────────────────────────────────────────────────────────────────

# Problema: Implementar um editor com função de desfazer

class Editor:
    """
    Simula um editor de texto com função de desfazer.
    
    Cada vez que escreve algo novo, o estado anterior é salvo
    em uma pilha, permitindo voltar aos estados anteriores.
    """
    
    def __init__(self):
        """Inicializa o editor vazio"""
        self.historico = Pilha()  # Pilha para armazenar histórico
        self.texto = ""  # Texto atual
    
    def escrever(self, novo_texto):
        """
        Escreve novo texto no editor.
        
        Antes de sobrescrever, salva o estado anterior na pilha.
        
        Args:
            novo_texto: Novo texto a escrever
        """
        # Salvar estado atual antes de mudar
        self.historico.push(self.texto)
        self.texto = novo_texto
        print(f"Escrito: '{self.texto}'")
    
    def desfazer(self):
        """
        Desfaz a última ação.
        
        Volta para o estado anterior armazenado na pilha.
        """
        if not self.historico.is_vazia():
            self.texto = self.historico.pop()
            print(f"Desfeito. Texto: '{self.texto}'")
        else:
            print("Nada para desfazer!")

print("\n=== CASO PRÁTICO: FUNÇÃO DESFAZER ===")

editor = Editor()

# Escrever sequência de textos
print("Escrevendo sequência:\n")
editor.escrever("Olá")
editor.escrever("Olá Mundo")
editor.escrever("Olá Mundo!")

# Desfazer ações
print("\nDesfazendo ações:\n")
editor.desfazer()  # Volta para "Olá Mundo"
editor.desfazer()  # Volta para "Olá"
editor.desfazer()  # Volta para ""


# ─────────────────────────────────────────────────────────────────────────────
# SEÇÃO 6: PILHA COM DEQUE - MAIS EFICIENTE
# ─────────────────────────────────────────────────────────────────────────────

# Módulo collections fornece deque (double-ended queue)
# Mais eficiente para operações em ambas extremidades

print("\n=== PILHA COM DEQUE ===")
from collections import deque

pilha_deque = deque()

# Adicionar elementos
pilha_deque.append(10)
pilha_deque.append(20)
pilha_deque.append(30)
print(f"Pilha: {pilha_deque}")
print(f"  → Adicionou 10, 20, 30 com append()")

# Remover elementos
print(f"\nRemovendo com pop():")
print(f"  Pop: {pilha_deque.pop()}")  # Remove 30
print(f"  Pop: {pilha_deque.pop()}")  # Remove 20
print(f"Pilha: {pilha_deque}")

print(f"\n✓ deque é mais eficiente para operações de pilha")
