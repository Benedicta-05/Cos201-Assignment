# Name - Boardman Benedicta Divine
# Matric No - BU24SEN1036
# Assignment - U.S Federal Personal Income Tax Calculator

# Filing Status:
# 0 - Single filers
# 1 - Married filing jointly or qualified widow(er)
# 2 - Married filing separately
# 3 - Head of household

         
print("US Federal Income Tax Calculator (2009)")

def get_tax_data(status):
    """Return tax brackets and rates based on filing status"""

    if status == 0:   # Single
        return [8350, 33950, 82250, 171550, 372950], \
            [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    if status == 1:   # Married Filing Jointly
        return [16700, 67900, 137050, 208850, 372950], \
               [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    if status == 2:   # Married Filing Separately
        return [8350, 33950, 68525, 104425, 186475], \
               [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    if status == 3:   # Head of Household
        return [11950, 45500, 117450, 190200, 372950], \
               [0.10, 0.15, 0.25, 0.28, 0.33, 0.35] 
    
    print("Invalid Tax filing status! Enter 0, 1, 2, or 3.")
    return None, None


# Get the status filing
print("Tax breakdown as follows:")
print("0 - Single")
print("1 - Married Filing Jointly")
print("2 - Married Filing Separately")
print("3 - Head of Household")

status = int(input("Enter number (0-3): "))

tax_limits, tax_rates = get_tax_data(status)

if tax_limits is None:
    quit()

#Taxable income
income = float(input("Enter taxable income: "))


# Now calculate the tax        
tax = 0.0
previous_limit = 0.0
breakdown = []
    

for i in range(len(tax_limits)):
    if income > tax_limits[i]:
        tax += (tax_limits[i] - previous_limit) * tax_rates[i]
        previous_limit = tax_limits[i]
    else:
        tax += (income - previous_limit) * tax_rates[i]
        break
else:
    tax += (income - previous_limit) * tax_rates[-1]

print("\nCalculation complete!")
print("\nYour Federal Income Tax is: ${:.2f}".format(tax))
print("Thank you for using the U.S. Federal Income Tax Calculator (2009). Have a great day!")



