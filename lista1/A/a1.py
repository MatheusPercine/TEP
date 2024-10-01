def calcular_expressao(n_str):
    # Transformando n em um número inteiro grande mod 4 e mod 2
    n_mod_4 = int(n_str[-2:]) % 4
    n_mod_2 = int(n_str[-1]) % 2
    
    # Se n_mod_4 == 0, usamos o último valor do ciclo de comprimento 4
    if n_mod_4 == 0:
        n_mod_4 = 4
    
    # Valores das potências mod 5
    valores = {
        1: 1,  # 1^n mod 5
        2: [2, 4, 3, 1][n_mod_4 - 1],  # 2^n mod 5
        3: [3, 4, 2, 1][n_mod_4 - 1],  # 3^n mod 5
        4: [4, 1][n_mod_2]  # 4^n mod 5
    }
    
    # Calcula o resultado final
    resultado = (valores[1] + valores[2] + valores[3] + valores[4]) % 5
    
    return resultado

# Leitura da entrada
n = input()

# Saída do resultado
print(calcular_expressao(n))