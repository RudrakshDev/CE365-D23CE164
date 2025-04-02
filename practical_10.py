import re
import operator
import math

# Operator precedence and associativity
OPERATORS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
    '^': (3, math.pow)
}
ASSOCIATIVITY = {
    '^': 'right',  # Right associative
    '*': 'left', '/': 'left', '+': 'left', '-': 'left'  # Left associative
}

def is_number(token):
    return re.match(r'^[0-9]+(\.[0-9]+)?$', token) is not None

def infix_to_postfix(expression):
    output = []
    stack = []
    tokens = re.findall(r'\d+\.?\d*|[()+\-*/^]', expression)
    
    for token in tokens:
        if is_number(token):
            output.append(float(token))
        elif token in OPERATORS:
            while (stack and stack[-1] in OPERATORS and
                   ((ASSOCIATIVITY[token] == 'left' and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]) or
                    (ASSOCIATIVITY[token] == 'right' and OPERATORS[token][0] < OPERATORS[stack[-1]][0]))):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return None  # Mismatched parentheses
    
    while stack:
        if stack[-1] in '()':
            return None  # Mismatched parentheses
        output.append(stack.pop())
    
    return output

def evaluate_postfix(postfix_expr):
    if postfix_expr is None:
        return "Invalid expression"
    
    stack = []
    for token in postfix_expr:
        if isinstance(token, float):
            stack.append(token)
        elif token in OPERATORS:
            if len(stack) < 2:
                return "Invalid expression"
            b = stack.pop()
            a = stack.pop()
            stack.append(OPERATORS[token][1](a, b))
    
    return stack[0] if len(stack) == 1 else "Invalid expression"

def evaluate_expression(expression):
    expression = expression.replace(" ", "")
    postfix_expr = infix_to_postfix(expression)
    return evaluate_postfix(postfix_expr)

# Test cases
test_expressions = [
    "(3 + 5) * 2 ^ 3",
    "3 + 5 * 2",
    "3 + 5 * 2 ^ 2",
    "3 + (5 * 2)",
    "3 + 5 ^ 2 * 2",
    "3 * (5 + 2)",
    "(3 + 5) ^ 2",
    "3 ^ 2 ^ 3",
    "3 ^ 2 + 5 * 2",
    "3 + ^ 5",  # Invalid case
    "(3 + 5 * 2",
    "(3 + 5 * 2 ^ 2 - 8) / 4 ^ 2 + 6"
]

for expr in test_expressions:
    print(f"{expr} = {evaluate_expression(expr)}")
import re
import operator
import math

# Operator precedence and associativity
OPERATORS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
    '^': (3, math.pow)
}
ASSOCIATIVITY = {
    '^': 'right',  # Right associative
    '*': 'left', '/': 'left', '+': 'left', '-': 'left'  # Left associative
}

def is_number(token):
    return re.match(r'^[0-9]+(\.[0-9]+)?$', token) is not None

def infix_to_postfix(expression):
    output = []
    stack = []
    tokens = re.findall(r'\d+\.?\d*|[()+\-*/^]', expression)
    
    for token in tokens:
        if is_number(token):
            output.append(float(token))
        elif token in OPERATORS:
            while (stack and stack[-1] in OPERATORS and
                   ((ASSOCIATIVITY[token] == 'left' and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]) or
                    (ASSOCIATIVITY[token] == 'right' and OPERATORS[token][0] < OPERATORS[stack[-1]][0]))):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return None  # Mismatched parentheses
    
    while stack:
        if stack[-1] in '()':
            return None  # Mismatched parentheses
        output.append(stack.pop())
    
    return output

def evaluate_postfix(postfix_expr):
    if postfix_expr is None:
        return "Invalid expression"
    
    stack = []
    for token in postfix_expr:
        if isinstance(token, float):
            stack.append(token)
        elif token in OPERATORS:
            if len(stack) < 2:
                return "Invalid expression"
            b = stack.pop()
            a = stack.pop()
            stack.append(OPERATORS[token][1](a, b))
    
    return stack[0] if len(stack) == 1 else "Invalid expression"

def evaluate_expression(expression):
    expression = expression.replace(" ", "")
    postfix_expr = infix_to_postfix(expression)
    return evaluate_postfix(postfix_expr)

# Test cases
test_expressions = [
    "(3 + 5) * 2 ^ 3",
    "3 + 5 * 2",
    "3 + 5 * 2 ^ 2",
    "3 + (5 * 2)",
    "3 + 5 ^ 2 * 2",
    "3 * (5 + 2)",
    "(3 + 5) ^ 2",
    "3 ^ 2 ^ 3",
    "3 ^ 2 + 5 * 2",
    "3 + ^ 5",  # Invalid case
    "(3 + 5 * 2",
    "(3 + 5 * 2 ^ 2 - 8) / 4 ^ 2 + 6"
]

for expr in test_expressions:
    print(f"{expr} = {evaluate_expression(expr)}")
