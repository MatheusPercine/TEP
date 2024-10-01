from collections import deque, defaultdict

def team_queue():
    case_number = 1
    
    while True:
        t = int(input())  # número de times
        if t == 0:
            break
        
        print(f"Scenario #{case_number}")
        case_number += 1
        
        # Dicionário para mapear cada elemento ao seu respectivo time
        team_map = {}
        # Fila principal que mantém a ordem dos times
        main_queue = deque()
        # Dicionário que mantém as filas de cada time
        team_queues = defaultdict(deque)
        # Conjunto para saber quais times já estão na fila principal
        in_queue = set()
        
        # Ler as descrições dos times
        for i in range(t):
            team_data = list(map(int, input().split()))[1:]  # Pular o número de membros do time
            for member in team_data:
                team_map[member] = i  # Mapear o membro ao seu time
        
        while True:
            command = input().strip()
            if command == "STOP":
                break
            elif command.startswith("ENQUEUE"):
                _, member = command.split()
                member = int(member)
                team_id = team_map[member]
                
                # Se o time ainda não está na fila principal, colocamos ele
                if team_id not in in_queue:
                    main_queue.append(team_id)
                    in_queue.add(team_id)
                
                # Adicionar o membro na fila do seu time
                team_queues[team_id].append(member)
            
            elif command == "DEQUEUE":
                # Pegar o time no início da fila principal
                team_id = main_queue[0]
                # Pegar o primeiro membro da fila desse time
                member = team_queues[team_id].popleft()
                print(member)
                
                # Se a fila do time ficar vazia, removemos ele da fila principal
                if not team_queues[team_id]:
                    main_queue.popleft()
                    in_queue.remove(team_id)
        
        print()

# Exemplo de execução
if __name__ == "__main__":
    team_queue()