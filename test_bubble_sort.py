import pytest
from bubble_sort import bubble_sort_iterative, bubble_sort_recursive


# ============= METAMORPHIC RELATION 1: REVERSAL RELATION =============
# MR1: If the input list L is reversed to create a follow-up list L',
# the sorted version of both lists must be identical.
# Relation: BubbleSort(Reverse(L)) = BubbleSort(L)

# Test groups for MR1 - designed to expose mutants with comparison operator changes
MR1_TEST_GROUPS = [
    [5, 3, 8, 1, 9, 2],           # MTG1: Unsorted with distinct values
    [4, 2, 4, 2, 4],              # MTG2: Alternating duplicates
    [-3, 5, -1, 8, 0, -2],        # MTG3: Mixed pos/neg requiring many swaps
    [10, 5, 15, 3, 12, 7, 1],     # MTG4: Large range, needs proper comparisons
    [6, 5, 4, 3, 2, 1],           # MTG5: Reverse sorted (worst case)
]

def test_iterative_mr1_basic():
    """MR1: Basic reversal test"""
    arr = MR1_TEST_GROUPS[0]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    # MR1: Reversal relation
    assert result1 == result2
    # Oracle: Result must be sorted
    assert result1 == sorted(arr)


def test_iterative_mr1_all_duplicates():
    """MR1: All duplicates reversal"""
    arr = MR1_TEST_GROUPS[1]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


def test_iterative_mr1_negative():
    """MR1: Negative numbers reversal"""
    arr = MR1_TEST_GROUPS[2]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


def test_iterative_mr1_multiple_duplicates():
    """MR1: Multiple duplicates reversal"""
    arr = MR1_TEST_GROUPS[3]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


def test_iterative_mr1_large():
    """MR1: Large array reversal"""
    arr = MR1_TEST_GROUPS[4]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


# ============= METAMORPHIC RELATION 2: PERMUTATION RELATION =============
# MR2: If the input list L is randomly shuffled (permuted) to create a follow-up list L',
# the sorted output must remain the same.
# Relation: BubbleSort(Permute(L)) = BubbleSort(L)

# Test groups for MR2
import random

MR2_TEST_GROUPS = [
    [9, 3, 7, 1, 5, 2, 8],        # MTG1: Many comparisons needed
    [3, 3, 1, 1, 2, 2],           # MTG2: Duplicate pairs needing stable sort
    [-8, 4, -2, 9, -5, 1],        # MTG3: Mixed signs, many swaps
    [12, 4, 16, 8, 2, 14, 6],     # MTG4: Even numbers, wide range
    [7, 6, 5, 4, 3, 2, 1, 0],     # MTG5: Longer reverse sequence
]

def test_iterative_mr2_basic():
    """MR2: Basic permutation test"""
    arr = MR2_TEST_GROUPS[0]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


def test_iterative_mr2_all_duplicates():
    """MR2: Pairs of duplicates permutation"""
    arr = MR2_TEST_GROUPS[1]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


def test_iterative_mr2_negative():
    """MR2: Symmetric around zero permutation"""
    arr = MR2_TEST_GROUPS[2]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


def test_iterative_mr2_multiple_duplicates():
    """MR2: Large value range permutation"""
    arr = MR2_TEST_GROUPS[3]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


def test_iterative_mr2_large():
    """MR2: Sequential numbers permutation"""
    arr = MR2_TEST_GROUPS[4]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


# ============= RECURSIVE VERSION - MR1: REVERSAL RELATION =============

def test_recursive_mr1_basic():
    """MR1: Basic reversal test"""
    arr = MR1_TEST_GROUPS[0]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


def test_recursive_mr1_all_duplicates():
    """MR1: All duplicates reversal"""
    arr = MR1_TEST_GROUPS[1]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


def test_recursive_mr1_negative():
    """MR1: Negative numbers reversal"""
    arr = MR1_TEST_GROUPS[2]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


def test_recursive_mr1_multiple_duplicates():
    """MR1: Multiple duplicates reversal"""
    arr = MR1_TEST_GROUPS[3]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


def test_recursive_mr1_large():
    """MR1: Large array reversal"""
    arr = MR1_TEST_GROUPS[4]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2
    assert result1 == sorted(arr)


# ============= RECURSIVE VERSION - MR2: PERMUTATION RELATION =============

def test_recursive_mr2_basic():
    """MR2: Basic permutation test"""
    arr = MR2_TEST_GROUPS[0]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


def test_recursive_mr2_all_duplicates():
    """MR2: Pairs of duplicates permutation"""
    arr = MR2_TEST_GROUPS[1]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


def test_recursive_mr2_negative():
    """MR2: Symmetric around zero permutation"""
    arr = MR2_TEST_GROUPS[2]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


def test_recursive_mr2_multiple_duplicates():
    """MR2: Large value range permutation"""
    arr = MR2_TEST_GROUPS[3]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)


def test_recursive_mr2_large():
    """MR2: Sequential numbers permutation"""
    arr = MR2_TEST_GROUPS[4]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2
    assert result1 == sorted(arr)
