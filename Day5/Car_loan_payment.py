def car_loan(p, y, r):
    interest = p * y * r / 100
    payment = p + interest
    monthly_payment = payment / 12
    return monthly_payment

principal = float(input("Principal amount: "))
years = int(input("Years: "))
rate = float(input("Interest rate: "))

monthly_payment = car_loan(principal, years, rate)
print("Monthly Payment: ", monthly_payment)