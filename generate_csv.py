import pandas as pd
import numpy as np
import os


def generate_csv(output_path, feature_headers, label_header, num_samples):
    """
    Generate a CSV file with user-defined headers, ensuring accuracy > 0.5.

    Args:
        output_path (str): Path to save the CSV file
        feature_headers (list): List of feature column names (must be exactly 4)
        label_header (str): Name of the label column
        num_samples (int): Number of samples to generate
    """
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate data dictionary
    data_dict = {}

    # Generate sample data for each feature
    for header in feature_headers:
        if "age" in header.lower():
            data_dict[header] = np.random.randint(25, 60, num_samples)  # Adjusted range for better correlation
        elif "income" in header.lower():
            data_dict[header] = np.random.uniform(50000, 120000, num_samples)
        elif "score" in header.lower() or "rating" in header.lower():
            data_dict[header] = np.random.randint(600, 850, num_samples)
        else:
            data_dict[header] = np.random.uniform(0.5, 1,
                                                  num_samples)  # Adjusted to increase probability of high scores

    # Generate label based on some logic ensuring accuracy > 0.5
    feature_sum = sum(data_dict[header] for header in feature_headers)
    threshold = np.percentile(feature_sum, 40)  # Set threshold slightly lower to ensure more positive labels
    data_dict[label_header] = (feature_sum > threshold).astype(int)

    # Create and save the CSV file
    data = pd.DataFrame(data_dict)
    data.to_csv(output_path, index=False)

    print(f"\n✅ CSV file saved at: {output_path}")
    print(f"✅ Feature headers: {feature_headers}")
    print(f"✅ Label header: {label_header}")
    print(f"✅ Sample data:\n{data.head()}")


if __name__ == "__main__":
    # Interactive user input
    output_path = input(
        "Enter output CSV file path (default: data/sample_data.csv): ").strip() or "data/sample_data.csv"

    while True:
        feature_input = input("Enter exactly four feature column names (comma-separated): ").strip()
        feature_headers = feature_input.split(",")
        if len(feature_headers) == 4:
            break
        print("⚠️ Please enter exactly four feature column names.")

    label_header = input("Enter label column name (default: loan_approval): ").strip() or "loan_approval"

    num_samples = input("Enter number of samples (default: 1000): ").strip()
    num_samples = int(num_samples) if num_samples.isdigit() else 1000

    generate_csv(output_path, feature_headers, label_header, num_samples)
