import pytest
from bubble_sort import bubble_sort_iterative, bubble_sort_recursive


# ============= METAMORPHIC RELATION 1: PERMUTATION INVARIANCE =============
# MR1: Reversing the input array should produce the same sorted output

def test_iterative_mr1_basic():
    """MR1: Basic permutation test"""
    arr = [3, 1, 2, 5, 4]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


def test_iterative_mr1_all_duplicates():
    """MR1: All duplicates permutation"""
    arr = [1, 1, 1, 1]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


def test_iterative_mr1_negative():
    """MR1: Negative numbers permutation"""
    arr = [5, -1, 4, -2, 0]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


def test_iterative_mr1_multiple_duplicates():
    """MR1: Multiple duplicates permutation"""
    arr = [2, 2, 1, 3, 3, 1]
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


def test_iterative_mr1_large():
    """MR1: Large array permutation"""
    arr = list(range(20, 0, -1))
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative(arr[::-1])
    assert result1 == result2


# ============= METAMORPHIC RELATION 2: ADDITION RELATION =============
# MR2: Adding a constant to all elements preserves relative order

def test_iterative_mr2_basic():
    """MR2: Basic addition test"""
    arr = [3, 1, 2, 5, 4]
    constant = 10
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


def test_iterative_mr2_all_duplicates():
    """MR2: All duplicates addition"""
    arr = [1, 1, 1, 1]
    constant = 100
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


def test_iterative_mr2_negative():
    """MR2: Negative numbers addition"""
    arr = [5, -1, 4, -2, 0]
    constant = 20
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


def test_iterative_mr2_multiple_duplicates():
    """MR2: Multiple duplicates addition"""
    arr = [2, 2, 1, 3, 3, 1]
    constant = 15
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


def test_iterative_mr2_large():
    """MR2: Large array addition"""
    arr = list(range(20, 0, -1))
    constant = 50
    result1 = bubble_sort_iterative(arr.copy())
    result2 = bubble_sort_iterative([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


# ============= RECURSIVE VERSION - MR1: PERMUTATION INVARIANCE =============

def test_recursive_mr1_basic():
    """MR1: Basic permutation test"""
    arr = [3, 1, 2, 5, 4]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


def test_recursive_mr1_all_duplicates():
    """MR1: All duplicates permutation"""
    arr = [1, 1, 1, 1]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


def test_recursive_mr1_negative():
    """MR1: Negative numbers permutation"""
    arr = [5, -1, 4, -2, 0]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


def test_recursive_mr1_multiple_duplicates():
    """MR1: Multiple duplicates permutation"""
    arr = [2, 2, 1, 3, 3, 1]
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


def test_recursive_mr1_large():
    """MR1: Large array permutation"""
    arr = list(range(20, 0, -1))
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive(arr[::-1])
    assert result1 == result2


# ============= RECURSIVE VERSION - MR2: ADDITION RELATION =============

def test_recursive_mr2_basic():
    """MR2: Basic addition test"""
    arr = [3, 1, 2, 5, 4]
    constant = 10
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


def test_recursive_mr2_all_duplicates():
    """MR2: All duplicates addition"""
    arr = [1, 1, 1, 1]
    constant = 100
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


def test_recursive_mr2_negative():
    """MR2: Negative numbers addition"""
    arr = [5, -1, 4, -2, 0]
    constant = 20
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


def test_recursive_mr2_multiple_duplicates():
    """MR2: Multiple duplicates addition"""
    arr = [2, 2, 1, 3, 3, 1]
    constant = 15
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted


def test_recursive_mr2_large():
    """MR2: Large array addition"""
    arr = list(range(20, 0, -1))
    constant = 50
    result1 = bubble_sort_recursive(arr.copy())
    result2 = bubble_sort_recursive([x + constant for x in arr])
    result2_adjusted = [x - constant for x in result2]
    assert result1 == result2_adjusted
