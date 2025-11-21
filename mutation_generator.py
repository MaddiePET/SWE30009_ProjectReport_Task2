import os, random, re, ast

MUTATION_OPERATORS = [
    # Relational operators
    (r'\s>\s', ' < ', 'relational'),
    (r'\s>\s', ' >= ', 'relational'),
    (r'\s>\s', ' <= ', 'relational'),
    (r'\s>\s', ' == ', 'relational'),
    (r'\s>\s', ' != ', 'relational'),
    # Boolean constants
    (r'\bTrue\b', 'False', 'boolean'),
    (r'\bFalse\b', 'True', 'boolean'),
    # Arithmetic operators
    (r'\s\+\s1\b', ' - 1', 'arithmetic'),
    (r'\s-\s1\b', ' + 1', 'arithmetic'),
    (r'\s\+\s', ' - ', 'arithmetic'),
    # Assignment operators
    (r'(\w+)\s*,\s*(\w+)\s*=\s*(\w+)\s*,\s*(\w+)', r'\1, \2 = \2, \4', 'assignment'),
    # Loop modification
    (r'\bfor\s+(\w+)\s+in\s+reversed\(range\(', r'for \1 in range(', 'loop'),
    (r'\bfor\s+(\w+)\s+in\s+range\((\w+)\s*-\s*1\)', r'for \1 in range(\2)', 'loop'),
    # Break statement removal
    (r'\n\s+break\s*#.*\n', '\n                pass  # mutated: removed break\n', 'control'),
]

def is_valid_python(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

def apply_mutation(source_code: str, operator):
    pattern, replacement, op_type = operator
    mutated = re.sub(pattern, replacement, source_code, count=1)
    return mutated, op_type

def generate_mutant(source_code: str, max_attempts: int = 100) -> tuple:
    """Generate a mutant and return (mutated_code, mutation_description)"""
    for _ in range(max_attempts):
        operator = random.choice(MUTATION_OPERATORS)
        mutated, op_type = apply_mutation(source_code, operator)
        
        if mutated != source_code and is_valid_python(mutated):
            pattern, replacement, _ = operator
            return mutated, f"{op_type}: {pattern} -> {replacement}"
    
    # Fallback: return original with note
    return source_code, "equivalent: no valid mutation found"


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
    
    generated_mutants = set()
    mutation_log = []
    
    # Keep track of mutation operators used
    operator_usage = {}
    
    for i in range(1, args.count + 1):
        mutated, description = generate_mutant(original)
        
        # Try harder to get unique mutants
        attempts = 0
        while mutated in generated_mutants and attempts < 20:
            mutated, description = generate_mutant(original)
            attempts += 1
        
        generated_mutants.add(mutated)
        
        # Track operator usage
        op_type = description.split(':')[0]
        operator_usage[op_type] = operator_usage.get(op_type, 0) + 1
        
        with open(os.path.join(args.outdir, f"mutant_{i}.py"), "w") as f:
            f.write(mutated)
        
        mutation_log.append(f"mutant_{i}.py: {description}")
    
    # Write mutation log
    with open(os.path.join(args.outdir, "mutation_log.txt"), "w") as f:
        f.write(f"Generated {args.count} mutants\n")
        f.write(f"Unique mutants: {len(generated_mutants)}\n\n")
        f.write("Mutation operator distribution:\n")
        for op_type, count in sorted(operator_usage.items()):
            f.write(f"  {op_type}: {count}\n")
        f.write("\nDetailed mutations:\n")
        for log_entry in mutation_log:
            f.write(log_entry + "\n")

    print(f"Generated {args.count} mutants in {args.outdir}")
    print(f"Unique mutants: {len(generated_mutants)}/{args.count}")
    print(f"Operator distribution: {operator_usage}")
    print(f"See {os.path.join(args.outdir, 'mutation_log.txt')} for details")

if __name__ == "__main__":
    main()
