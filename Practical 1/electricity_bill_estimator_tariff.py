print("Electricity bill estimator")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_price = float(input("Which Tariff? 11 or 31 : "))

if tariff_price == 11:
    tariff_cost = TARIFF_11

elif tariff_price == 31:
    tariff_cost = TARIFF_31

else:
    print("Invalid")

price_daily = float(input("Enter daily use in kWh: "))
number_billing = float(input("Enter number of billing days: "))

estimated_bill = price_daily * number_billing * tariff_cost

print("Estimated Bill: ${}" .format(estimated_bill))
