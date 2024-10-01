def is_correct_parentheses(s):
    stack = []
    
    matching_bracket = {')': '(', ']': '['}
    
    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != matching_bracket[char]:
                return "No"
            stack.pop()
    
    return "Yes" if not stack else "No"

def main():
    import sys
    input = sys.stdin.read().strip().split('\n')
    
    n = int(input[0].strip())
    results = []
    
    for i in range(1, n + 1):
        results.append(is_correct_parentheses(input[i].strip()))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()