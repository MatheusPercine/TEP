def min_steps_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # Os pares possíveis que fazem o número ser divisível por 25
    target_pairs = ['00', '25', '50', '75']
    
    min_steps = float('inf')
    
    # Tentar cada par
    for pair in target_pairs:
        j = len(pair) - 1
        steps = 0
        
        # Vamos verificar do final para o começo para encontrar os dois dígitos correspondentes
        for i in range(length - 1, -1, -1):
            if s[i] == pair[j]:
                j -= 1
            else:
                steps += 1
            
            if j < 0:
                min_steps = min(min_steps, steps)
                break
    
    return min_steps

# Ler o número de casos de teste
t = int(input())
results = []

# Processar cada caso de teste
for _ in range(t):
    n = int(input())
    result = min_steps_to_divisible_by_25(n)
    results.append(result)

# Imprimir resultados para cada caso de teste
for result in results:
    print(result)
