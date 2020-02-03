import pytest
from sorting import Sorting

def test_selection_sort(): 
    arr = [64, 34, 25, 12, 22, 22, 11, 90]
    algorithm = ['bubble', 'selection', 'insert', 'merge', 'heap']
    for alg in algorithm:
        sorting = Sorting(arr, alg)        
        sorting.select_sorting()
        assert sorting._arr == [11, 12, 22, 22, 25, 34, 64, 90]
        assert sorting._algorithm == alg
#    assert sorting.select_sorting() == [11, 12, 22, 25, 34, 64, 90]
'''
def test_selection_sort():
    arr = [64, 25, 12, 22, 11]
    assert selection_sort(arr) == [11, 12, 22, 25, 64]

def test_insertion_sort():
    arr = [64, 25, 12, 22, 11]
    assert insertion_sort(arr) == [11, 12, 22, 25, 64]

def test_merge_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert merge_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_heap_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert heap_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_counting_sort():
    arr = 'zxykjhcab'
   # assert counting_sort(arr) == ['a', 'b', 'c', 'h', 'j', 'k', 'x', 'y', 'z']

def test_heap_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert radix_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_bucket_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bucket_sort(arr) == [11, 12, 22, 25, 34, 64, 90]
    '''