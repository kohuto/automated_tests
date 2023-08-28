from heap_sort import heapSort

def test_heap_sort():
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    assert arr == [5, 6, 7, 11, 12, 13], "Test heap_sort selhal: Neočekávaný výstup."

def test_empty_list():
    arr = []
    heapSort(arr)
    assert arr == [], "Test empty_list selhal: Neočekáváno změny v prázdném seznamu."

def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    heapSort(arr)
    assert arr == [1, 2, 4, 5], "Test sorted_list selhal: Neočekávaný výstup pro seřazený seznam."

def test_reverse_list():
    arr = [5, 4, 3, 2, 1]
    heapSort(arr)
    assert arr == [1, 2, 3, 4, 5], "Test reverse_list selhal: Neočekávaný výstup pro obrácený seznam."
