def basic_op(operator, value1, value2):
    
    if operator == "+":
        operator = value1 + value2
    elif operator == "-":
        operator = value1 - value2
    elif operator == "*":
        operator= value1 * value2
    elif operator == "/":
        operator = value1 / value2
    
    return operator