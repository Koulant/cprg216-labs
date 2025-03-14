#Assignment: Programming basics
#Anton Koulikov
print("Welcome to the Global Green Energy bill calculator!")

#Inputs
account_number = int(input("Enter your Global Green Energy account number."))
month_number = int(input("Enter the month number (e.g., for January, enter 1)."))
eplan = str(input("Enter your electricity plan (EFIR or EFLR)."))
ele = float(input(f"Enter the amount of electricity you in month {month_number} (Measured in kWh)."))
gplan = str(input("Enter your gas plan (GFIR or GFLR)."))
gas = float(input(f"Enter the amount of gas you used in month {month_number}."))
province = str(input("Enter the abbreviation for your province of residence (two letters)."))

#Variables
month_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tax1 = float(1.05)
tax2 = float(1.13)
tax3 = float(1.15)
ele_EFIR = float(8.36*0.01)
ele_EFIR2 = float(9.41*0.01)
ele_EFLR = float(9.11*0.01)
gas_GFIR = float(4.56*0.01)
gas_GFIR2 = float(5.89*0.01)
gas_GFLR_rate = float(3.93)
gas_GFLR = float(gas_GFLR_rate * 0.01)
monthly_fee = float(120.62)
monthly_fee2 = float(1.32)

#Outputs
#Test 1 total should be = 41.8 + 22.8 + monthly fees + tax = 195.867
#Test 2 total should be = 63.77 + 27.51 + monthly fees + tax = 223.881
#Test 3 total should be = (83.6 + 9.41) 93.01 + (43.43 + 21.793) 65.223 + monthly fees + tax = 280.173
while True:
    if eplan == "EFIR":
        if ele <= 1000:
            ele_billfir = float((ele_EFIR * ele))
            #print("Electricity costs: $", ele_billfir)
        elif ele > 1000:
            ele_billfir = float(ele_EFIR2 * ele)
            #print("Electricity costs: $", ele_billfir)
        break
    if eplan == "EFLR":
        ele_billflr = float((ele_EFLR * ele))
        #print("Electricity costs: $", ele_billflr)
    break

while True:
    if gplan == "GFIR":
        if gas <= 950:
            gas_billfir = float((gas_GFIR * ele))
            #print("Electricity costs: $", gas_billfir)
        elif gas > 950:
            ele_billfir = float(gas_GFIR2 * ele)
            #print("Electricity costs: $", gas_billfir)
        break
    if gplan == "GFLR":
        gas_billflr = float((gas_GFLR * ele))
        #print("Gas costs: $", gas_billflr)
    break

while True:
    if province == "AB" or "BC" or "MB" or "NT" or "NU" or "QC" or "SK" or "YT":
        provincetax = tax1
    elif province == "ON":
        provincetax = tax2
    elif province == "NB" or "NL" or "NS" or "PE":
        provincetax = tax3
    else:
        print("Error, please try again.")
    break

if eplan == "EFIR" and gplan == "GFIR":
    total = round((provincetax * (ele_billfir + gas_billfir + monthly_fee + monthly_fee2)), 2)

if eplan == "EFIR" and gplan == "GFLR":
    total = round((provincetax * (ele_billfir + gas_billflr + monthly_fee + monthly_fee2)), 2)

if eplan == "EFLR" and gplan == "GFIR":
    total = round((provincetax * (ele_billflr + gas_billflr + monthly_fee + monthly_fee2)), 2)

if eplan == "EFLR" and gplan == "GFLR":
    total = round((provincetax * (ele_billflr + gas_billflr + monthly_fee + monthly_fee2)), 2)

#Program
print("Thank you! Your total amount due now is: $", total)