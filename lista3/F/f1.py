def find_largest_n(s):
    length = len(s)
    
    # Percorrer todos os divisores do comprimento da string
    for i in range(1, length + 1):
        if length % i == 0:  # Verificar se i é divisor de length
            # Verificar se s é formada pela repetição de s[0:i] por length // i vezes
            if s == s[:i] * (length // i):
                return length // i

def solve():
    while True:
        s = input().strip()
        if s == ".":
            break
        print(find_largest_n(s))

# Exemplo de execução
if __name__ == "__main__":
    solve()
