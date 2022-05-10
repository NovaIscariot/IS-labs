from random import shuffle
from prettytable import PrettyTable


def bubble_sort(arr):
    n = len(arr)
    comp = 0
    moves = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 1
            comp += 1
    return comp, moves


def insertion_sort(arr):
    n = len(arr)
    comp = 0
    moves = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if key >= arr[j]:
                break
            arr[j + 1] = arr[j]
            j -= 1
            moves += 1
        arr[j + 1] = key
    return comp, moves


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    moves = 0
    comp = 0
    for j in range(low, high):
        comp += 1
        if arr[j] <= pivot:
            moves += 1
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    moves += 1

    return i + 1, comp, moves


def quick_sort(arr, low, high):
    comp = 0
    moves = 0
    if len(arr) == 1:
        return arr, 0, 0
    if low < high:
        pi, comp_i, moves_i = partition(arr, low, high)
        comp_l, moves_l = quick_sort(arr, low, pi - 1)
        comp_r, moves_r = quick_sort(arr, pi + 1, high)

        comp = comp_i + comp_l + comp_r
        moves = moves_i + moves_l + moves_r
    return comp, moves


table = PrettyTable()
table.field_names = ["Array", "Bubble sort", "Insert sort", "Quick sort"]


def gen_test_data(min_len, max_len, step):
    tests = []
    for i in range(min_len, max_len, step):
        arr1 = [x for x in range(i)]
        arr2 = arr1[::-1]
        arr3 = arr1[:]
        shuffle(arr3)
        tests.append(arr1)
        tests.append(arr2)
        tests.append(arr3)
    return tests


for test in gen_test_data(5, 21, 5):
    row = [test]
    tmp = test[:]
    row.append(bubble_sort(tmp))
    tmp = test[:]
    row.append(insertion_sort(tmp))
    tmp = test[:]
    row.append(quick_sort(tmp, 0, len(tmp)-1))
    table.add_row(row)

print(table)
