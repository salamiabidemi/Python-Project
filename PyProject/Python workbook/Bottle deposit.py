LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25
less = int(input("How many containers 1 litre or less do you have? "))
more = int(input("How many containers more than litre do you have? "))
refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT
print("Your total refund will be $%.2f." % refund)
