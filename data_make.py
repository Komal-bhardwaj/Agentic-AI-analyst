import pandas as pd
import random

# Parameters
num_rows = 2000    # number of rows
num_cols = 5       # number of columns

# Generate data
data = {}
for i in range(1, num_cols + 1):
    data[f"Column{i}"] = [random.randint(1, 100) for _ in range(num_rows)]

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("numeric_data_2000rows.csv", index=False)

print("CSV file 'numeric_data_2000rows.csv' with 2000 rows created successfully!")
