#Name: Brian Williams & Dustin Bowyer
#Prog Purpose: compute employee hours and pay

import datetime

###### questions have to be asked: Residency, Number of credits, Amount of scholarship received.

############ define global variables #############
# define tuition fees for in and out of state students.
CASHIER = 16.50
STOCKER = 15.75
JANITOR = 15.75
MAINTENANCE = 19.50


FED_TAX = .12   #  12%
STATE_TAX = .03 #  03%
SS_TAX = .062   #  06.2%
MED_TAX = .0145 #  01.45%


#define global variables
category = 0 # C for cashier S for Stocker J for Janitor M for Maintenance
fed_tax = 0
state_tax = 0
ss_tax = 0
med_tax = 0
gross = 0
total = 0
hours = 0

########### define program functions ############
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\n\nWould You Like to Calculate Another Employees Hours? (Y/N): ")
        if yesno.upper() != "Y":
            another_employee = False

def get_user_data():
    global category, hours
    category = input("Enter C for Cashier, S for Stocker, J for Janitor, M for Maintenance: ")
    hours = int(input("\nEnter Number of Hours Worked "))

def perform_calculations():
    global category, hours, fed_tax, state_tax, ss_tax, med_tax, gross, total
    if category == "C" or category == "c" :
        gross = hours * CASHIER
        
    if category == "S" or category == "s" :
        gross = hours * STOCKER
        
    if category == "J" or category == "j" :
        gross = hours * JANITOR
        
    if category == "M" or category == "m" :
        gross = hours * MAINTENANCE
        

    fed_tax = gross * FED_TAX
    state_tax = gross * STATE_TAX
    ss_tax = gross * SS_TAX
    med_tax = gross * MED_TAX
    total = gross - fed_tax - state_tax - ss_tax - med_tax


def display_results():
    print('\n\nFresh Foods Market Employee Pay Ticket')
    print('\n--------------------------------------')
    print('Hours Worked :          ' + str(hours))
    print('Gross Pay             $ ' + format(gross,'5,.2f'))
    print('Federal Income       -$ ' + format(fed_tax,'5,.2f'))
    print('State Income Tax     -$ ' + format(state_tax,'5,.2f'))
    print('Social Security Tax  -$ ' + format(ss_tax,'5,.2f'))
    print('Medicare Tax         -$ ' + format(med_tax,'5,.2f'))
    print('--------------------------------------')
    print('Net Pay               $ ' + format(total,'5,.2f'))
    print('\n--------------------------------------')
    print(str(datetime.datetime.now()))
    print('--------------------------------------')

######### call on main program to execute ########
main()
