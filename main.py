# Ozner Leyva Mariscal A01742377
# Carolina González Leal A01284948
# Erick Siller Ojeda A01382929
# Valeria Enríquez Limón A00832782
# Santiago Martínez Vallejo A00571878

import random

def evaluate_clause(clause, assignment):
    for literal in clause:
        if literal > 0 and assignment[abs(literal)] or literal < 0 and not assignment[abs(literal)]:
            return True
    return False

def evaluate_clauses(clauses, assignment):
    for clause in clauses:
        if not evaluate_clause(clause, assignment):
            return False
    return True

def schoenings_algorithm(clauses, num_variables, max_tries=100):
    for _ in range(max_tries):
        assignment = [random.choice([True, False]) for _ in range(num_variables + 1)]

        for _ in range(2 * num_variables**2):
            unsatisfied_clauses = [c for c in clauses if not evaluate_clause(c, assignment)]

            if not unsatisfied_clauses:
                return assignment[:-1]  # Exclude the 0th element for 1-indexed variables

            random_unsatisfied_clause = random.choice(unsatisfied_clauses)
            random_literal = random.choice(random_unsatisfied_clause)
            flip_literal = abs(random_literal)
            assignment[flip_literal] = not assignment[flip_literal]

    return None  # No satisfying assignment found within the given number of tries

def read_clauses_from_file(file_path):
    clauses = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('c') or line.startswith('p'):
                continue
            clause = list(map(int, line.strip().split()[:-1]))
            clauses.append(clause)
    return clauses


# Example usage:
file_path = "04. Instance_3SAT_example.txt"
clauses = read_clauses_from_file(file_path)
n = 20
max_tries = 3*n
result = schoenings_algorithm(clauses, n, max_tries)
if result:
    print("Satisfying assignment found:", result)
else:
    print("No satisfying assignment found within the given number of iterations.")




