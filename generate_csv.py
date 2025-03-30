import pandas as pd
import numpy as np
import os

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# Generate 1000 samples with meaningful features
num_samples = 1000

# Meaningful features
age = np.random.randint(18, 70, num_samples)               # Age: 18 to 70
income = np.random.uniform(25000, 100000, num_samples)     # Income: $25,000 to $100,000
credit_score = np.random.randint(300, 850, num_samples)    # Credit Score: 300 to 850

# Labels: 0 or 1 (binary classification)
# Loan approval rule: higher age, income, and credit score → higher chance of approval
labels = ((age > 30) & (income > 50000) & (credit_score > 600)).astype(int)

# Create the DataFrame
data = pd.DataFrame({
    "age": age,
    "income": income,
    "credit_score": credit_score,
    "loan_approval": labels
})

# Save the CSV file in the /data folder
output_path = "data/sample_data.csv"
data.to_csv(output_path, index=False)

print(f"✅ CSV file saved at: {output_path}")
