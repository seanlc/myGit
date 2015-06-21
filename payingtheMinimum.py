balance = 5000
originalBalance = balance
annualInterestRate = .098
monthlyInterestRate = annualInterestRate / 12.0
payment = 10
foundAnswer = False
while not foundAnswer:
    for n in range(12):
        balance -= payment
        balance += (balance * monthlyInterestRate)
    if balance < 0:
        foundAnswer = True
    else:
        payment += 10
        balance = originalBalance
print ("Lowest Payment: " + str(payment))