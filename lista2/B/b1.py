def is_palindrome(s):
    return s == s[::-1]

def is_mirrored_string(s, mirror_map):
    mirrored_version = ''.join(mirror_map.get(char, '') for char in reversed(s))
    return s == mirrored_version

def classify_string(s, mirror_map):
    palindrome = is_palindrome(s)
    mirrored = is_mirrored_string(s, mirror_map)
    
    if palindrome and mirrored:
        return f"{s} -- is a mirrored palindrome."
    elif palindrome:
        return f"{s} -- is a regular palindrome."
    elif mirrored:
        return f"{s} -- is a mirrored string."
    else:
        return f"{s} -- is not a palindrome."

# Mapeamento de caracteres com seus reversos
mirror_map = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J', 'M': 'M', 'O': 'O', 'S': '2', 
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', 
    '3': 'E', '5': 'Z', '8': '8'
}

# Entrada de exemplo
strings = [
    "NOTAPALINDROME",
    "ISAPALINILAPASI",
    "2A3MEAS",
    "ATOYOTA"
]

# Processar e imprimir os resultados
for s in strings:
    result = classify_string(s, mirror_map)
    print(result)
    print()  # Linha em branco após cada saída
