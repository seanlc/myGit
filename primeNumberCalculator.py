number = int(raw_input("Enter the number you think may be prime: "))
prime = True
divisor = []
for num in range(2,number):
    if number % num == 0:
        prime = False
        divisor.append(num)
if prime:
    print str(number) + " is prime"
else:
    divisors = ""
    for num in divisor:
        divisors += str(num)
        divisors += " "
    print "the divisors of " + str(number) + " are " + divisors