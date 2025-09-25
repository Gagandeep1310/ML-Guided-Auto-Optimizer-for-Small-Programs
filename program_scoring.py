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
def run_program(program, input_value):
    result = input_value
    for op in program:
        result = apply_operation(op, result)
    return result
test_cases = [(2, 10), (3, 15)]  # input → expected output
def score_program(program, test_cases):
    score = 0
    for inp, expected in test_cases:
        output = run_program(program, inp)
        if output == expected:
            score += 1
    return score / len(test_cases)
