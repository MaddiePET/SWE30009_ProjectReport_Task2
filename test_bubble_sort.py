import pytest
from bubble_sort import bubble_sort_iterative, bubble_sort_recursive


# ============= METAMORPHIC RELATION 1: REVERSAL RELATION =============
# MR1: If the input list L is reversed to create a follow-up list L',
# the sorted version of both lists must be identical.
# Relation: BubbleSort(Reverse(L)) = BubbleSort(L)

# Test groups for MR1
MR1_TEST_GROUPS = [
    [3, 1, 2, 5, 4],
    [1, 1, 1, 1],
    [5, -1, 4, -2, 0],
    [2, 2, 1, 3, 3, 1],
    list(range(20, 0, -1)),
]

def test_iterative_mr1_basic():
    """MR1: Basic reversal test"""
    arr = MR1_TEST_GROUPS[0]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


def test_iterative_mr1_all_duplicates():
    """MR1: All duplicates reversal"""
    arr = MR1_TEST_GROUPS[1]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


def test_iterative_mr1_negative():
    """MR1: Negative numbers reversal"""
    arr = MR1_TEST_GROUPS[2]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


def test_iterative_mr1_multiple_duplicates():
    """MR1: Multiple duplicates reversal"""
    arr = MR1_TEST_GROUPS[3]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


def test_iterative_mr1_large():
    """MR1: Large array reversal"""
    arr = MR1_TEST_GROUPS[4]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


# ============= METAMORPHIC RELATION 2: PERMUTATION RELATION =============
# MR2: If the input list L is randomly shuffled (permuted) to create a follow-up list L',
# the sorted output must remain the same.
# Relation: BubbleSort(Permute(L)) = BubbleSort(L)

# Test groups for MR2
import random

MR2_TEST_GROUPS = [
    [7, 2, 9, 1, 5],
    [10, 10, 8, 8, 6],
    [-5, -10, 0, 5, 10],
    [100, 1, 50, 25, 75],
    list(range(1, 16)),
]

def test_iterative_mr2_basic():
    """MR2: Basic permutation test"""
    arr = MR2_TEST_GROUPS[0]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2


def test_iterative_mr2_all_duplicates():
    """MR2: Pairs of duplicates permutation"""
    arr = MR2_TEST_GROUPS[1]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2


def test_iterative_mr2_negative():
    """MR2: Symmetric around zero permutation"""
    arr = MR2_TEST_GROUPS[2]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2


def test_iterative_mr2_multiple_duplicates():
    """MR2: Large value range permutation"""
    arr = MR2_TEST_GROUPS[3]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2


def test_iterative_mr2_large():
    """MR2: Sequential numbers permutation"""
    arr = MR2_TEST_GROUPS[4]
    result1 = bubble_sort_iterative(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_iterative(permuted)
    assert result1 == result2


# ============= RECURSIVE VERSION - MR1: REVERSAL RELATION =============

def test_recursive_mr1_basic():
    """MR1: Basic reversal test"""
    arr = MR1_TEST_GROUPS[0]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


def test_recursive_mr1_all_duplicates():
    """MR1: All duplicates reversal"""
    arr = MR1_TEST_GROUPS[1]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


def test_recursive_mr1_negative():
    """MR1: Negative numbers reversal"""
    arr = MR1_TEST_GROUPS[2]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


def test_recursive_mr1_multiple_duplicates():
    """MR1: Multiple duplicates reversal"""
    arr = MR1_TEST_GROUPS[3]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


def test_recursive_mr1_large():
    """MR1: Large array reversal"""
    arr = MR1_TEST_GROUPS[4]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


# ============= RECURSIVE VERSION - MR2: PERMUTATION RELATION =============

def test_recursive_mr2_basic():
    """MR2: Basic permutation test"""
    arr = MR2_TEST_GROUPS[0]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2


def test_recursive_mr2_all_duplicates():
    """MR2: Pairs of duplicates permutation"""
    arr = MR2_TEST_GROUPS[1]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2


def test_recursive_mr2_negative():
    """MR2: Symmetric around zero permutation"""
    arr = MR2_TEST_GROUPS[2]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2


def test_recursive_mr2_multiple_duplicates():
    """MR2: Large value range permutation"""
    arr = MR2_TEST_GROUPS[3]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2


def test_recursive_mr2_large():
    """MR2: Sequential numbers permutation"""
    arr = MR2_TEST_GROUPS[4]
    result1 = bubble_sort_recursive(arr.copy())
    permuted = arr.copy()
    random.shuffle(permuted)
    result2 = bubble_sort_recursive(permuted)
    assert result1 == result2
