# EMI Calculator

# Get input values from user
p = float(input('Enter Principal Amount: '))
iry = float(input('Enter Annual Interest Rate (in %): '))
yr = float(input('Enter Number of Years: '))

# Calculate monthly interest rate
ir = iry / (12 * 100)

# Convert years into months
mn = yr * 12

# Check if interest rate is zero (simple division protection)
if ir == 0:
    emi = p / mn
else:
    # Calculate Monthly EMI using the formula
    emi = (p * ir * ((1 + ir) ** mn)) / (((1 + ir) ** mn) - 1)

# Calculate total payment and interest
total_payment = emi * mn
total_interest = total_payment - p

# Display the results
print("\n===== EMI Calculation Result =====")
print(f"Monthly EMI: {emi:.2f}")
print(f"Total Payment (Principal + Interest): {total_payment:.2f}")
print(f"Total Interest Payable: {total_interest:.2f}")
print("==================================")