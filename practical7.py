# First and Follow
from collections import defaultdict

def compute_first(grammar):
    first = defaultdict(set)
    nullable = set()
    
    def first_of(symbol):
        if symbol in first:
            return first[symbol]
        if not symbol.isupper():
            return {symbol}
        temp_first = set()
        for rule in grammar[symbol]:
            for sym in rule:
                sym_first = first_of(sym)
                temp_first |= sym_first - {'ε'}
                if 'ε' not in sym_first:
                    break
            else:
                temp_first.add('ε')
                nullable.add(symbol)
        first[symbol] |= temp_first
        return first[symbol]
    
    for non_terminal in grammar:
        first_of(non_terminal)
    
    return first, nullable

def compute_follow(grammar, start_symbol):
    first, nullable = compute_first(grammar)
    follow = defaultdict(set)
    follow[start_symbol].add('$')
    
    changed = True
    while changed:
        changed = False
        for lhs, productions in grammar.items():
            for production in productions:
                trailer = follow[lhs].copy()
                for i in range(len(production) - 1, -1, -1):
                    symbol = production[i]
                    if symbol.isupper():
                        if trailer - follow[symbol]:
                            follow[symbol] |= trailer
                            changed = True
                        trailer = first[symbol] - {'ε'} | trailer if symbol in nullable else first[symbol] - {'ε'}
                    else:
                        trailer = {symbol}
    
    return first, follow

# Define the given grammar
grammar = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

# Compute First and Follow sets
first_sets, follow_sets = compute_follow(grammar, 'S')

# Display results
print("First Sets:")
expected_first = {
    'S': {'a', 'b', '(', 'c'},
    'A': {'a', 'ε'},
    'B': {'b', 'ε'},
    'C': {'(', 'c'},
    'D': {'a', '(', 'c'}
}
for non_terminal in ['S', 'A', 'B', 'C', 'D']:
    print(f"First({non_terminal}) = {first_sets[non_terminal]}")

print("\nFollow Sets:")
expected_follow = {
    'S': {')', '$'},
    'A': {'b', '(', 'c', ')', '$'},
    'B': {'c', ')', '$'},
    'C': {')', '$'},
    'D': {')', '$'}
}
for non_terminal in ['S', 'A', 'B', 'C', 'D']:
    print(f"Follow({non_terminal}) = {follow_sets[non_terminal]}")
