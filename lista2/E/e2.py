def find_counterfeit(n, cases):
    for case in cases:
        possible_light = {coin: True for coin in "ABCDEFGHIJKL"}
        possible_heavy = {coin: True for coin in "ABCDEFGHIJKL"}
        
        for weighing in case:
            left, right, result = weighing
            
            if result == "even":
                # Todas as moedas em "left" e "right" são verdadeiras
                for coin in left + right:
                    possible_light[coin] = False
                    possible_heavy[coin] = False
            elif result == "up":
                # Moedas na esquerda são leves e na direita são pesadas
                for coin in left:
                    possible_light[coin] = True
                    possible_heavy[coin] = False
                for coin in right:
                    possible_light[coin] = False
                    possible_heavy[coin] = True
                # As demais moedas são verdadeiras
                for coin in set("ABCDEFGHIJKL") - set(left + right):
                    possible_light[coin] = False
                    possible_heavy[coin] = False
            elif result == "down":
                # Moedas na esquerda são pesadas e na direita são leves
                for coin in left:
                    possible_light[coin] = False
                    possible_heavy[coin] = True
                for coin in right:
                    possible_light[coin] = True
                    possible_heavy[coin] = False
                # As demais moedas são verdadeiras
                for coin in set("ABCDEFGHIJKL") - set(left + right):
                    possible_light[coin] = False
                    possible_heavy[coin] = False
        
        counterfeit = None
        counterfeit_type = None
        for coin in "ABCDEFGHIJKL":
            if possible_light[coin] and not possible_heavy[coin]:
                if counterfeit is not None:
                    counterfeit = None
                    break
                counterfeit = coin
                counterfeit_type = "light"
            elif possible_heavy[coin] and not possible_light[coin]:
                if counterfeit is not None:
                    counterfeit = None
                    break
                counterfeit = coin
                counterfeit_type = "heavy"
        
        if counterfeit:
            print(f"{counterfeit} is the counterfeit coin and it is {counterfeit_type}.")
        else:
            print("No unique counterfeit coin could be determined.")

# Exemplo de uso:
n = int(input())
cases = []
for _ in range(n):
    case = []
    for _ in range(3):
        weighing = input().split()
        case.append((weighing[0], weighing[1], weighing[2]))
    cases.append(case)

find_counterfeit(n, cases)