import importlib.util, os, csv

# MR1: Permutation Invariance
def MR1_source(arr): return arr

def MR1_follow_up(arr): return arr[::-1]

# MR2: Addition Relation
def MR2_source(arr): return arr

def MR2_follow_up(arr, constant=10): return [x + constant for x in arr]

TEST_GROUPS = [
    [3,1,2,5,4],
    [10,9,8,7,6],
    [1,1,1,1],
    [5,-1,4,-2,0],
    list(range(20,0,-1)),
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

            for MR_name, (src, follow) in {
                "MR1": (MR1_source, MR1_follow_up),
                "MR2": (MR2_source, MR2_follow_up)
            }.items():

                for idx, tg in enumerate(TEST_GROUPS):
                    if MR_name == "MR1":
                        # Permutation: sort(arr) == sort(reverse(arr))
                        SO = apply_sort(mutant_sort, src(tg))
                        FO = apply_sort(mutant_sort, follow(tg))
                        all_results[mutant_label]["MR1"]["SO"].append(SO)
                        all_results[mutant_label]["MR1"]["FO"].append(FO)
                        if SO != FO:
                            mutant_killed = True
                    else:
                        # Addition: sort(arr) with constant added should match
                        constant = 10
                        SO = apply_sort(mutant_sort, src(tg))
                        FO = apply_sort(mutant_sort, follow(tg, constant))
                        # Adjust FO by subtracting constant
                        if FO is not None:
                            FO_adjusted = [x - constant for x in FO]
                        else:
                            FO_adjusted = None
                        all_results[mutant_label]["MR2"]["SO"].append(SO)
                        all_results[mutant_label]["MR2"]["FO"].append(FO_adjusted)
                        if SO != FO_adjusted:
                            mutant_killed = True

            mut_writer.writerow([mutant_label, "K" if mutant_killed else "S"])
    
    # Write formatted CSV with separate tables for MR1 and MR2
    with open(so_fo_path, "w", newline="") as sofo:
        writer = csv.writer(sofo)
        
        # MR1 Table
        writer.writerow(["MR1"])
        header = ["ID", "Output"] + [f"MTG{i+1}" for i in range(len(TEST_GROUPS))]
        writer.writerow(header)
        
        for mutant_label in sorted(all_results.keys(), key=lambda x: int(x[1:])):
            if "MR1" in all_results[mutant_label]:
                writer.writerow([mutant_label, "SO"] + all_results[mutant_label]["MR1"]["SO"])
                writer.writerow(["", "FO"] + all_results[mutant_label]["MR1"]["FO"])
        
        writer.writerow([])  # Empty row separator
        
        # MR2 Table
        writer.writerow(["MR2"])
        writer.writerow(header)
        
        for mutant_label in sorted(all_results.keys(), key=lambda x: int(x[1:])):
            if "MR2" in all_results[mutant_label]:
                writer.writerow([mutant_label, "SO"] + all_results[mutant_label]["MR2"]["SO"])
                writer.writerow(["", "FO"] + all_results[mutant_label]["MR2"]["FO"])
            if mutant_killed:
                killed += 1

    with open(os.path.join(outdir, "mutation_score.txt"), "w") as f:
        f.write(f"Killed: {killed}/{total} mutants (Score = {killed/total:.2f})")

if __name__ == "__main__":
    run_tests("bubble_sort.py", "mutants", "results")
    print("Testing complete! Check the 'results' folder for output.")
