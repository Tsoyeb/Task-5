#Capstone project- variables and control structures. 
#The below program will help the user calculate the interest they will earn on an investment or the amount they need to pay on a home loan. 

import math 


print('Investment - to calculate the amount of interest you will earn on your investment')
print('Bond -  to calculate the amount you will have to pay on a home loan')

# if input is investment the following questions will be asked to gather information in order to calculate the interest amount.
# If the choice is invalid then the user will be prompted to enter the choice again

ask_again_outer = True
while(ask_again_outer):

        customer_input= input('Please enter Investment or Bond from the menu above to proceed: ')
        if customer_input.lower() == 'investment':
                print('You have selected Investment.')
                amount = float(input('Please enter the sum you wish to deposit: '))
                rate= float(input('Please enter your interest rate: '))
                years= int(input('Please enter how many years you intend to invest for: '))

                ask_again_inner = True #This is used to determine whether the user should be prompted for the input again
                while(ask_again_inner):
                        interest= input('Please enter if you would like simple or compound interest: ')

                        if interest.lower()== 'simple':
                                #calculation for simple interest.
                                total_s= amount*(1 + (rate/100)*years)
                                print(f'You have selected simple interest your interest is: {total_s:.2f}')
                                ask_again_inner = False

                        elif interest.lower() == 'compound':
                                #calculation for compound interest.
                                total_c= amount*math.pow((1+(rate/100)),years)
                                print(f'You have selected Compound interest your interest is: {total_c:.2f}')
                                ask_again_inner = False
                        else:
                                print('The entry you have made is invalid.')
                                ask_again_inner = True

                ask_again_outer = False

        # If input is bond the following information is required from the user in order to calculate the repayment ammount.  
        elif customer_input.lower() == 'bond':
                print('You have selected Bond.')
                value = float(input('Please enter the present value of your home: '))
                rate= float(input('please enter your annual interest rate: '))
                months= int(input('Please enter how many months you intend to take to repay the bond: '))
                
                #calculation for bond repayment amount. 
                monthly_rate =((rate/100)/12)
                repayment_sum= ((monthly_rate*value)/(1 - (1+ monthly_rate)**(-months)))
                print (f'Your monthly repayment is: {repayment_sum:.2f}')
                ask_again_outer = False
        else:
                print('The entry you have made is invalid.')
                ask_again_outer = True



