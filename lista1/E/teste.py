def Verificar(n):
    s = str(n);
    length = len(s)

    pares_possiveis = ['00', '25', '50', '75']

    min_passos = float('inf')

    for par in pares_possiveis:

        j = len(par) - 1
        passos = 0

        for i in range(length-1, -1, -1):

            if s[i] == par[j]:
                j -= 1
            else:
                passos += 1
            
            if j < 0:
                min_passos = min(passos, passos)
                break
            

        return min_passos



n = int(input())
results = []

for i in range(n):
    num = int(input())
    result = Verificar(n)
    results.append(result)

for result in results:
    print(result)