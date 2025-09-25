!pip install numpy pandas
program = [("add", 2), ("multiply", 3), ("subtract, 1"), ("divide, 5")]
def apply_operation(op, x):
    name, val = op
    if name == "add":
        return x + val
    elif name == "multiply":
        return x * val
    elif name == "subtract":
        return x - val
    elif name == "divide":
        return x / val
