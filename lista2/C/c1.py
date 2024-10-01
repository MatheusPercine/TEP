def find_relative_ananagrams(words):
    from collections import defaultdict
    
    def normalize(word):
        return ''.join(sorted(word.lower()))
    
    anagram_groups = defaultdict(list)
    
    for word in words:
        norm = normalize(word)
        anagram_groups[norm].append(word)

    result = set()
    for norm, group in anagram_groups.items():
        if len(group) == 1:
            result.add(group[0])
    
    return sorted(result)

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    
    words = []
    for line in input_lines:
        if line.strip() == '#':
            break
        words.extend(line.split())
    
    relative_ananagrams = find_relative_ananagrams(words)
    
    for word in relative_ananagrams:
        print(word)

if __name__ == "__main__":
    main()
