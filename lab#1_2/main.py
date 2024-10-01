import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        steps = len(arr) - 1
        sorted_left, left_steps = quick_sort(left)
        sorted_right, right_steps = quick_sort(right)
        return sorted_left + middle + sorted_right, steps + left_steps + right_steps

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    steps = 0

    if left < n and arr[left] > arr[largest]:
        largest = left
        steps += 1
    if right < n and arr[right] > arr[largest]:
        largest = right
        steps += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps += 1 + heapify(arr, n, largest)  # один шаг за обмен и рекурсивно считаем шаги
    return steps

def heap_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n // 2 - 1, -1, -1):
        steps += heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps += 1 + heapify(arr, i, 0)
    return arr, steps

def shell_sort(arr):
    n = len(arr)
    steps = 0
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                steps += 1
            arr[j] = temp
        gap //= 2
    return arr, steps


with open("sort_results.txt", "w") as f:
    for run in range(15):
        f.write(f"Запуск номер: {run + 1}\n")
        array = [random.randint(1, 100000) for _ in range(10000)]

        for sort_function in [quick_sort, heap_sort, shell_sort]:
            copy_array = array.copy()

            start_time = time.time()
            sorted_array, total_steps = sort_function(copy_array)
            end_time = time.time()

            execution_time = end_time - start_time

            f.write(f"Сортировка: {sort_function.__name__}\n")
            f.write(f"Время выполнения: {execution_time:.6f} секунд\n")
            f.write(f"Количество шагов: {total_steps}\n")
            f.write("\n")
