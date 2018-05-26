print("Electricity bill estimator")
price_kwh = float(input("Enter cents per kWh: "))
price_daily = float(input("Enter daily use in kWh: "))
number_billing = float(input("Enter number of billing days: "))

total_price_kwh = price_kwh * 0.01
estimated_bill = total_price_kwh * price_daily * number_billing

print("Estimated Bill: ${}" .format(estimated_bill))
