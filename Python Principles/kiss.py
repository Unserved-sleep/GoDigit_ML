import pandas as pd

def analyze_sales(data):
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

    monthly_stats = df.groupby('Month')['Sales'].agg(['mean', 'median', 'std', 'min', 'max'])
    monthly_stats['Unique_Customers'] = df.groupby('Month')['Customer'].nunique()

    product_comparison = df.groupby('Product')['Sales'].mean()

    return {
        'Monthly Statistics': monthly_stats.to_dict(),
        'Product Comparison': product_comparison.to_dict()
    }

data = [
    {'Date': '2023-01-01', 'Product': 'Product A', 'Sales': 100, 'Customer': 'C1'},
    {'Date': '2023-01-02', 'Product': 'Product B', 'Sales': 150, 'Customer': 'C2'},
]

report = analyze_sales(data)
print(report)