#Name: Brian Williams
#Prog Purpose: compute tuition, fees, and balance for pvcc student based on inputs listed in handout

import datetime

###### questions have to be asked: Residency, Number of credits, Amount of scholarship received.

############ define global variables #############
# define tuition fees for in and out of state students.
TUITION_IN = 155
TUITION_OUT = 331.6
INST_FEE = 1.75
ACT_FEE = 2.9
CAP_FEE = 23.5

#define global variables
num_cred = 0
scholar_amt = 0
total = 0
resident = 1 # 1 means in state, 2 means out of state
tuition = 0
inst = 0
cap = 0
act = 0
bal = 0


########### define program functions ############
def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.upper() != "Y":
            another_student = False

def get_user_data():
    global resident, num_cred, scholar_amt
    resident = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    num_cred = int(input("Number of credits registered for: "))
    scholar_amt = float(input("Scholorship amout received; If none enter Number zero: "))

def perform_calculations():
    global tuition, cap, inst, act, total, bal
    if resident == 1:
        tuition = num_cred * TUITION_IN
        cap = 0
    else:
        tuition = num_cred * TUITION_OUT
        cap = num_cred * CAP_FEE

    inst = num_cred * INST_FEE
    act = num_cred * ACT_FEE
    total = tuition + cap + inst + act
    bal = total - scholar_amt

def display_results():
    print('--------------------------------')
    print('Number of credits : ' + str(num_cred))
    print('Tuitions          $ ' + format(tuition,'10,.2f'))
    print('Capital fee       $ ' + str(cap))
    print('Institution Fee   $ ' + str(inst))
    print('Activity Fee      $ ' + str(act))
    print('Total             $ ' + str(total))
    print('Scholarship       $ ' + str(scholar_amt))
    print('--------------------------------')
    print('Balance Owed      $ ' + str(bal))
    print(str(datetime.datetime.now()))
    print("NOTE: PVCC Fee Rates: https:www.pvcc.edu/tuition-and-fees")

######### call on main program to execute ########
main()
