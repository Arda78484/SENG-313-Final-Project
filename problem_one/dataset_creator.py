import random
import os
import csv

class DatasetCreator:
    """
    A class to generate and save a dataset of product records.
    """
    @staticmethod
    def generate_dataset(size):
        # Generate a dataset of product records with product IDs, sales volumes, and user ratings.
        # @param size: int - The number of records to generate.
        # @return: list - A list of dictionaries containing the dataset.
        return [
            {
                "id": f"P{i}",
                "sales_volume": random.randint(1, 1000),
                "user_rating": round(random.uniform(1, 5), 2),
            }
            for i in range(size)
        ]

    @staticmethod
    def format_filename(size):
        # Format the filename based on the dataset size.
        # @param size: int - The number of records in the dataset.
        # @return: str - The formatted filename.
        if size >= 1000:
            size_str = f"{size // 1000}k"
        else:
            size_str = f"{size}"
        return f"dataset_{size_str}.csv"

    @staticmethod
    def save_dataset(dataset, size):
        # Save the dataset to the datasets folder as a CSV file.
        # @param dataset: list - The dataset to save.
        # @param size: int - The number of records in the dataset.
        # @return: str - The path to the saved file.
        # Ensure the datasets directory exists
        os.makedirs("datasets", exist_ok=True)

        # Format the filename
        filename = DatasetCreator.format_filename(size)

        # Save the dataset as a CSV file
        filepath = os.path.join("datasets", filename)
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "sales_volume", "user_rating"])
            writer.writeheader()
            writer.writerows(dataset)

        return filepath

if __name__ == "__main__":
    # Set the desired dataset size
    dataset_size = int(input("Enter the number of records to generate: "))

    # Generate the dataset
    dataset = DatasetCreator.generate_dataset(dataset_size)

    # Save the dataset
    file_path = DatasetCreator.save_dataset(dataset, dataset_size)
    print(f"Dataset of size {dataset_size} saved at: {file_path}")