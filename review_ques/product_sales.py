sales = [
    ("laptop", 50000),
    ("phone", 20000),
    ("laptop", 70000),
    ("tablet", 30000)
]

revenue = {}
for item, price in sales:
    revenue[item] = revenue.get(item, 0) + price

print(revenue)
ma_x = 0
for item, price in revenue.items():
    if price > ma_x:
        ma_x = price
        item_name = item

print(item_name)

sales = list(revenue.items())
for i in range (0, len(sales)-1):
    for j in range (i+1, len(sales)):
        if sales[i][1] < sales[j][1]:
            sales[i],sales[j] = sales[j],sales[i]

print(sales)