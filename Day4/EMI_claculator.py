principle: float = float(input("Enter the principle: "))
interest: float = float(input("Enter the rate of interest: "))
time: int = int(input("Enter the time in years: "))

def calc_monthly_interest(principal, interest, time):
    monthly_interest: float = round(principle * interest/12 *time/100 ,2)
    return monthly_interest


monthly_interest = calc_monthly_interest(principle, interest, time)

def calc_emi(principal, interest, time):
    emi = round(principle * monthly_interest * (1+ interest)**(time*12) / ((1+ interest)**(time*12) -1),2)
    return emi

emi = calc_emi(principle, interest, time)

def compute_emi_details(principal, interest, time):
    emi_details: list = []
    emi = calc_emi(principal, interest, time)
    balance: float = principal

    for month in range(1, time*12 +1):
        emi_dict: dict = {}

        monthly_interest = calc_monthly_interest(balance, interest, 12)
        principal: float = emi - interest
        balance: float = balance - principal

        if balance < 0:
            principal: float = round(principal + emi, 2)
            emi = round(principal + monthly_interest, 2)
            balance = 0

        emi_dict["Principal"] = principal
        emi_dict["EMI"] = emi
        emi_dict["Balance"] = balance
        emi_dict["Month"] = month
        emi_dict["Monthly Interest"] = monthly_interest

        emi_details.append(emi_dict)
    return emi_details

emi_details = compute_emi_details(principle, interest, time)
#print(f"EMI Details for Principal: {principle}, ROI: {interest}, Years: {time} is")
#for emi_detail in emi_details:
#    print(emi_detail)


def display_emi_details(emi_details):
    print("-"*68)
    print(f"| {'Month':^8} | {'EMI':^10} | {'Interest':^10} |", f"| {'Principal':^10} | {'Balance':^10} |")
    print("-"*68)

    total_month =  total_emi = total_interest = total_principal = 0.0

    for emi_detail in emi_details:
        month = emi_detail["Month"]
        emi = emi_detail["EMI"]
        balance = emi_detail["Balance"]
        principal = emi_detail["Principal"]
        interest = emi_detail["Monthly Interest"]

        total_month += 1
        total_emi += emi
        total_interest += interest
        total_principal += principal

        print(f"| {month:^8} | {emi:^10} | {interest:^10} |", f"| {principal:^10} | {balance:^10} |")
        print("-" * 68)

    print(f"| {'Total':^8} | {total_emi:^10.2f} | {total_principal:^10.2f} |", f"| {total_principal:^10.2f} | {balance:^10.2f} |")
    print("-" * 88)

display_emi_details(compute_emi_details(principle, interest, time))




