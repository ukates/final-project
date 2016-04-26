import time, datetime, os
os.makedirs(('LoanDetails'), exist_ok=True)


print('WELCOME TO YOUR PERSONAL AUTO LOAN CALCULATOR!')
print()
while True:
    try:
        print('How much will you be borrowing? #NOTE# No need for commas!\n')
        p = float(input())
    except ValueError:
        print('Invalid input, please do not use commas!\n')
    else:
        break
while True:
    try:
        print('What will be your interest rate? #NOTE# No % symbol needed! An example of the proper format is 7.99\n' )
        rate = float(input())/100
        r = (rate/int(12))
    except ValueError:
        print('Invalid input, please do not use % symbol! ')
    else:
        break
while True:
    try:
        print('In how many months would you like to pay this off? Integers only please!')
        l = int(input())
    except ValueError:
        print('Invalid input, integers only please!\n')
    else:
        break
while True:
    try:
        date_entry = input('Lastly, what will be the date of your first payment?\nPlease use the format YYYY-MM-DD:\n') 
        year, month, day = map(int, date_entry.split('-'))
        paymentDate= datetime.date(year,month,day)
        some_day = datetime.timedelta(l*365/12)
        payOffDate = paymentDate + some_day
    except ValueError:
        print('Invalid format, please use YYYY-MM-DD with dashes please!\n')
    else:
        break


def payOff(p,r,l):
    a = p*(r*(1+r)**l)
    b = (((1+r)**l)-1)
    c = (a/b)

    totalPayoff = (c*l)
    interestPaid = totalPayoff - p
    print()
    print('Calculating...')
    print()
    time.sleep(3)
    print('In order to pay off your loan in ' + str(l) + ' months, you would need to pay $' + str(round(c,2)) + ' per month.')
    print()
    time.sleep(2)
    print()
    print('Once the loan is complete, you will have paid $' + str(round(interestPaid,2)) + ' in interest!')
    print()
    time.sleep(2)
    print()
    print('Based on the date of your first payment, you will complete the terms of your loan on ' + str(payOffDate) + ' having paid a total of $ ' + str(round(totalPayoff,2)))

    

    
    resultFile = open('LoanDetails/payOffResults.txt', 'w')
    resultFile.write('In order to pay off your loan in ' + str(l) + ' months, you would need to pay $' + str(round(c,2)) + ' per month.\n\nOnce the loan is complete, you will have paid $' + str(round(interestPaid,2)) + ' in interest!\n\nBased on the date of your first payment, you will complete the terms of your loan on ' + str(payOffDate) + ' having paid a total of $ ' + str(round(totalPayoff,2)))
    resultFile.close()

payOff(p,r,l)


    
