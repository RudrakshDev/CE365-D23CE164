import re

def generate_quadruples(expression):
    tokens = re.findall(r'\d+|[+\-*/()]', expression)
    op_stack, postfix, temp_vars = [], [], []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    temp_count = 1

    def get_temp():
        nonlocal temp_count
        temp_var = f't{temp_count}'
        temp_count += 1
        return temp_var
    
    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token in precedence:
            while (op_stack and op_stack[-1] in precedence and
                   precedence[op_stack[-1]] >= precedence[token]):
                postfix.append(op_stack.pop())
            op_stack.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while op_stack and op_stack[-1] != '(':
                postfix.append(op_stack.pop())
            op_stack.pop()
    
    while op_stack:
        postfix.append(op_stack.pop())
    
    stack = []
    quadruples = []
    for token in postfix:
        if token.isdigit():
            stack.append(token)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            result = get_temp()
            quadruples.append((token, op1, op2, result))
            stack.append(result)
    
    return quadruples

# Test Cases
test_expressions = [
    "9 + 42 * 8",
    "5 + 6 - 3",
    "7 - ( 8 * 2 )",
    "( 9 - 3 ) + ( 5 * 4 / 2 )",
    "(3 + 5 * 2 - 8) / 4 - 2 + 6",
    "86 / 2 / 3"
]

for expr in test_expressions:
    print(f"\nExpression: {expr}")
    quadruples = generate_quadruples(expr)
    print("Operator  Operand1  Operand2  Result")
    for q in quadruples:
        print(f"{q[0]:<9} {q[1]:<8} {q[2]:<8} {q[3]:<6}")
import re

def generate_quadruples(expression):
    tokens = re.findall(r'\d+|[+\-*/()]', expression)
    op_stack, postfix, temp_vars = [], [], []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    temp_count = 1

    def get_temp():
        nonlocal temp_count
        temp_var = f't{temp_count}'
        temp_count += 1
        return temp_var
    
    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token in precedence:
            while (op_stack and op_stack[-1] in precedence and
                   precedence[op_stack[-1]] >= precedence[token]):
                postfix.append(op_stack.pop())
            op_stack.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while op_stack and op_stack[-1] != '(':
                postfix.append(op_stack.pop())
            op_stack.pop()
    
    while op_stack:
        postfix.append(op_stack.pop())
    
    stack = []
    quadruples = []
    for token in postfix:
        if token.isdigit():
            stack.append(token)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            result = get_temp()
            quadruples.append((token, op1, op2, result))
            stack.append(result)
    
    return quadruples

# Test Cases
test_expressions = [
    "9 + 42 * 8",
    "5 + 6 - 3",
    "7 - ( 8 * 2 )",
    "( 9 - 3 ) + ( 5 * 4 / 2 )",
    "(3 + 5 * 2 - 8) / 4 - 2 + 6",
    "86 / 2 / 3"
]

for expr in test_expressions:
    print(f"\nExpression: {expr}")
    quadruples = generate_quadruples(expr)
    print("Operator  Operand1  Operand2  Result")
    for q in quadruples:
        print(f"{q[0]:<9} {q[1]:<8} {q[2]:<8} {q[3]:<6}")
