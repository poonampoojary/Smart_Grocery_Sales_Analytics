import pandas as pd
import sqlite3

# Read cleaned grocery data
df = pd.read_csv("data/cleaned_grocery_sales.csv")

# Connect to SQLite database
connection = sqlite3.connect("database/grocery.db")

# Store data in SQL table
df.to_sql(
    "Sales",
    connection,
    if_exists="replace",
    index=False
)

# Check inserted records
result = pd.read_sql_query(
    "SELECT * FROM Sales LIMIT 5",
    connection
)

print("DATA SUCCESSFULLY STORED IN SQL!")
print(result)

# Count total records
count = pd.read_sql_query(
    "SELECT COUNT(*) AS Total_Records FROM Sales",
    connection
)

print("\nTOTAL RECORDS:")
print(count)
# SQL BUSINESS ANALYSIS

# 1. Total Revenue
revenue = pd.read_sql_query(
    "SELECT SUM(Revenue) AS Total_Revenue FROM Sales",
    connection
)
print("\nTOTAL REVENUE:")
print(revenue)

# 2. Category-wise Revenue
category = pd.read_sql_query(
    """
    SELECT Category, SUM(Revenue) AS Total_Revenue
    FROM Sales
    GROUP BY Category
    ORDER BY Total_Revenue DESC
    """,
    connection
)
print("\nCATEGORY-WISE REVENUE:")
print(category)

# 3. Top 5 Products
top_products = pd.read_sql_query(
    """
    SELECT Product, SUM(Revenue) AS Revenue
    FROM Sales
    GROUP BY Product
    ORDER BY Revenue DESC
    LIMIT 5
    """,
    connection
)
print("\nTOP 5 PRODUCTS:")
print(top_products)
# Revenue by Category
category_revenue = pd.read_sql_query(
    """
    SELECT Category, SUM(Revenue) AS Total_Revenue
    FROM Sales
    GROUP BY Category
    ORDER BY Total_Revenue DESC
    """,
    connection
)

print("\nREVENUE BY CATEGORY:")
print(category_revenue)
# Average Revenue by Category
avg_revenue = pd.read_sql_query(
    """
    SELECT Category, AVG(Revenue) AS Average_Revenue
    FROM Sales
    GROUP BY Category
    ORDER BY Average_Revenue DESC
    """,
    connection
)

print("\nAVERAGE REVENUE BY CATEGORY:")
print(avg_revenue)
# Total Quantity by Category
quantity_category = pd.read_sql_query(
    """
    SELECT Category, SUM(Quantity) AS Total_Quantity
    FROM Sales
    GROUP BY Category
    ORDER BY Total_Quantity DESC
    """,
    connection
)

print("\nTOTAL QUANTITY BY CATEGORY:")
print(quantity_category)
# SQL BUSINESS ANALYSIS

# 1. Total Revenue
revenue = pd.read_sql_query(
    "SELECT SUM(Revenue) AS Total_Revenue FROM Sales",
    connection
)
print("\nTOTAL REVENUE:")
print(revenue)

# 2. Category-wise Revenue
category = pd.read_sql_query(
    """
    SELECT Category, SUM(Revenue) AS Total_Revenue
    FROM Sales
    GROUP BY Category
    ORDER BY Total_Revenue DESC
    """,
    connection
)
print("\nCATEGORY-WISE REVENUE:")
print(category)

# 3. Top 5 Products
top_products = pd.read_sql_query(
    """
    SELECT Product, SUM(Revenue) AS Revenue
    FROM Sales
    GROUP BY Product
    ORDER BY Revenue DESC
    LIMIT 5
    """,
    connection
)
print("\nTOP 5 PRODUCTS:")
print(top_products)
# Monthly Revenue Analysis
monthly_revenue = pd.read_sql_query(
    """
    SELECT
        strftime('%Y-%m', Date) AS Month,
        SUM(Revenue) AS Total_Revenue
    FROM Sales
    GROUP BY Month
    ORDER BY Month
    """,
    connection
)

print("\nMONTHLY REVENUE:")
print(monthly_revenue)
# Revenue by Product
product_revenue = pd.read_sql_query(
    """
    SELECT
        Product,
        SUM(Revenue) AS Total_Revenue
    FROM Sales
    GROUP BY Product
    ORDER BY Total_Revenue DESC
    """,
    connection
)

print("\nREVENUE BY PRODUCT:")
print(product_revenue)
# Export SQL data for Power BI
sales_data = pd.read_sql_query(
    "SELECT * FROM Sales",
    connection
)

sales_data.to_csv(
    "data/sales_from_sqlite.csv",
    index=False
)

print("DATA EXPORTED SUCCESSFULLY FOR POWER BI!")
connection.close()