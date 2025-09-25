# -------------------------------
# Step 1: Environment Setup
# -------------------------------
import random
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Step 2: Define DSL (Arithmetic Example)
# -------------------------------
operations = ["add", "subtract", "multiply", "divide"]
constants = [1, 2, 3, 4, 5]

# -------------------------------
# Step 3 & 4: Represent Program & Apply Single Operation
# -------------------------------
def apply_operation(op, x):
    name, val = op
    if name == "add":
        return x + val
    elif name == "subtract":
        return x - val
    elif name == "multiply":
        return x * val
    elif name == "divide":
        return x / val if val != 0 else x
    return x

# -------------------------------
# Step 5: Run Entire Program
# -------------------------------
def run_program(program, input_value):
    result = input_value
    for op in program:
        result = apply_operation(op, result)
    return result

# -------------------------------
# Step 6: Generate Random Candidate Programs
# -------------------------------
def generate_random_program(max_length=3):
    length = random.randint(1, max_length)
    program = []
    for _ in range(length):
        op = random.choice(operations)
        val = random.choice(constants)
        program.append((op, val))
    return program

def generate_programs(n=10):
    return [generate_random_program() for _ in range(n)]

# -------------------------------
# Step 7: Create Test Cases
# -------------------------------
test_cases = [
    (2, 10),  # input → expected output
    (3, 15),
    (5, 25)
]

# -------------------------------
# Step 8: Scoring Function
# -------------------------------
def score_program(program, test_cases):
    score = 0
    for inp, expected in test_cases:
        output = run_program(program, inp)
        if output == expected:
            score += 1
    return score / len(test_cases)

# -------------------------------
# Step 9: Evaluate Candidate Programs
# -------------------------------
def evaluate_programs(programs, test_cases):
    results = []
    for prog in programs:
        score = score_program(prog, test_cases)
        results.append({"program": prog, "score": score})
    return results

# Generate 20 candidate programs
candidates = generate_programs(20)
results = evaluate_programs(candidates, test_cases)

# -------------------------------
# Step 10: Print and Visualize Results
# -------------------------------
df = pd.DataFrame(results)
df = df.sort_values(by="score", ascending=False)
print("Top Programs:")
print(df.head())

# Optional: bar chart visualization
plt.figure(figsize=(10,5))
plt.bar(range(len(df)), df['score'])
plt.xlabel("Candidate Programs")
plt.ylabel("Score")
plt.title("Candidate Program Scores")
plt.show()
