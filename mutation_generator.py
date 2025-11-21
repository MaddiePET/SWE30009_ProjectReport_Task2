import os, random, re, ast

MUTATION_OPERATORS = [
    (">", "<"),
    (">", ">="),
    (">", "<="),
    ("True", "False"),
    ("False", "True"),
    ("+ 1", "- 1"),
    ("- 1", "+ 1"),
]

def is_valid_python(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

def generate_mutant(source_code: str, max_attempts: int = 50) -> str:
    for _ in range(max_attempts):
        op, repl = random.choice(MUTATION_OPERATORS)
        mutated = source_code.replace(op, repl, 1)
        if mutated != source_code and is_valid_python(mutated):
            return mutated
    # If no valid mutation found, return original (will be detected as equivalent)
    return source_code


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--count", type=int, default=30)
    args = parser.parse_args()

    with open(args.source, "r") as f:
        original = f.read()

    os.makedirs(args.outdir, exist_ok=True)

    for i in range(1, args.count + 1):
        mutated = generate_mutant(original)
        with open(os.path.join(args.outdir, f"mutant_{i}.py"), "w") as f:
            f.write(mutated)

    print(f"Generated {args.count} mutants in {args.outdir}")

if __name__ == "__main__":
    main()
