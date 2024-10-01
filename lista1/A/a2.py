def calcular_expressao(n):
    # Transformando n em um número inteiro grande mod 4 e mod 2
    a = pow(1,n)
    b = pow(2,n)
    c = pow(3,n)
    d = pow(4,n)

    soma = a+b+c+d
    
    resultado = soma % 5
    print(str(n)+" - "+str(resultado))

# Leitura da entrada
# n = input()


# Saída do resultado
for i in range(100):
    print(calcular_expressao(i))