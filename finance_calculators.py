import math
#Tells the user what to input to determine the finance type
print("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan \n\nEnter either 'investment' or 'bond' from the menu above to proceed:")

#User input
finance_type = input()

#Changes the input casing to lower so that the result is not changed by casing
finance_type = finance_type.lower()

#investment calculation
if finance_type == "investment":
    
    deposit = input("Enter how much money are you depositing: ")

    interest_rate = input("Enter the interest rate (Number not percentage): ")

    duration = input("Enter how many years you plan on investing: ")

    interest = input("Simple or Compound interest: ")
    interest = interest.lower()
    interest_rate = int(interest_rate) / 100

    if interest == "simple":
        sum = int(deposit)*(1 + interest_rate * int(duration))
        print(sum)
    elif interest == "compound":
        sum = int(deposit) * math.pow((1 + interest_rate), int(duration))
        print(sum)

#bond calculation
elif finance_type == "bond":
    
    house_value = input("Enter your present house value: ")
    
    interest_rate = input("Enter the interest rate (Number not percentage): ")
    interest_rate = int(interest_rate) / 100
    
    bond_repayment_duration = input("Enter the number of months to repay the bond: ")
                        
    repayment = ((interest_rate / 12) * int(house_value))/(1 - (1 + (interest_rate / 12))**(-int(bond_repayment_duration)))
    print(repayment)