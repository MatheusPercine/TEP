def calculate_votes(a, b, c):
    lista = [a,b,c]
    maior = max(lista)
    A = max(0, max(b, c) + 1 - a)
    B = max(0, max(a, c) + 1 - b)
    C = max(0, max(a, b) + 1 - c)
    return A, B, C

num_casos = int(input())
results = []

for i in range(num_casos):
    a, b, c = map(int, input().split())
    result = calculate_votes(a, b, c)
    results.append(result)

for result in results:
    print(result[0], result[1], result[2])