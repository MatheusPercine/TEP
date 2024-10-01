def max_removed_chars(s):
    n = len(s)
    # Contar totais de 0s e 1s na string
    total_0 = s.count('0')
    total_1 = s.count('1')

    # Inicializar o máximo removido
    max_removed = 0

    # Contadores acumulados
    count_0 = 0
    count_1 = 0
    
    for i in range(n):
        if s[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
        
        # Remover '0's se houver menos '0's do que '1's
        if count_0 < count_1:
            max_removed = max(max_removed, count_0)
        # Remover '1's se houver menos '1's do que '0's
        elif count_1 < count_0:
            max_removed = max(max_removed, count_1)

    return max_removed

# Ler o número de casos de teste
t = int(input())
results = []

# Processar cada caso de teste
for _ in range(t):
    s = input().strip()
    result = max_removed_chars(s)
    results.append(result)

# Imprimir resultados para cada caso de teste
for result in results:
    print(result)
