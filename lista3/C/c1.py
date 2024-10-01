from collections import deque, defaultdict

def topological_sort(n, graph, in_degree):
    # Fila para processar os nós com grau de entrada 0
    queue = deque()
    
    # Adicionar todos os nós com grau de entrada 0 à fila
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    
    while queue:
        # Pegar um nó da fila
        node = queue.popleft()
        result.append(node)
        
        # Para cada vizinho do nó atual
        for neighbor in graph[node]:
            # Reduzir o grau de entrada do vizinho
            in_degree[neighbor] -= 1
            # Se o grau de entrada do vizinho for 0, adicioná-lo à fila
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

def solve():
    while True:
        # Leitura dos valores de n e m
        n, m = map(int, input().split())
        
        if n == 0 and m == 0:
            break
        
        # Grafo e grau de entrada de cada nó
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        
        # Leitura das relações de precedência
        for _ in range(m):
            i, j = map(int, input().split())
            graph[i].append(j)  # Tarefa i deve ser feita antes de tarefa j
            in_degree[j] += 1  # Incrementa o grau de entrada de j
        
        # Realiza a ordenação topológica
        result = topological_sort(n, graph, in_degree)
        
        # Imprime o resultado
        print(" ".join(map(str, result)))

# Exemplo de execução
if __name__ == "__main__":
    solve()
