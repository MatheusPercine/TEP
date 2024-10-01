def calculate_votes(a, b, c):
    A = max(0, max(b, c) + 1 - a)
    B = max(0, max(a, c) + 1 - b)
    C = max(0, max(a, b) + 1 - c)
    return A, B, C

# Read number of test cases
t = int(input())
results = []

# Process each test case
for _ in range(t):
    a, b, c = map(int, input().split())
    result = calculate_votes(a, b, c)
    results.append(result)

# Output results
for result in results:
    print(result[0], result[1], result[2])
