import pandas as pd

# Load the ID–VDS sweep data
df = pd.read_csv("MOSFET_ID_VDS.csv")   # replace with the actual filename

print("Columns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nDescriptive statistics:")
print(df.describe())