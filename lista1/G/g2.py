def max_removed_chars(s):
    total_0 = s.count('0')
    total_1 = s.count('1')

    if total_0 == total_1:
        return 0
    
    if total_0 > total_1:
        return total_1
    
    if total_0 < total_1:
        return total_0
    
# Read number of test cases
t = int(input())
results = []

# Process each test case
for _ in range(t):
    s = input().strip()
    result = max_removed_chars(s)
    results.append(result)

# Output results for each test case
for result in results:
    print(result)