def find_counterfeit(n, cases):
    for case in cases:
        possible_coins = "ABCDEFGHIJKL"
        possible_light = {coin: True for coin in "ABCDEFGHIJKL"}
        possible_heavy = {coin: True for coin in "ABCDEFGHIJKL"}
        
        for weighing in case:
            left, right, result = weighing
            
            if result == "even":
                possible_coins = ''.join([char for char in possible_coins if char not in left])
                possible_coins = ''.join([char for char in possible_coins if char not in right])
            


n = int(input())
cases = []
for _ in range(n):
    case = []
    for _ in range(3):
        weighing = input().split()
        case.append((weighing[0], weighing[1], weighing[2]))
    cases.append(case)

find_counterfeit(n, cases)
