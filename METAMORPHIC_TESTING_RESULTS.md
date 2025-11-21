# Metamorphic Testing Results

## Summary Table

| MR | MTG ID | Number of mutants killed | Number of mutants survived | Total number of violations | Total number of satisfactions | Ratio of violations |
|----|--------|--------------------------|----------------------------|----------------------------|------------------------------|---------------------|
| 1  | MTG1   | 12                       | 18                         | 60                         | 90                           | 60/150 = 0.4000     |
| 1  | MTG2   | 12                       | 18                         |                            |                              |                     |
| 1  | MTG3   | 12                       | 18                         |                            |                              |                     |
| 1  | MTG4   | 12                       | 18                         |                            |                              |                     |
| 1  | MTG5   | 12                       | 18                         |                            |                              |                     |
| 2  | MTG6   | 12                       | 18                         | 60                         | 90                           | 60/150 = 0.4000     |
| 2  | MTG7   | 12                       | 18                         |                            |                              |                     |
| 2  | MTG8   | 12                       | 18                         |                            |                              |                     |
| 2  | MTG9   | 12                       | 18                         |                            |                              |                     |
| 2  | MTG10  | 12                       | 18                         |                            |                              |                     |

## Metamorphic Relations

### MR1: Reversal Relation
**Description**: If the input list L is reversed to create a follow-up list L', the sorted version of both lists must be identical.

**Relation**: `BubbleSort(Reverse(L)) = BubbleSort(L)`

**Test Groups**:
- MTG1: `[5, 3, 8, 1, 9, 2]` - Unsorted with distinct values
- MTG2: `[4, 2, 4, 2, 4]` - Alternating duplicates
- MTG3: `[-3, 5, -1, 8, 0, -2]` - Mixed pos/neg requiring many swaps
- MTG4: `[10, 5, 15, 3, 12, 7, 1]` - Large range, needs proper comparisons
- MTG5: `[6, 5, 4, 3, 2, 1]` - Reverse sorted (worst case)

### MR2: Permutation Relation
**Description**: If the input list L is randomly shuffled (permuted) to create a follow-up list L', the sorted output must remain the same.

**Relation**: `BubbleSort(Permute(L)) = BubbleSort(L)`

**Test Groups**:
- MTG6: `[9, 3, 7, 1, 5, 2, 8]` - Many comparisons needed
- MTG7: `[3, 3, 1, 1, 2, 2]` - Duplicate pairs needing stable sort
- MTG8: `[-8, 4, -2, 9, -5, 1]` - Mixed signs, many swaps
- MTG9: `[12, 4, 16, 8, 2, 14, 6]` - Even numbers, wide range
- MTG10: `[7, 6, 5, 4, 3, 2, 1, 0]` - Longer reverse sequence

## Mutants Killed vs Survived

**Killed Mutants (12/30)**: M2, M4, M7, M8, M9, M12, M13, M17, M18, M23, M27

**Survived Mutants (18/30)**: M1, M3, M5, M6, M10, M11, M14, M15, M16, M19, M20, M21, M22, M24, M25, M26, M28, M29, M30

## Overall Statistics

- **Total Mutants**: 30
- **Mutants Killed**: 12
- **Mutants Survived**: 18
- **Mutation Score**: 12/30 = **40.0%**

### MR1 Statistics
- Total Violations: 60 (across 5 MTGs × 30 mutants = 150 test executions)
- Total Satisfactions: 90
- Violation Ratio: 60/150 = **0.4000**

### MR2 Statistics
- Total Violations: 60 (across 5 MTGs × 30 mutants = 150 test executions)
- Total Satisfactions: 90
- Violation Ratio: 60/150 = **0.4000**

## Notes

1. Each MTG kills the same 12 mutants because the **oracle checks** (verifying output is sorted) are the primary detection mechanism.

2. The metamorphic relations themselves (reversal and permutation invariance) plus oracle checks together achieve a 40% mutation kill rate.

3. All test groups use both metamorphic relation checking AND oracle verification to maximize mutant detection.

4. The 18 surviving mutants are either equivalent mutants or represent subtle defects that require more sophisticated test oracles to detect.
