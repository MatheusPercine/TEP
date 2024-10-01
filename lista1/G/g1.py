def max_removed_chars(s):
    n = len(s)
    
    # Prefix sums
    prefix_0 = [0] * (n + 1)
    prefix_1 = [0] * (n + 1)
    
    for i in range(n):
        prefix_0[i + 1] = prefix_0[i] + (1 if s[i] == '0' else 0)
        prefix_1[i + 1] = prefix_1[i] + (1 if s[i] == '1' else 0)
    
    max_removed = 0
    
    # Evaluate all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            count_0 = prefix_0[j] - prefix_0[i]
            count_1 = prefix_1[j] - prefix_1[i]
            
            if count_0 < count_1:
                max_removed = max(max_removed, count_0)
            elif count_1 < count_0:
                max_removed = max(max_removed, count_1)
    
    return max_removed

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