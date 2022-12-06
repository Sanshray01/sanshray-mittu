Gross_Income = int(input("Enter your Gross Income :"))
Number_Of_Dependents = int(input("Enter number of dependents : "))
Taxable_Income = Gross_Income - 10000 -(3000*Number_Of_Dependents)
if Taxable_Income<0:
    print("tax = 0")
else:

#total tax to be paid

    print(f"Tax = {Taxable_Income*0.2}")