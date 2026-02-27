total = int(input("What is your total sales for this month?"))
def sales_tax():
    Sales_Tax = total - (total - total * 0.05)
    return Sales_Tax
def county_tax():
    County_Tax = total - (total - total * 0.025)
    return County_Tax

Total = sales_tax() + county_tax()

print("Your county tax is :", county_tax())
print("Your sales tax is :", sales_tax())
print("Your total sales tax is :", Total)
