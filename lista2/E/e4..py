def find_counterfeit(n, cases):
    for case in cases:
        # Inicialização: Todas as moedas podem ser pesadas ou leves
        possible_light = {coin: True for coin in "ABCDEFGHIJKL"}
        possible_heavy = {coin: True for coin in "ABCDEFGHIJKL"}
        
        # Processar cada pesagem
        for weighing in case:
            left, right, result = weighing
            
            if result == "even":
                # Todas as moedas na pesagem são verdadeiras
                for coin in left + right:
                    possible_light[coin] = False
                    possible_heavy[coin] = False
            elif result == "up":
                # Lado esquerdo está mais pesado
                # Moedas no lado esquerdo podem ser mais pesadas
                # Moedas no lado direito podem ser mais leves
                # Todas as outras moedas não podem ser falsas
                # Primeiro, atualizamos possible_heavy
                for coin in "ABCDEFGHIJKL":
                    if coin not in left:
                        possible_heavy[coin] = False
                # Atualizamos possible_light
                for coin in "ABCDEFGHIJKL":
                    if coin not in right:
                        possible_light[coin] = False
                # Além disso, as moedas no lado esquerdo que não podem ser pesadas
                # e as moedas no lado direito que não podem ser leves
                for coin in left:
                    possible_light[coin] = False
                for coin in right:
                    possible_heavy[coin] = False
            elif result == "down":
                # Lado direito está mais pesado
                # Moedas no lado direito podem ser mais pesadas
                # Moedas no lado esquerdo podem ser mais leves
                # Todas as outras moedas não podem ser falsas
                # Primeiro, atualizamos possible_heavy
                for coin in "ABCDEFGHIJKL":
                    if coin not in right:
                        possible_heavy[coin] = False
                # Atualizamos possible_light
                for coin in "ABCDEFGHIJKL":
                    if coin not in left:
                        possible_light[coin] = False
                # Além disso, as moedas no lado direito que não podem ser pesadas
                # e as moedas no lado esquerdo que não podem ser leves
                for coin in right:
                    possible_light[coin] = False
                for coin in left:
                    possible_heavy[coin] = False
        
        # Identificar a moeda falsa
        counterfeit = None
        status = None
        for coin in "ABCDEFGHIJKL":
            if possible_heavy[coin]:
                counterfeit = coin
                status = "heavy"
                break
            if possible_light[coin]:
                counterfeit = coin
                status = "light"
                break
        
        # Exibir o resultado
        print(f"{counterfeit} is the counterfeit coin and it is {status}.")

# Função principal para ler a entrada e processar os casos
def main():
    n = int(input())
    cases = []
    for _ in range(n):
        case = []
        for _ in range(3):
            weighing = input().split()
            case.append((weighing[0], weighing[1], weighing[2]))
        cases.append(case)
    
    find_counterfeit(n, cases)

# Executar a função principal
if __name__ == "__main__":
    main()
