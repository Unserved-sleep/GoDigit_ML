buyer_name: str = input("Enter buyer name: ")
apple_price: int = int(input("Enter apple price per kg: "))
apple_quantity: int = int(input("Enter apple quantity in kg: "))
orange_price: int = int(input("Enter orange price per kg: "))
orange_quantity: int = int(input("Enter orange quantity in kg: "))
gst_apple: int = 12
gst_orange: int = 5

print(f"Buyer Name: {buyer_name}")
print("-"*85)
print(f"{'Item Code':^10} | {'Price/Unit':^10} | {'# Unit':^10} | {'Price':^10} | {'GST':^10} | {'Total w/ GST':^10}")
print("-"*85)
print(f"{'Apple':^10} | {f'Rs {apple_price}':^10} | {apple_quantity:^10} | {f'Rs {apple_price*apple_quantity}':^10} | {f'Rs {gst_apple}':^10} | {f'Rs {(apple_price*apple_quantity)+(apple_price*apple_quantity)*gst_apple/100}':^10}")
print(f"{'Orange':^10} | {f'Rs {orange_price}':^10} | {orange_quantity:^10} | {f'Rs {orange_price*orange_quantity}':^10} | {f'Rs {gst_orange}':^10} | {f'Rs {(orange_price*orange_quantity)+(orange_price*orange_quantity)*gst_orange/100}':^10}")
print("-"*85)
print(f"Total: {f'Rs {((apple_price*apple_quantity)+(orange_price*orange_quantity)):.2f}':>75}")
print(f"Total Rounded: {f'Rs {(round((apple_price*apple_quantity)+(orange_price*orange_quantity)))}':>67}")


