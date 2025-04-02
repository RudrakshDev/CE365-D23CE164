import re
import ast

def evaluate_constant_expression(expr):
    try:
        return str(eval(expr))
    except Exception:
        return expr 

def optimize_expression(expression):
    tokens = re.findall(r'\d+\.?\d*|[a-zA-Z]+|[+\-*/()]', expression)
    
    stack = []
    sub_expr = ""
    
    for token in tokens:
        if re.match(r'\d+\.?\d*', token): 
            sub_expr += token
        elif token in '+-*/':  
            sub_expr += token
        else: 
            if sub_expr:
                stack.append(evaluate_constant_expression(sub_expr))
                sub_expr = ""
            stack.append(token)
    
    if sub_expr:
        stack.append(evaluate_constant_expression(sub_expr))
    
    return " ".join(stack)

# Example usage
expressions = [
    "5 + x - 3 * 2",
    "2 + 3 * 4 - 1",
    "x + (3 * 5) - 2",
    "( 22 / 7 ) * r * r"
]

for expr in expressions:
    print(f"Original: {expr}")
    print(f"Optimized: {optimize_expression(expr)}\n")

print("Hello!")
import re
import ast

def evaluate_constant_expression(expr):
    try:
        return str(eval(expr))
    except Exception:
        return expr 

def optimize_expression(expression):
    tokens = re.findall(r'\d+\.?\d*|[a-zA-Z]+|[+\-*/()]', expression)
    
    stack = []
    sub_expr = ""
    
    for token in tokens:
        if re.match(r'\d+\.?\d*', token): 
            sub_expr += token
        elif token in '+-*/':  
            sub_expr += token
        else: 
            if sub_expr:
                stack.append(evaluate_constant_expression(sub_expr))
                sub_expr = ""
            stack.append(token)
    
    if sub_expr:
        stack.append(evaluate_constant_expression(sub_expr))
    
    return " ".join(stack)

# Example usage
expressions = [
    "5 + x - 3 * 2",
    "2 + 3 * 4 - 1",
    "x + (3 * 5) - 2",
    "( 22 / 7 ) * r * r"
]

for expr in expressions:
    print(f"Original: {expr}")
    print(f"Optimized: {optimize_expression(expr)}\n")
