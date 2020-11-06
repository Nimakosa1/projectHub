"""This simple program calculates the restaurant bill
taking into consideration the tip given and also the number of
of people to split the bill.
"""

print("===========================================")
print("Welcome to The Geo Accurate Bill Calculator")
print("===========================================")
print()

bill_amount = float(input("What was the bill? "))
tip_percent = int(input("What percentage tip will you like to give: 10, 12, or 15 ? "))
tip_amount = (tip_percent/100) * bill_amount
total_bill = tip_amount + bill_amount

bill_splitting = input("Are you splitting the bill? ")

if bill_splitting == "Yes" or bill_splitting == "YES":
    num_people = int(input("How many people to split the bill? "))
    tip_per_person = tip_amount / num_people
    total_per_person = total_bill / num_people
    print("Tip per person is GHC {:.2f} and total per person is GHC {:.2f}".format(tip_per_person, total_per_person))
elif bill_splitting == "No" or bill_splitting == "NO":
    print("The total bill is GHC {:.2f}".format(total_bill))

print("Thanks for using the Geo Bill Calculator")
