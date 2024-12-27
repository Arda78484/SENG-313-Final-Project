import random
import time
import math

# Merge Sort Implementation
def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] <= right_half[j][key]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort Implementation
def quick_sort(data, low, high, key):
    if low < high:
        pi = partition(data, low, high, key)
        quick_sort(data, low, pi - 1, key)
        quick_sort(data, pi + 1, high, key)

def partition(data, low, high, key):
    pivot = data[high][key]
    i = low - 1

    for j in range(low, high):
        if data[j][key] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

# Helper function to generate random dataset
# TODO: Real dataset 
def generate_dataset(size):
    return [
        {
            "id": f"P{i}",
            "sales_volume": random.randint(1, 1000),
            "user_rating": round(random.uniform(1, 5), 2),
        }
        for i in range(size)
    ]

# Testing both algorithms
def test_algorithms():
    sizes = [1000, 5000, 10000]
    results = []

    for size in sizes:
        dataset = generate_dataset(size)

        # Merge Sort Timing
        data_copy = dataset.copy()
        start_time = time.time()
        merge_sort(data_copy, "sales_volume")
        merge_sort(data_copy, "user_rating")
        merge_time = time.time() - start_time

        # Quick Sort Timing
        data_copy = dataset.copy()
        start_time = time.time()
        quick_sort(data_copy, 0, len(data_copy) - 1, "sales_volume")
        quick_sort(data_copy, 0, len(data_copy) - 1, "user_rating")
        quick_time = time.time() - start_time

        # Normalized times for complexity comparison
        merge_complexity = size * math.log2(size)
        quick_complexity = size * math.log2(size)

        results.append((size, merge_time, quick_time, merge_complexity, quick_complexity))

    return results

# Run and display results
if __name__ == "__main__":
    results = test_algorithms()
    print("Input Size | Merge Sort Time (s) | Quick Sort Time (s) | Merge Normalized | Quick Normalized")
    for size, merge_time, quick_time, merge_complexity, quick_complexity in results:
        print(f"{size:<10} | {merge_time:<18.6f} | {quick_time:<18.6f} | {merge_complexity:<15.6f} | {quick_complexity:<15.6f}")