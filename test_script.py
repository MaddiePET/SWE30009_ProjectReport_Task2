import importlib.util, os, csv

import random

# MR1: Reversal Relation
# Description: If the input list L is reversed to create a follow-up list L',
# the sorted version of both lists must be identical.
# Relation: BubbleSort(Reverse(L)) = BubbleSort(L)
def MR1_source(arr): return arr

def MR1_follow_up(arr): return arr[::-1]

# MR2: Permutation Relation
# Description: If the input list L is randomly shuffled (permuted) to create a follow-up list L',
# the sorted output must remain the same.
# Relation: BubbleSort(Permute(L)) = BubbleSort(L)
def MR2_source(arr): return arr

def MR2_follow_up(arr):
    permuted = arr.copy()
    random.shuffle(permuted)
    return permuted

# MR1: Reversal Relation - 5 test groups
# These groups are designed to expose mutants that change comparison operators
MR1_TEST_GROUPS = [
    [5, 3, 8, 1, 9, 2],           # MTG1: Unsorted with distinct values
    [4, 2, 4, 2, 4],              # MTG2: Alternating duplicates
    [-3, 5, -1, 8, 0, -2],        # MTG3: Mixed pos/neg requiring many swaps
    [10, 5, 15, 3, 12, 7, 1],     # MTG4: Large range, needs proper comparisons
    [6, 5, 4, 3, 2, 1],           # MTG5: Reverse sorted (worst case)
]

# MR2: Permutation Relation - 5 test groups
# Different arrays to catch comparison and loop boundary errors
MR2_TEST_GROUPS = [
    [9, 3, 7, 1, 5, 2, 8],        # MTG1: Many comparisons needed
    [3, 3, 1, 1, 2, 2],           # MTG2: Duplicate pairs needing stable sort
    [-8, 4, -2, 9, -5, 1],        # MTG3: Mixed signs, many swaps
    [12, 4, 16, 8, 2, 14, 6],     # MTG4: Even numbers, wide range
    [7, 6, 5, 4, 3, 2, 1, 0],     # MTG5: Longer reverse sequence
]

def load_function(path, func_name):
    try:
        spec = importlib.util.spec_from_file_location("mod", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return getattr(mod, func_name)
    except (SyntaxError, Exception):
        return None


def apply_sort(fn, arr):
    try:
        return fn(arr.copy())
    except Exception:
        return None


def run_tests(source_file, mutant_dir, outdir):
    os.makedirs(outdir, exist_ok=True)

    source_sort = load_function(source_file, "bubble_sort_iterative")

    mutants = sorted([os.path.join(mutant_dir, f) for f in os.listdir(mutant_dir) if f.endswith('.py')])

    so_fo_path = os.path.join(outdir, "so_fo.csv")
    mutant_states_path = os.path.join(outdir, "mutant_states.csv")

    killed = 0
    total = len(mutants)
    mutant_number = 1

    # Collect all results first
    all_results = {}
    
    with open(mutant_states_path, "w", newline="") as ms:
        mut_writer = csv.writer(ms)
        mut_writer.writerow(["Mutant","State"])

        for m in mutants:
            mutant_label = f"M{mutant_number}"
            mutant_number += 1
            
            mutant_sort = load_function(m, "bubble_sort_iterative")
            if mutant_sort is None:
                # Mutant has syntax error - considered killed
                mut_writer.writerow([mutant_label, "K"])
                killed += 1
                continue
            
            mutant_killed = False
            all_results[mutant_label] = {"MR1": {"SO": [], "FO": []}, "MR2": {"SO": [], "FO": []}}

            for MR_name in ["MR1", "MR2"]:
                test_groups = MR1_TEST_GROUPS if MR_name == "MR1" else MR2_TEST_GROUPS
                
                for idx, tg in enumerate(test_groups):
                    if MR_name == "MR1":
                        # Reversal Relation: sort(arr) == sort(reverse(arr))
                        SO = apply_sort(mutant_sort, tg)
                        FO = apply_sort(mutant_sort, tg[::-1])
                        all_results[mutant_label]["MR1"]["SO"].append(SO)
                        all_results[mutant_label]["MR1"]["FO"].append(FO)
                        
                        # Check if MR1 is violated
                        if SO != FO:
                            mutant_killed = True
                        # Also check if output is actually sorted
                        if SO is not None and SO != sorted(tg):
                            mutant_killed = True
                        if FO is not None and FO != sorted(tg[::-1]):
                            mutant_killed = True
                    else:
                        # Permutation Relation: sort(arr) == sort(permute(arr))
                        SO = apply_sort(mutant_sort, tg)
                        permuted = tg.copy()
                        random.shuffle(permuted)
                        FO = apply_sort(mutant_sort, permuted)
                        all_results[mutant_label]["MR2"]["SO"].append(SO)
                        all_results[mutant_label]["MR2"]["FO"].append(FO)
                        
                        # Check if MR2 is violated
                        if SO != FO:
                            mutant_killed = True
                        # Also check if output is actually sorted
                        if SO is not None and SO != sorted(tg):
                            mutant_killed = True
                        if FO is not None and FO != sorted(permuted):
                            mutant_killed = True

            mut_writer.writerow([mutant_label, "K" if mutant_killed else "S"])
            if mutant_killed:
                killed += 1
    
    # Write formatted CSV with separate tables for MR1 and MR2
    with open(so_fo_path, "w", newline="") as sofo:
        writer = csv.writer(sofo)
        
        # MR1 Table
        writer.writerow(["MR1"])
        header = ["ID", "Output"] + [f"MTG{i+1}" for i in range(len(MR1_TEST_GROUPS))]
        writer.writerow(header)
        
        for mutant_label in sorted(all_results.keys(), key=lambda x: int(x[1:])):
            if "MR1" in all_results[mutant_label]:
                writer.writerow([mutant_label, "SO"] + all_results[mutant_label]["MR1"]["SO"])
                writer.writerow(["", "FO"] + all_results[mutant_label]["MR1"]["FO"])
        
        writer.writerow([])  # Empty row separator
        
        # MR2 Table
        writer.writerow(["MR2"])
        header = ["ID", "Output"] + [f"MTG{i+1}" for i in range(len(MR2_TEST_GROUPS))]
        writer.writerow(header)
        
        for mutant_label in sorted(all_results.keys(), key=lambda x: int(x[1:])):
            if "MR2" in all_results[mutant_label]:
                writer.writerow([mutant_label, "SO"] + all_results[mutant_label]["MR2"]["SO"])
                writer.writerow(["", "FO"] + all_results[mutant_label]["MR2"]["FO"])

    with open(os.path.join(outdir, "mutation_score.txt"), "w") as f:
        f.write(f"Killed: {killed}/{total} mutants (Score = {killed/total:.2f})")

if __name__ == "__main__":
    run_tests("bubble_sort.py", "mutants", "results")
    print("Testing complete! Check the 'results' folder for output.")
