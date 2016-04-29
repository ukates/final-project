import time, datetime, os 
os.makedirs(('LoanDetails'), exist_ok=True) #creates folder in current directory, does not crash if folder currently exists by using exist_ok=True


print('WELCOME TO YOUR PERSONAL AUTO LOAN CALCULATOR!') #this portion of code gets info from user and assigns it to variables that will be used in the function
print()
while True: #while loop, allows user to input their loan details without crashing if they make a mistake. 
    try:
        print('How much will you be borrowing? #NOTE# No need for commas!\n')
        p = float(input())
    except ValueError: #exception that prevents program from crashing, if user does not use correct input and program returns value error the program will loop back to try again
        print('Invalid input, please do not use commas!\n')
    else:
        break
while True: #asks for interest rate from user 
    try:
        print('What will be your interest rate? #NOTE# No % symbol needed! An example of the proper format is 7.99\n' )
        rate = float(input())/100 #takes interest rate from user and devides by 100 in order to turn it into a decimal
        r = (rate/int(12)) #takes apr devides by 12 months to get montly interest rate this is used in monthly payment formula. 
    except ValueError:
        print('Invalid input, please do not use % symbol! ')
    else:
        break
while True:
    try:
        print('In how many months would you like to pay this off? Integers only please!')
        l = int(input()) #asks user for months of loan
    except ValueError:
        print('Invalid input, integers only please!\n') #wording printed when exception occurs and user is looped back 
    else:
        break
while True:
    try:
        date_entry = input('Lastly, what will be the date of your first payment?\nPlease use the format YYYY-MM-DD:\n') #asks user for estimated first payment date
        year, month, day = map(int, date_entry.split('-')) #this maps the users input to take the information in year month and date taking out - as a split between the input
        paymentDate= datetime.date(year,month,day) #takes users input of date and assigns to paymentDate
        some_day = datetime.timedelta(l*365/12) #determines how far in future end payment will be 
        payOffDate = paymentDate + some_day #adds future date to payment date to return the date that the loan will be paid off
    except ValueError:
        print('Invalid format, please use YYYY-MM-DD with dashes please!\n')
    else:
        break


def payOff(p,r,l): #this is the function that will determine the monthly payment/ interest / and total payoff
    a = p*(r*(1+r)**l)
    b = (((1+r)**l)-1)
    c = (a/b)

    totalPayoff = (c*l)
    interestPaid = totalPayoff - p
    print()
    print('Calculating...')
    print()
    time.sleep(3) #this will pause program for three seconds before printing next line, give the illusion that the program is thinking
    print('In order to pay off your loan in ' + str(l) + ' months, you would need to pay $' + str(round(c,2)) + ' per month.') 
    print()
    time.sleep(2)
    print()
    print('Once the loan is complete, you will have paid $' + str(round(interestPaid,2)) + ' in interest!')
    print()
    time.sleep(2)
    print()
    print('Based on the date of your first payment, you will complete the terms of your loan on ' + str(payOffDate) + ' having paid a total of $ ' + str(round(totalPayoff,2)))
    print()
    print('Creating folder "LoanDetails" within current directory...')
    time.sleep(2)
    print('Creating file "payOffResults.txt" and saving to LoanDetails...')
    time.sleep(1)
    print('Process Complete!')
    

    
    resultFile = open('LoanDetails/payOffResults.txt', 'w') #opens loadetails folder and allows you to write to payoffresults.txt that is created
    resultFile.write('In order to pay off your loan in ' + str(l) + ' months, you would need to pay $' + str(round(c,2)) + ' per month.\n\nOnce the loan is complete, you will have paid $' + str(round(interestPaid,2)) + ' in interest!\n\nBased on the date of your first payment, you will complete the terms of your loan on ' + str(payOffDate) + ' having paid a total of $ ' + str(round(totalPayoff,2)))#write to the txt document
    resultFile.close() #closes text document that will be saved in loandetails folder. 
    

payOff(p,r,l) #calls the function payOff by using variables P,R, and L that are determined by user


    
