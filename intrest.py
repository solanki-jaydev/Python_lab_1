def calculate_simple_interest(principal, time, rate):
    return (principal * time * rate) / 100

principal = float(input("Enter principal amount: "))
time = float(input("Enter time period (in years): "))
rate = float(input("Enter rate of interest (per annum): "))

simple_interest = calculate_simple_interest(principal, time, rate)

print(f"Simple Interest: {simple_interest}")
