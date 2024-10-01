def is_slump(s, start):
    # Slump starts with 'D' or 'E'
    if s[start] not in 'DE':
        return False, start
    
    # Must be followed by one or more 'F's
    idx = start + 1
    if idx >= len(s) or s[idx] != 'F':
        return False, start

    while idx < len(s) and s[idx] == 'F':
        idx += 1

    # After F's, should be either 'G' or another slump
    if idx < len(s) and s[idx] == 'G':
        return True, idx + 1
    elif idx < len(s):
        return is_slump(s, idx)
    
    return False, start

def is_slimp(s, start):
    if s[start] != 'A':
        return False, start

    idx = start + 1
    if idx >= len(s):
        return False, start

    # Case: two-character Slimp: "AH"
    if s[idx] == 'H':
        return True, idx + 1

    # Case: 'A' followed by 'B', another Slimp, and 'C'
    if s[idx] == 'B':
        slimp_valid, idx = is_slimp(s, idx + 1)
        if slimp_valid and idx < len(s) and s[idx] == 'C':
            return True, idx + 1
        return False, start

    # Case: 'A' followed by a Slump and 'C'
    slump_valid, idx = is_slump(s, idx)
    if slump_valid and idx < len(s) and s[idx] == 'C':
        return True, idx + 1

    return False, start

def is_slurpy(s):
    slimp_valid, idx = is_slimp(s, 0)
    if slimp_valid:
        slump_valid, idx = is_slump(s, idx)
        if slump_valid and idx == len(s):
            return True
    return False

def solve():
    n = int(input().strip())
    print("SLURPYS OUTPUT")
    for _ in range(n):
        s = input().strip()
        if is_slurpy(s):
            print("YES")
        else:
            print("NO")
    print("END OF OUTPUT")

# Exemplo de execução
if __name__ == "__main__":
    solve()
