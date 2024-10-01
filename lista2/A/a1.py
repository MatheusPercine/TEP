import heapq

def correct_log(n, operations):
    heap = []
    output = []
    
    for operation in operations:
        if operation.startswith("insert"):
            _, x = operation.split()
            x = int(x)
            heapq.heappush(heap, x)
            output.append(operation)
        
        elif operation.startswith("getMin"):
            _, x = operation.split()
            x = int(x)
            
            # Ensure heap is not empty and minimum element is x
            while heap and heap[0] < x:
                output.append("removeMin")
                heapq.heappop(heap)
            
            if not heap or heap[0] > x:
                heapq.heappush(heap, x)
                output.append(f"insert {x}")
            
            output.append(operation)
        
        elif operation == "removeMin":
            if not heap:
                # If heap is empty, insert a dummy element (e.g., 1)
                output.append("insert 1")
                heapq.heappush(heap, 1)
            
            heapq.heappop(heap)
            output.append(operation)
    
    # Output the total number of operations and the corrected operations
    print(len(output))
    for op in output:
        print(op)

# Example usage:
n = int(input())
operations = [input().strip() for _ in range(n)]
correct_log(n, operations)
