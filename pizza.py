#Name: Brian Williams & Dustin Bowyer
#Prog Purpose: compute employee hours and pay

import datetime

###### questions have to be asked: Residency, Number of credits, Amount of scholarship received.

############ define global variables #############
# define tuition fees for in and out of state students.
SMALL = 9.99
MEDIUM = 12.99
LARGE = 14.99
EXTRA_L = 17.99

SALES_TAX = .055


#define global variables
category = 0 # S small, M medium, L large, XL, extra large
sales_tax = 0
num_pizza = 0
subtotal = 0
total = 0

########### define program functions ############
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\n\nWould You Like to Order More Pizzas? (Y/N): ")
        if yesno.upper() != "Y":
            another_employee = False

def get_user_data():
    global category, num_pizza
    category = input("What Size Pizza would you like? S for small, M for medium, L for large, XL for extra large: ")
    num_pizza = int(input("\nEnter Number of Pizzas "))

def perform_calculations():
    global category, num_pizza, subtotal, sales_tax, total
    if category == "S" or category == "s" :
        subtotal = num_pizza * SMALL
        
    if category == "M" or category == "m" :
        subtotal = num_pizza * MEDIUM
        
    if category == "L" or category == "l" :
        subtotal = num_pizza * LARGE
        
    if category == "XL" or category == "xl" :
        subtotal = num_pizza * EXTRA_L
        

    sales_tax = subtotal * SALES_TAX
    total = sales_tax + subtotal

def display_results():
    print('\n\nPalermos Pizza!')
    print('\n--------------------------------------')
    print('Number of Pizzas :      ' + str(num_pizza))
    print('Sales Tax            $  ' + format(sales_tax,'5,.2f'))
    print('Subtotal             $  ' + format(subtotal,'5,.2f'))
    print('--------------------------------------')
    print('Total               $ ' + format(total,'5,.2f'))
    print('\n--------------------------------------')
    print(str(datetime.datetime.now()))
    print('--------------------------------------')

######### call on main program to execute ########
main()
