# -*- coding: cp1251 -*-
import random
import time
import math

def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return steps, True
    return steps, False

def exponential_search(arr, target):
    steps = 0
    if arr[0] == target:
        return 1, True
    index = 1
    while index < len(arr) and arr[index] <= target:
        steps += 1
        index *= 2
    steps_exp, found = binary_search(arr[:min(index, len(arr))], target)
    return steps + steps_exp, found

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0
    while left <= right:
        mid = left + (right - left) // 2
        steps += 1
        if arr[mid] == target:
            return steps, True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return steps, False

def jump_search(arr, target):
    steps = 0
    length = len(arr)
    jump = int(math.sqrt(length))
    prev = 0
    while arr[min(jump, length)-1] < target:
        steps += 1
        prev = jump
        jump += int(math.sqrt(length))
        if prev >= length:
            return steps, False
    while arr[prev] < target:
        steps += 1
        prev += 1
        if prev == min(jump, length):
            return steps, False
    return steps + 1 if prev < length and arr[prev] == target else steps, prev < length and arr[prev] == target

array_size = 1000000
results = []

for i in range(15):
    results.append(f"Итерация номер: {i + 1}")
    arr = sorted(random.sample(range(1, 10000000), array_size))
    target = random.choice(arr)

    for search_algo in [linear_search, exponential_search, jump_search]:
        start_time = time.time()
        try:
            steps, found = search_algo(arr, target)
        except Exception as e:
            steps = str(e)
            found = False
        elapsed_time = time.time() - start_time
        found_str = "Нашел" if found else "Не нашел"
        results.append(f"{search_algo.__name__} - Шаги: {steps}, Время: {elapsed_time:.6f} секунды, {found_str}")

with open("search_results.txt", "w") as file:
    for result in results:
        file.write(result + "\n")
