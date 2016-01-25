# MITx Problem Set 2
#try use bisection search

# case not using bisection
# month = 10

# while True:
#    test = balance
#    for i in range(12):
#        test = (test - month)*(1+annualInterestRate/12)

#    if test - 0 > 0.1:
#        month += 10
#    elif test - 0<0.1:
#        break

# print "Lowest Payment: "+ str(int(month))

mRate = annualInterestRate/12.0
# lower bound suppose there is no interest
lb = balance/12.0
# upper bound suppose pay all the debt & interst for the whole year 
ub = balance*(1+mRate)**12/12.0

while True:
    month = (lb+ub)/2
    test = balance

    for i in range(12):
        test = (test - month)*(1+annualInterestRate/12)

    if test > 0.1:
        lb = month
    elif test < -0.1:
        ub = month
    else:
        break

print "Lowest Payment: "+ str(round(month,2))
