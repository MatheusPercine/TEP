import sys
import re

# Função para converter a expressão LISP em uma árvore binária
def parse_tree(s_expr):
    # Remove espaços extras e parênteses sem conteúdo
    s_expr = s_expr.replace(' ', '').replace('()', 'None')
    
    # Converter a expressão para uma árvore usando eval (usamos None para os subárvores vazias)
    return eval(s_expr.replace('(', '[').replace(')', ']'))

# Função para realizar uma busca DFS e verificar se há um caminho cuja soma dos nós seja o alvo
def has_path_sum(tree, target_sum):
    if tree is None:
        return False
    
    root_value, left_subtree, right_subtree = tree[0], tree[1], tree[2]
    
    # Se chegarmos em uma folha, verificamos se a soma é igual ao alvo
    if left_subtree is None and right_subtree is None:
        return target_sum == root_value
    
    # Continuamos a busca nas subárvores, diminuindo o valor da soma
    new_sum = target_sum - root_value
    return (has_path_sum(left_subtree, new_sum) if left_subtree else False) or \
           (has_path_sum(right_subtree, new_sum) if right_subtree else False)

# Função principal para processar os casos de teste
def process_input():
    input_data = sys.stdin.read()
    
    # Regex para identificar cada teste no formato <integer> <s-expression>
    test_cases = re.findall(r'(\d+)\s*(\(.*?\))', input_data, re.DOTALL)
    
    for target_sum, tree_str in test_cases:
        target_sum = int(target_sum)
        tree = parse_tree(tree_str)
        
        # Verificar se há um caminho cujo a soma dos nós seja igual ao target_sum
        if has_path_sum(tree, target_sum):
            print("yes")
        else:
            print("no")

# Exemplo de uso com entrada via stdin
if __name__ == "__main__":
    process_input()