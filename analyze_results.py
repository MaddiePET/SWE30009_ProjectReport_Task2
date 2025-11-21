import importlib.util
import random

# Test groups
MR1_TEST_GROUPS = [
    [5, 3, 8, 1, 9, 2],           # MTG1
    [4, 2, 4, 2, 4],              # MTG2
    [-3, 5, -1, 8, 0, -2],        # MTG3
    [10, 5, 15, 3, 12, 7, 1],     # MTG4
    [6, 5, 4, 3, 2, 1],           # MTG5
]

MR2_TEST_GROUPS = [
    [9, 3, 7, 1, 5, 2, 8],        # MTG6
    [3, 3, 1, 1, 2, 2],           # MTG7
    [-8, 4, -2, 9, -5, 1],        # MTG8
    [12, 4, 16, 8, 2, 14, 6],     # MTG9
    [7, 6, 5, 4, 3, 2, 1, 0],     # MTG10
]

def load_function(path, func_name):
    try:
        spec = importlib.util.spec_from_file_location("mod", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return getattr(mod, func_name)
    except:
        return None

def apply_sort(fn, arr):
    try:
        return fn(arr.copy())
    except:
        return None

# Analyze each mutant
print("MR | MTG ID | Mutants Killed | Mutants Survived | Total Violations | Total Satisfactions | Ratio")
print("-" * 100)

for mr_idx, (mr_name, test_groups) in enumerate([("MR1", MR1_TEST_GROUPS), ("MR2", MR2_TEST_GROUPS)], 1):
    mr_violations = 0
    mr_satisfactions = 0
    
    for mtg_idx, test_group in enumerate(test_groups, 1):
        killed = []
        survived = []
        
        for mutant_num in range(1, 31):
            mutant_path = f"mutants/mutant_{mutant_num}.py"
            mutant_sort = load_function(mutant_path, "bubble_sort_iterative")
            
            if mutant_sort is None:
                killed.append(mutant_num)
                continue
            
            mtg_killed = False
            
            if mr_name == "MR1":
                # Reversal Relation
                SO = apply_sort(mutant_sort, test_group)
                FO = apply_sort(mutant_sort, test_group[::-1])
                
                # Check MR violation only
                if SO != FO:
                    mtg_killed = True
            else:
                # Permutation Relation
                SO = apply_sort(mutant_sort, test_group)
                random.seed(42 + mutant_num)  # Deterministic shuffle
                permuted = test_group.copy()
                random.shuffle(permuted)
                FO = apply_sort(mutant_sort, permuted)
                
                # Check MR violation only
                if SO != FO:
                    mtg_killed = True
            
            if mtg_killed:
                killed.append(mutant_num)
                mr_violations += 1
            else:
                survived.append(mutant_num)
                mr_satisfactions += 1
        
        actual_mtg_num = mtg_idx if mr_name == "MR1" else mtg_idx + 5
        ratio = mr_violations / (mr_violations + mr_satisfactions) if (mr_violations + mr_satisfactions) > 0 else 0
        
        print(f"{mr_idx}  | MTG{actual_mtg_num}  | {len(killed):14} | {len(survived):16} | {len(killed):16} | {len(survived):19} | ")

    print()
    ratio = mr_violations / (mr_violations + mr_satisfactions) if (mr_violations + mr_satisfactions) > 0 else 0
    print(f"   MR{mr_idx} Total: Violations={mr_violations}, Satisfactions={mr_satisfactions}, Ratio={ratio:.4f}")
    print()
