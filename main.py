
def get_operands(stack):
    """ Pop two operands from the stack and return them. """
    return stack.pop(), stack.pop()

def op_plus(stack):
    x, y = get_operands(stack)
    stack.append(x + y)

def op_minus(stack):
    x, y = get_operands(stack)
    stack.append(y - x)

def op_multiply(stack):
    x, y = get_operands(stack)
    stack.append(x * y)

def op_divide(stack):
    x, y = get_operands(stack)
    stack.append(y / x)


def op_power(stack):
    x, y = get_operands(stack)
    stack.append(y ** x)

# A dictionary mapping operator tokens to the evaluation functions


operators = {'+': op_plus,
             '-': op_minus,
             '*': op_multiply,
             '/': op_divide,
             '**': op_power}

# Initialize an empty stack and get the user's RPN expression, split into tokens
stack = []  # input('RPN expression:').strip().split()
tokens = []
while True:
    command = input()
    if command == "=":
        print(stack[0])
    else:
        tokens.append(command)
for token in tokens:
    if token in operators:
        # Operate with the top two numbers on the stack
        operators[token](stack)
    else:
        # We encountered a number: push it onto the top of the stack
        stack.append(float(token))



