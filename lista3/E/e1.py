def find_password(n, message):
    # Dicionário para armazenar as ocorrências das substrings
    substring_count = {}
    
    # Extrair todas as substrings de tamanho n
    for i in range(len(message) - n + 1):
        substring = message[i:i + n]
        if substring in substring_count:
            substring_count[substring] += 1
        else:
            substring_count[substring] = 1

    # Encontrar a substring mais frequente
    password = max(substring_count, key=substring_count.get)
    
    return password

def solve():
    while True:
        try:
            # Ler a entrada (primeiro valor é o tamanho n, o resto é a mensagem)
            line = input().strip()
            n = int(line[0])  # Tamanho da senha
            message = line[1:]  # Mensagem codificada
            
            # Encontrar e imprimir a senha
            print(find_password(n, message))
        except EOFError:
            break  # Fim da entrada

# Exemplo de execução
if __name__ == "__main__":
    solve()
