def calcular_expressao(n):
    # Transformando n em um número inteiro grande mod 4 e mod 2
    a = pow(1,n)
    b = pow(2,n)
    c = pow(3,n)
    d = pow(4,n)

    soma = a+b+c+d

    return soma

n = input()

soma = calcular_expressao(n)

if soma % 4 == 0:
    print(4)
else:
    print(0)