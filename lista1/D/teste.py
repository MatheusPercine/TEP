def Calcular(a, b, c):
    lista = [a, b, c]
    maior = max(lista)
    A = max(0, max(b, c) + 1 - a)
    B = max(0, max(a, c) + 1 - b)
    C = max(0, max(a, b) + 1 - c)
    return A, B, C


n = int(input())
resultados = []

for i in range(n):
    a, b, c = map(int, input().split())
    resultado = Calcular(a,b,c)
    resultados.append(resultado)

for resultado in resultados:
    print(resultado[0], resultado[1], resultado[2])