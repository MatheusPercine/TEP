def is_divisible_by_60(number):
    digits = list(number)
    
    # Verifica se há pelo menos um '0'
    if '0' not in digits:
        return "cyan"
    
    # Verifica se a soma dos dígitos é divisível por 3
    digit_sum = sum(int(d) for d in digits)
    if digit_sum % 3 != 0:
        return "cyan"
    
    # Verifica se há pelo menos outro dígito par além do '0'
    zero_count = digits.count('0')
    even_count = sum(1 for d in digits if int(d) % 2 == 0)
    
    if even_count > 1:  # Tem pelo menos um zero e um outro número par
        return "red"
    
    return "cyan"

n = int(input())  # Lê o número de entradas
for _ in range(n):
    number = input().strip()  # Lê o número de Alice
    print(is_divisible_by_60(number))
