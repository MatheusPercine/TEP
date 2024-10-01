def max_mice_saved(n, mice_positions):
    mice_positions.sort(reverse=True)  # Ordenar em ordem decrescente
    saved_mice = 0
    cat_position = 0
    
    for mouse in mice_positions:
        # Se o rato mais próximo do buraco ainda pode ser salvo:
        if mouse > cat_position:
            saved_mice += 1
            cat_position += (n - mouse)
        else:
            break  # Pare se o próximo rato não puder mais ser salvo
    
    return saved_mice

# Ler número de casos de teste
t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    mice_positions = list(map(int, input().split()))
    result = max_mice_saved(n, mice_positions)
    results.append(result)

# Imprimir os resultados
for result in results:
    print(result)