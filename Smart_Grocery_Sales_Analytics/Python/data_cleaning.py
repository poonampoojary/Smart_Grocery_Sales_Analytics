import pandas as pd

# Read grocery Excel dataset
df = pd.read_excel("data/grocery.xlsx")

# Display first five records
print("FIRST FIVE RECORDS:")
print(df.head())

# Display dataset information
print("\nDATASET INFORMATION:")
print(df.info())

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())
# Check revenue calculations

df["Expected_Revenue"] = df["Quantity"] * df["Unit_Price"]

df["Revenue_Check"] = (
    df["Revenue"].round(2) ==
    df["Expected_Revenue"].round(2)
)

print("\nREVENUE VALIDATION:")
print(df[["Product", "Quantity", "Unit_Price",
          "Revenue", "Expected_Revenue", "Revenue_Check"]])

print("\nIncorrect Revenue Records:")
print((~df["Revenue_Check"]).sum())
# DATA CLEANING

# Remove duplicate records
df = df.drop_duplicates()

# Remove rows with missing important values
df = df.dropna(
    subset=["Product", "Category", "Quantity", "Unit_Price", "Revenue"]
)

# Remove extra spaces from text columns
df["Product"] = df["Product"].astype(str).str.strip()
df["Category"] = df["Category"].astype(str).str.strip()

# Save cleaned data
df.to_csv("data/cleaned_grocery_sales.csv", index=False)

print("\nCLEANING COMPLETED!")
print("Total Records:", len(df))
print("Cleaned dataset saved successfully!")