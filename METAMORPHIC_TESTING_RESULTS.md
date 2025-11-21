# Metamorphic Testing Results (Pure MR - No Oracle Checks)

## Summary Table

| MR | MTG ID | Number of mutants killed | Number of mutants survived | Total number of violations | Total number of satisfactions | Ratio of violations |
|----|--------|--------------------------|----------------------------|----------------------------|------------------------------|---------------------|
| 1  | MTG1   | 6                        | 24                         | 24                         | 126                          | 24/150 = 0.1600     |
| 1  | MTG2   | 0                        | 30                         |                            |                              |                     |
| 1  | MTG3   | 6                        | 24                         |                            |                              |                     |
| 1  | MTG4   | 6                        | 24                         |                            |                              |                     |
| 1  | MTG5   | 6                        | 24                         |                            |                              |                     |
| 2  | MTG6   | 6                        | 24                         | 30                         | 120                          | 30/150 = 0.2000     |
| 2  | MTG7   | 6                        | 24                         |                            |                              |                     |
| 2  | MTG8   | 6                        | 24                         |                            |                              |                     |
| 2  | MTG9   | 6                        | 24                         |                            |                              |                     |
| 2  | MTG10  | 6                        | 24                         |                            |                              |                     |

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

**Killed Mutants (6/30)**: M2, M4, M8, M9, M12, M13

**Survived Mutants (24/30)**: M1, M3, M5, M6, M7, M10, M11, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24, M25, M26, M27, M28, M29, M30

## Overall Statistics

- **Total Mutants**: 30
- **Mutants Killed**: 6
- **Mutants Survived**: 24
- **Mutation Score**: 6/30 = **20.0%**

### MR1 Statistics
- Total Violations: 24 (across 5 MTGs × 30 mutants = 150 test executions)
- Total Satisfactions: 126
- Violation Ratio: 24/150 = **0.1600**

### MR2 Statistics
- Total Violations: 30 (across 5 MTGs × 30 mutants = 150 test executions)
- Total Satisfactions: 120
- Violation Ratio: 30/150 = **0.2000**

## Notes

1. **Pure Metamorphic Testing**: Uses ONLY metamorphic relations (no oracle checks that verify output is sorted).

2. **MTG2 (All duplicates `[4,2,4,2,4]`)**: Kills 0 mutants because with all duplicates, even incorrect sorting can produce outputs that satisfy the reversal relation.

3. **Limited Detection**: The 20% mutation score reflects the inherent limitation of these particular metamorphic relations - they detect violations of sorting order invariants but miss many faulty implementations.

4. **MR2 More Effective**: Permutation relation (20% violation ratio) is slightly more effective than reversal relation (16% violation ratio) at detecting mutants.

5. **Equivalent Mutants**: Many surviving mutants likely produce consistently wrong outputs that still satisfy both metamorphic relations.
