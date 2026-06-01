import pathlib

def description_for(index: int) -> tuple[str, str, str, str, str]:
    # Define dificuldade e um tema de exercício para cada índice
    if index <= 33:
        nivel = "Fácil"
    elif index <= 66:
        nivel = "Médio"
    else:
        nivel = "Difícil"

    temas = [
        "gestão de estoque com cálculo de médias e limites",
        "processamento de dados de vendas e descontos",
        "análise de notas de alunos com validação de entradas",
        "cadastro de clientes e classificação por faixa etária",
        "relatórios financeiros simples com soma e média",
        "verificação de condições e operadores lógicos em entradas",
        "filtro de transações e cálculo de totais por categoria",
        "simulação de parâmetros e fluxo sequencial de decisões",
        "controle de itens com atualização condicional e laços",
        "normalização de dados e aplicaçãod e regras de negócio",
    ]
    tema = temas[(index - 1) % len(temas)]

    if nivel == "Fácil":
        tarefa = (
            f"Ler entradas simples, aplicar funções de cálculo, usar estruturas sequenciais, condicionais e operadores para resolver um problema de {tema}."
        )
        entrada = "valores numéricos, listas curtas e parâmetros de controle"
        saida = "resultado calculado, mensagem ou relatório breve"
    elif nivel == "Médio":
        tarefa = (
            f"Ler listas ou registros, validar tipos, usar funções auxiliares, estruturas de repetição e condicionais para obter um resultado de {tema}."
        )
        entrada = "listas de dados, estados e parâmetros de configuração"
        saida = "relatório estruturado ou valor agregado"
    else:
        tarefa = (
            f"Implementar um algoritmo completo com funções, tipos definidos, validação rigorosa e controle de fluxo para resolver um desafio complexo de {tema}."
        )
        entrada = "dataset de registros complexos, múltiplas opções e cenários"
        saida = "resultado composto, análise ou resumo detalhado"

    return nivel, tarefa, entrada, saida, tema


def pseudocode_for(index: int, nivel: str, tema: str) -> str:
    return f"""# Pseudocódigo estruturado
# Funções e tipos obrigatórios
# Variáveis com tipos e estruturas de controle:
#   inteiro, real, texto, lógico, lista, registro
#   condicionais (se/então/senão), laços (para/enquanto), operadores aritméticos e lógicos

# Função principal:
# função principal():
#   escreva \"Exercício {index}: {tema}\"
#   leia dados de entrada ({'dados simples' if nivel == 'Fácil' else 'variáveis e coleções'})
#   resultado <- calcular_resultado(dados)
#   escreva resultado
# fim função

# Função auxiliar de processamento:
# função calcular_resultado(entrada: lista): tipo
#   inicializar acumuladores e variáveis de controle
#   para cada item em entrada:
#       se item não for válido então
#           escreva \"Erro: entrada inválida\"
#           retorne valor padrão
#       fim se
#       aplique operadores e regras de negócio usando condiçãoais
#   fim para
#   retorne valor calculado ou registro
# fim função

# Tipos esperados:
#   - inteiro para contadores e opções
#   - real para médias, porcentagens e cálculos
#   - texto para nomes, categorias e mensagens
#   - lógico para validações e flags
#   - lista para coleções de entradas
#   - registro para dados compostos de cada item

# Estrutura sequencial:
#   1. receber entradas
#   2. validar tipos e limites
#   3. processar com funções e laços
#   4. usar condicionais para decisões
#   5. retornar e exibir resultado
"""


def main():
    root = pathlib.Path(__file__).resolve().parents[1]
    exercicios = root / "exercicios"
    for index in range(1, 101):
        nivel, tarefa, entrada, saida, tema = description_for(index)
        filename = exercicios / f"exercicio_{index:03}.py"
        content = [
            f"# Exercício {index}: {tarefa}\n",
            f"# Notação: Pseudocódigo estruturado\n",
            f"# Nível: {nivel}\n",
            f"# Entradas: {entrada}\n",
            f"# Saídas: {saida}\n",
            f"# Tema: {tema}\n",
            "#\n",
            pseudocode_for(index, nivel, tema),
            "\n",
            "from __future__ import annotations\n",
            "from typing import Any, List, Dict\n",
            "\n",
            "def calcular_resultado(entradas: List[Any]) -> Any:\n",
            "    # Implemente esta função usando o pseudocódigo acima.\n",
            "    pass\n",
            "\n",
            "def main() -> None:\n",
            "    # Aqui você deve ler dados, chamar calcular_resultado e exibir resultados.\n",
            f"    print(\"Exercício {index} executado!\")\n",
            "\n",
            "if __name__ == '__main__':\n",
            "    main()\n",
        ]
        filename.write_text(''.join(content), encoding='utf-8')


if __name__ == '__main__':
    main()
