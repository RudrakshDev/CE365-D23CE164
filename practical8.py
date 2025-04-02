from collections import defaultdict
import pandas as pd

def compute_parsing_table(grammar, first_sets, follow_sets):
    parsing_table = defaultdict(dict)
    is_ll1 = True
    
    for non_terminal, productions in grammar.items():
        for production in productions:
            first_set = set()
            for symbol in production:
                if symbol in first_sets:
                    first_set |= first_sets[symbol] - {'ε'}
                    if 'ε' not in first_sets[symbol]:
                        break
                else:
                    first_set.add(symbol)
                    break
            else:
                first_set |= follow_sets[non_terminal]
            
            for terminal in first_set:
                if terminal in parsing_table[non_terminal]:
                    is_ll1 = False
                parsing_table[non_terminal][terminal] = production
            
    return parsing_table, is_ll1

def validate_string(parsing_table, start_symbol, input_string):
    stack = ['$']
    stack.append(start_symbol)
    input_string += '$'
    pointer = 0
    
    while stack:
        top = stack.pop()
        if top == input_string[pointer]:
            pointer += 1
        elif top in parsing_table:
            if input_string[pointer] in parsing_table[top]:
                stack.extend(reversed(parsing_table[top][input_string[pointer]]))
            else:
                return "Invalid string"
        else:
            return "Invalid string"
    return "Valid string" if pointer == len(input_string) else "Invalid string"

# Define the grammar
grammar = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

# First and Follow sets (precomputed from previous practical)
first_sets = {
    'S': {'a', 'b', '(', 'c'},
    'A': {'a', 'ε'},
    'B': {'b', 'ε'},
    'C': {'(', 'c'},
    'D': {'a', '(', 'c'}
}

follow_sets = {
    'S': {')', '$'},
    'A': {'b', '(', 'c', ')', '$'},
    'B': {'c', ')', '$'},
    'C': {')', '$'},
    'D': {')', '$'}
}

# Construct parsing table
parsing_table, is_ll1 = compute_parsing_table(grammar, first_sets, follow_sets)

table_df = pd.DataFrame(parsing_table).fillna('-')
print("Predictive Parsing Table:")
print(table_df)
print("\nIs the grammar LL(1)?:", "Yes" if is_ll1 else "No")

# Test cases
test_strings = ["abc", "ac", "(abc)", "c", "(ac)", "a", "()", "(ab)", "abcabc", "b"]
for test_string in test_strings:
    result = validate_string(parsing_table, 'S', test_string)
    print(f"Input: {test_string} -> {result}")
from collections import defaultdict
import pandas as pd

def compute_parsing_table(grammar, first_sets, follow_sets):
    parsing_table = defaultdict(dict)
    is_ll1 = True
    
    for non_terminal, productions in grammar.items():
        for production in productions:
            first_set = set()
            for symbol in production:
                if symbol in first_sets:
                    first_set |= first_sets[symbol] - {'ε'}
                    if 'ε' not in first_sets[symbol]:
                        break
                else:
                    first_set.add(symbol)
                    break
            else:
                first_set |= follow_sets[non_terminal]
            
            for terminal in first_set:
                if terminal in parsing_table[non_terminal]:
                    is_ll1 = False
                parsing_table[non_terminal][terminal] = production
            
    return parsing_table, is_ll1

def validate_string(parsing_table, start_symbol, input_string):
    stack = ['$']
    stack.append(start_symbol)
    input_string += '$'
    pointer = 0
    
    while stack:
        top = stack.pop()
        if top == input_string[pointer]:
            pointer += 1
        elif top in parsing_table:
            if input_string[pointer] in parsing_table[top]:
                stack.extend(reversed(parsing_table[top][input_string[pointer]]))
            else:
                return "Invalid string"
        else:
            return "Invalid string"
    return "Valid string" if pointer == len(input_string) else "Invalid string"

# Define the grammar
grammar = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

# First and Follow sets (precomputed from previous practical)
first_sets = {
    'S': {'a', 'b', '(', 'c'},
    'A': {'a', 'ε'},
    'B': {'b', 'ε'},
    'C': {'(', 'c'},
    'D': {'a', '(', 'c'}
}

follow_sets = {
    'S': {')', '$'},
    'A': {'b', '(', 'c', ')', '$'},
    'B': {'c', ')', '$'},
    'C': {')', '$'},
    'D': {')', '$'}
}

# Construct parsing table
parsing_table, is_ll1 = compute_parsing_table(grammar, first_sets, follow_sets)

table_df = pd.DataFrame(parsing_table).fillna('-')
print("Predictive Parsing Table:")
print(table_df)
print("\nIs the grammar LL(1)?:", "Yes" if is_ll1 else "No")

# Test cases
test_strings = ["abc", "ac", "(abc)", "c", "(ac)", "a", "()", "(ab)", "abcabc", "b"]
for test_string in test_strings:
    result = validate_string(parsing_table, 'S', test_string)
    print(f"Input: {test_string} -> {result}")
