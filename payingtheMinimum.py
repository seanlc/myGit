balance = 320000
originalBalance = balance
annualInterestRate = .2
monthlyInterestRate = annualInterestRate / 12.0
hi = (originalBalance * (1+monthlyInterestRate) ** 12)/12.0
lo = originalBalance / 12
foundAnswer = False
while not foundAnswer:
    payment = (hi+lo)/2
    for n in range(12):
        balance -= payment
        balance += (balance * monthlyInterestRate)
    if balance < 0 and balance > -.25:
        foundAnswer = True
    elif balance < 0:
        hi = payment
    else:
        lo = payment
    balance = originalBalance
print ("Lowest Payment: " + str(round(payment,2)))