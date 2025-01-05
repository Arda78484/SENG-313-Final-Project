import time
import csv
import os
import matplotlib.pyplot as plt

class SortComparison:
    """
    A class to implement and compare Merge Sort and Quick Sort algorithms on product datasets.
    """
    @staticmethod
    def merge_sort(data, key):
        """
        Perform Merge Sort on the dataset based on a specific key.
        
        @param data: list - The dataset to be sorted.
        @param key: str - The key on which to sort the dataset.
        @return: None
        """
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            SortComparison.merge_sort(left_half, key)
            SortComparison.merge_sort(right_half, key)

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

    @staticmethod
    def quick_sort(data, low, high, key):
        """
        Perform Quick Sort on the dataset based on a specific key.
        
        @param data: list - The dataset to be sorted.
        @param low: int - The starting index of the dataset.
        @param high: int - The ending index of the dataset.
        @param key: str - The key on which to sort the dataset.
        @return: None
        """
        if low < high:
            pi = SortComparison.partition(data, low, high, key)
            SortComparison.quick_sort(data, low, pi - 1, key)
            SortComparison.quick_sort(data, pi + 1, high, key)

    @staticmethod
    def partition(data, low, high, key):
        """
        Partition the dataset for Quick Sort.
        
        @param data: list - The dataset to be partitioned.
        @param low: int - The starting index of the dataset.
        @param high: int - The ending index of the dataset.
        @param key: str - The key on which to partition the dataset.
        @return: int - The partition index.
        """
        pivot = data[high][key]
        i = low - 1

        for j in range(low, high):
            if data[j][key] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]

        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    @staticmethod
    def load_dataset(filepath):
        """
        Load dataset from a CSV file.
        
        @param filepath: str - The path to the dataset file.
        @return: list - The loaded dataset.
        """
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            return [
                {
                    "id": row["id"],
                    "sales_volume": int(row["sales_volume"]),
                    "user_rating": float(row["user_rating"]),
                }
                for row in reader
            ]

    @staticmethod
    def sort_and_measure(data, sort_fn, key):
        """
        Measure the execution time of a sorting function.
        
        @param data: list - The dataset to be sorted.
        @param sort_fn: function - The sorting function to be used.
        @param key: str - The key on which to sort the dataset.
        @return: float - The execution time of the sorting function.
        """
        start_time = time.time()
        sort_fn(data, key)
        return time.time() - start_time

if __name__ == "__main__":
    dataset_sizes = ["1k", "5k", "10k"]
    results = []

    for size in dataset_sizes:
        # Load dataset
        filepath = os.path.join("datasets", f"dataset_{size}.csv")
        dataset = SortComparison.load_dataset(filepath)

        # Create copies for sorting
        data_merge = dataset.copy()
        data_quick = dataset.copy()

        # Measure execution time for Merge Sort (sales_volume)
        merge_time_sales = SortComparison.sort_and_measure(
            data_merge, lambda d, k: SortComparison.merge_sort(d, k), "sales_volume"
        )

        # Measure execution time for Quick Sort (sales_volume)
        data_quick = dataset.copy()
        quick_time_sales = SortComparison.sort_and_measure(
            data_quick, lambda d, k: SortComparison.quick_sort(d, 0, len(d) - 1, k), "sales_volume"
        )

        # Measure execution time for Merge Sort (user_rating)
        data_merge = dataset.copy()
        merge_time_rating = SortComparison.sort_and_measure(
            data_merge, lambda d, k: SortComparison.merge_sort(d, k), "user_rating"
        )

        # Measure execution time for Quick Sort (user_rating)
        data_quick = dataset.copy()
        quick_time_rating = SortComparison.sort_and_measure(
            data_quick, lambda d, k: SortComparison.quick_sort(d, 0, len(d) - 1, k), "user_rating"
        )

        results.append(
            {
                "Size": size,
                "Merge Sort Sales (s)": merge_time_sales,
                "Quick Sort Sales (s)": quick_time_sales,
                "Merge Sort Rating (s)": merge_time_rating,
                "Quick Sort Rating (s)": quick_time_rating,
            }
        )

print("\nExecution Time Comparison:")
print("Size\tMerge Sort Sales (s)\tQuick Sort Sales (s)\tMerge Sort Rating (s)\tQuick Sort Rating (s)")
for result in results:
    print(result)

# Extract sizes and timings from results
sizes = [result['Size'] for result in results]
merge_sales = [result['Merge Sort Sales (s)'] for result in results]
quick_sales = [result['Quick Sort Sales (s)'] for result in results]
merge_ratings = [result['Merge Sort Rating (s)'] for result in results]
quick_ratings = [result['Quick Sort Rating (s)'] for result in results]

# Create a figure for the plots
plt.figure(figsize=(12, 8))

# Plot for sales volume sorting
plt.subplot(2, 1, 1)
plt.plot(sizes, merge_sales, label="Merge Sort (Sales)", marker="o")
plt.plot(sizes, quick_sales, label="Quick Sort (Sales)", marker="o")
plt.title("Execution Time for Sorting by Sales Volume")
plt.xlabel("Dataset Size")
plt.ylabel("Time (s)")
plt.legend()

# Plot for user rating sorting
plt.subplot(2, 1, 2)
plt.plot(sizes, merge_ratings, label="Merge Sort (Ratings)", marker="o")
plt.plot(sizes, quick_ratings, label="Quick Sort (Ratings)", marker="o")
plt.title("Execution Time for Sorting by User Ratings")
plt.xlabel("Dataset Size")
plt.ylabel("Time (s)")
plt.legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()