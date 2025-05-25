import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------
# Алгоритми сортування
# ---------------------------

# Детермінований QuickSort (опорний елемент — середній)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# ---------------------------
# Вимірювання часу виконання
# ---------------------------

def measure_time(sort_func, arr, runs=5):
    times = []
    for _ in range(runs):
        arr_copy = arr.copy()
        start = time.perf_counter()
        sort_func(arr_copy)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

# ---------------------------
# Тестування
# ---------------------------

sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

for size in sizes:
    print(f"Розмір масиву: {size}")
    test_array = random.sample(range(size * 10), size)

    rand_time = measure_time(randomized_quick_sort, test_array)
    randomized_times.append(rand_time)
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")

    det_time = measure_time(deterministic_quick_sort, test_array)
    deterministic_times.append(det_time)
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

# ---------------------------
# Побудова графіку
# ---------------------------

plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, marker='o', label='Randomized QuickSort')
plt.plot(sizes, deterministic_times, marker='s', label='Deterministic QuickSort')
plt.xlabel('Розмір масиву')
plt.ylabel('Середній час виконання (секунди)')
plt.title('Порівняння Randomized vs Deterministic QuickSort')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------
# Табличний результат
# ---------------------------

df = pd.DataFrame({
    "Array Size": sizes,
    "Randomized QuickSort (s)": randomized_times,
    "Deterministic QuickSort (s)": deterministic_times
})
print("\nРезультати у вигляді таблиці:\n")
print(df)
