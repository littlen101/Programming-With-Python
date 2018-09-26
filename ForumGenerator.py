#Using to insert line breaks
import sys

#Instantiate string variables
sStmt_initial = str('Who must use this form?:\n'
'\t1. Whether or not you have - W-2 Forms from all employers you (and your spouse,\n\t   if filing a joint return) worked for during the past tax year.\n'
'\t2. Whether or not you have - 1099 Forms if you (or your spouse) completed contract\n\t   work and earned more than $600.\n') 
sStmt_non_monetary_values = str('\nGENERAL INFORMATION: \nPress ENTER after recording values for each prompt. If a given prompt does not apply, simply press ENTER to continue.\n\n'
'Press ENTER to begin inputting information related to yourself and your family.\n\n')
sStmt_monetary_values = str('\nENTER GENERAL INFORMATION:\nPress ENTER after recording exact monetary values for the prompts to follow.\n' 
'If you have nothing to report for a given prompt, press ENTER to continue, and $0.00 will be recorded for you.\n\n'
'Press ENTER to begin.\n\n')
sFormEntryRecap_inc = 'Entries representing income:\n\n'
sFormEntryRecap_cred = 'Entries representing credits:\n\n'
sFormEntryRecap_gen_stmt = '\nPress enter to see a summary of your entries and to view your calculated tax or refund.\n\tIf you are entitled to a refund, follow prompts for delivery.\n\n'
sPrompt_SSN_personal = 'Your Social Security number without using hypens: '
sPrompt_SSN_spouse = 'Your spouse’s Social Security number without hyphens (if married): '
sPrompt_SSN_dependents = 'Social Security numbers for any dependents: '
sPrompt_Invstmnt_inc = 'Investment income information (including: interest income, dividend income, proceeds from the sale of bonds or stocks, and income from foreign investments): '
sPrompt_StateLocalTax_inc = 'Income from local and state tax refunds from the prior year: '
sPrompt_Bus_inc = 'Business income (accounting records for any business that you own): '
sPrompt_Unemp_inc = 'Unemployment income: '
sPrompt_Rental_inc = 'Rental property income: '
sPrompt_SS_inc = 'Social Security benefits: '
sPrompt_Misc_inc = 'Miscellaneous income (including: jury duty, lottery and gambling winnings, Form 1099-MISC for prizes and awards, and Form 1099-MSA for distributions from medical savings accounts): '
sPrompt_Homebuyer_cred = 'Homebuyer tax credit: '
sPrompt_Energy_cred = 'Green energy credits: '
sPrompt_IRA_cred = 'IRA contributions: '
sPrompt_Mortgage_cred = 'Mortgage interest: '
sPrompt_Student_cred = 'Student loan interest: '
sPrompt_MedSavingsAcct_cred = 'Medical Savings Account (MSA) contributions: '
sPrompt_SelfEmpHealthIns_cred = 'Self-employed health insurance: '
sPrompt_Job_Moving_cred = 'Job and moving expenses: ' 
#Moving expenses --- THIS SEEMS TO BE REPEAT
sPrompt_Education_cred = 'Education costs: '
sPrompt_Childcare_cred = 'Childcare costs: '
sPrompt_Adoption_cred = 'Adoption costs: '
sPrompt_Contrib_cred = 'Charitable contributions/donations: '
sPrompt_CasualtyTheft_cred = 'Casualty and theft losses: '
sPrompt_QualBus_cred = 'Qualified business expenses: '
sPrompt_MedExp_cred = 'Medical expenses: '
#If a return is due
sPrompt_CheckOrDD = 'You will now be asked if you prefer having your refund sent via check sent or via direct deposit.\n'
sYNcheck = 'Do you prefer a check? Type Y or N and then press ENTER.\n'
sDDinfo = 'Please provide your bank information for direct deposit. Press ENTER after each entry.\n'
#If direct deposit is chosen, obtain bank information
sPrompt_BankAcctNum = 'Your bank account number: '
sPrompt_BankRtgNum = 'The bank’s routing number: '

enteredNumReq = '\nYou must enter a number.\n'
incorrectPrecisionReq = 'Invalid monetary entry.\n'

# Function returns 9 digit int after determining character length and reprompting for correct entry length
def is_nine_digits(sPromptVal,sInputVal,DesiredLength):
    if sInputVal != '':
        while int(len(sInputVal)) != int(DesiredLength):
            sInputVal = input(sPromptVal + ' (Number should contain exactly {} characters): '.format(DesiredLength))
        return sInputVal

# Function returns boolean, indicating whether an entry is an int datatype with a value greater than 0.
def is_int(sInputVal):   
    try:
        int(sInputVal) > 0
        return True
    except ValueError:
        return False

# Function returns boolean, indicating whether an entry is a float datatype with a value greater than 0.
def is_number(x):
    try:
        float(x) > 0
        return True
    except ValueError:
        return False

# Function returns boolean, indicating whether float float precision is limited to two decimal spaces or less.
def precision_check(y):
    if '.' not in str(y):
        bCorrectPrecision = True
    else:    
        lstValSplit: list = (str(y).split('.',2))
        decimalVal: str = lstValSplit[1]
        lengthPrecision = len(decimalVal)
        bCorrectPrecision = lengthPrecision < 3
    return bCorrectPrecision

# Function returns string value, possibly
def money_val_str_output(z):
    if '.' not in str(z):
        z = str(z) + '.00'
    else:    
        lstValSplit: list = (str(z).split('.',2))
        if len(lstValSplit[1]) == 1:
            z = str(z) + '0'
        elif len(lstValSplit[1]) == 2:
            z = str(z)
    return z

# Function prompts users to enter proper monetary value before proceeding. Returns float value.
def num_entry_eval(sPromptVal,inputFltNumVal):
    is_flt = is_number(inputFltNumVal)
    is_correct_precision = precision_check(inputFltNumVal)
    if is_flt is False or is_correct_precision is False or (is_flt is True and float(inputFltNumVal) <= int(0)) :
        not_valid_entry = True
        loopIncorrectValType: int = 0
        while not_valid_entry:
            if loopIncorrectValType > int(0):
                    inputFltNumVal = input(sPromptVal)
                    is_correct_precision = precision_check(inputFltNumVal)
            elif str(inputFltNumVal) == '':
                not_valid_entry = False  
            else:
                if is_correct_precision is False:
                    print(incorrectPrecisionReq)
                    loopIncorrectValType = loopIncorrectValType + 1
                else:    
                    print(enteredNumReq)
                    loopIncorrectValType = loopIncorrectValType + 1
            if is_flt is True and float(inputFltNumVal) > int(0) and is_correct_precision is True:
                not_valid_entry = False
        if str(inputFltNumVal) == '':
            inputFltNumVal = '0.0'
    return float(inputFltNumVal)    
        
def main():
    # General, introductory statements
    print(sStmt_initial)
    input(sStmt_non_monetary_values)

    # SSN information
    input_num_SSN_personal = input(sPrompt_SSN_personal)
    num_SSN_personal = is_nine_digits(sPrompt_SSN_personal,input_num_SSN_personal,int(9))
    if str(input_num_SSN_personal) == '':
        while input_num_SSN_personal == '':
            input_num_SSN_personal = input(sPrompt_SSN_personal)
    if str(input_num_SSN_personal) != '':  
        bNum_SSN_personal_is_int = is_int(input_num_SSN_personal)
        if bNum_SSN_personal_is_int is False: 
            while bNum_SSN_personal_is_int is False:
                input_num_SSN_personal = input(sPrompt_SSN_personal + ' (Number should contain exactly 9 characters): ')
                bNum_SSN_personal_is_int = is_int(input_num_SSN_personal)       
    input_num_SSN_Spouse = input(sPrompt_SSN_spouse)
    num_SSN_Spouse = is_nine_digits(sPrompt_SSN_spouse,input_num_SSN_Spouse,int(9))
    input_num_SSN_dependents = input(sPrompt_SSN_dependents)
    num_SSN_dependents = is_nine_digits(sPrompt_SSN_dependents,input_num_SSN_dependents,int(9))
    if str(input_num_SSN_dependents) != '':
        lst_num_SSN_dependents = ()
        while str(input_num_SSN_dependents) != '':
            num_SSN_dependents = is_nine_digits(sPrompt_SSN_dependents,input_num_SSN_dependents,int(9))
            lst_num_SSN_dependents: list = (lst_num_SSN_dependents,num_SSN_dependents)
            input_num_SSN_dependents = input(sPrompt_SSN_dependents)
 
    #obtain income source values below this line. Place into list, filling any blank spaces in with 0.0
    input(sStmt_monetary_values)
    input_num_Invstmnt_inc = input(sPrompt_Invstmnt_inc)
    num_Invstmnt_inc = num_entry_eval(sPrompt_Invstmnt_inc,input_num_Invstmnt_inc)
    input_num_StateLocalTax_inc = input(sPrompt_StateLocalTax_inc)
    num_StateLocalTax_inc = num_entry_eval(sPrompt_StateLocalTax_inc,input_num_StateLocalTax_inc)
    input_num_Bus_inc = input(sPrompt_Bus_inc)
    num_Bus_inc = num_entry_eval(sPrompt_Bus_inc,input_num_Bus_inc)
    input_num_Unemp_inc = input(sPrompt_Unemp_inc)
    num_Unemp_inc = num_entry_eval(sPrompt_Unemp_inc,input_num_Unemp_inc)
    input_num_Rental_inc = input(sPrompt_Rental_inc)
    num_Rental_inc = num_entry_eval(sPrompt_Rental_inc,input_num_Rental_inc)
    input_num_SS_inc = input(sPrompt_SS_inc)
    num_SS_inc = num_entry_eval(sPrompt_SS_inc,input_num_SS_inc)
    input_num_Misc_inc = input(sPrompt_Misc_inc)
    num_Misc_inc = num_entry_eval(sPrompt_Misc_inc,input_num_Misc_inc)

    total_combined_income: float = (num_Invstmnt_inc + num_StateLocalTax_inc +
        num_Bus_inc + num_Unemp_inc + num_Rental_inc + num_SS_inc +
        num_Misc_inc)

    #obtain tax source values below this line. Place into list, filling any blank spaces in with 0.0
    input_num_Homebuyer_cred = input(sPrompt_Homebuyer_cred)
    num_Homebuyer_cred = num_entry_eval(sPrompt_Homebuyer_cred,input_num_Homebuyer_cred)
    input_num_Energy_cred = input(sPrompt_Energy_cred)
    num_Energy_cred =num_entry_eval(sPrompt_Energy_cred,input_num_Energy_cred)
    input_num_IRA_cred = input(sPrompt_IRA_cred)
    num_IRA_cred = num_entry_eval(sPrompt_IRA_cred,input_num_IRA_cred)
    input_num_Mortgage_cred = input(sPrompt_Mortgage_cred)
    num_Mortgage_cred = num_entry_eval(sPrompt_Mortgage_cred,input_num_Mortgage_cred)
    input_num_Student_cred = input(sPrompt_Student_cred)
    num_Student_cred = num_entry_eval(sPrompt_Student_cred,input_num_Student_cred)
    input_num_MedSavingsAcct_cred = input(sPrompt_MedSavingsAcct_cred)
    num_MedSavingsAcct_cred = num_entry_eval(sPrompt_MedSavingsAcct_cred,input_num_MedSavingsAcct_cred)
    input_num_SelfEmpHealthIns_cred = input(sPrompt_SelfEmpHealthIns_cred)
    num_SelfEmpHealthIns_cred = num_entry_eval(sPrompt_SelfEmpHealthIns_cred,input_num_SelfEmpHealthIns_cred)
    input_num_Job_Moving_cred = input(sPrompt_Job_Moving_cred)
    num_Job_Moving_cred = num_entry_eval(sPrompt_Job_Moving_cred,input_num_Job_Moving_cred)
    input_num_Education_cred = input(sPrompt_Education_cred)
    num_Education_cred = num_entry_eval(sPrompt_Education_cred,input_num_Education_cred)
    input_num_Childcare_cred = input(sPrompt_Childcare_cred)
    num_Childcare_cred = num_entry_eval(sPrompt_Childcare_cred,input_num_Childcare_cred)
    input_num_Adoption_cred = input(sPrompt_Adoption_cred)
    num_Adoption_cred = num_entry_eval(sPrompt_Adoption_cred,input_num_Adoption_cred)
    input_num_Contrib_cred = input(sPrompt_Contrib_cred)
    num_Contrib_cred  = num_entry_eval(sPrompt_Contrib_cred,input_num_Contrib_cred)
    input_num_CasualtyTheft_cred = input(sPrompt_CasualtyTheft_cred)
    num_CasualtyTheft_cred = num_entry_eval(sPrompt_CasualtyTheft_cred,input_num_CasualtyTheft_cred)
    input_num_QualBus_cred = input(sPrompt_QualBus_cred)
    num_QualBus_cred = num_entry_eval(sPrompt_QualBus_cred,input_num_QualBus_cred)
    input_num_MedExp_cred = input(sPrompt_MedExp_cred)
    num_MedExp_cred = num_entry_eval(sPrompt_MedExp_cred,input_num_MedExp_cred)

    total_combined_credits: float = (num_Homebuyer_cred + num_Energy_cred +
        num_IRA_cred + num_Mortgage_cred + num_Student_cred + num_MedSavingsAcct_cred +
        num_Job_Moving_cred + num_Education_cred + num_Childcare_cred + num_SelfEmpHealthIns_cred +
        num_Adoption_cred + num_Contrib_cred + num_CasualtyTheft_cred + num_QualBus_cred + 
        num_MedExp_cred)

    adjusted_income = total_combined_income - total_combined_credits
 
    input(sFormEntryRecap_gen_stmt)

    print(sFormEntryRecap_inc +
    '\n'+ sPrompt_SSN_personal + str(num_SSN_personal) +          
    '\n'+ sPrompt_SSN_spouse + str(num_SSN_Spouse))
    for f in lst_num_SSN_dependents:
        ssn = str(f)
        print(sPrompt_SSN_dependents + ssn + '\n')
    print(sPrompt_Invstmnt_inc + money_val_str_output(num_Invstmnt_inc) +
    '\n' + sPrompt_StateLocalTax_inc + money_val_str_output(num_StateLocalTax_inc) +
    '\n' + sPrompt_Bus_inc + money_val_str_output(num_Bus_inc) +
    '\n' + sPrompt_Unemp_inc + money_val_str_output(num_Unemp_inc) +
    '\n' + sPrompt_Rental_inc + money_val_str_output(num_Rental_inc) +
    '\n' + sPrompt_SS_inc + money_val_str_output(num_SS_inc) +
    '\n' + sPrompt_Misc_inc + money_val_str_output(num_Misc_inc) +
    '\n' + sFormEntryRecap_cred +
    sPrompt_Homebuyer_cred + money_val_str_output(num_Homebuyer_cred) +
    '\n' + sPrompt_Energy_cred + money_val_str_output(num_Energy_cred) +
    '\n' + sPrompt_IRA_cred + money_val_str_output(num_IRA_cred) +
    '\n' + sPrompt_Mortgage_cred + money_val_str_output(num_Mortgage_cred) +
    '\n' + sPrompt_Student_cred + money_val_str_output(num_Student_cred) +
    '\n' + sPrompt_MedSavingsAcct_cred + money_val_str_output(num_MedSavingsAcct_cred) +
    '\n' + sPrompt_SelfEmpHealthIns_cred + money_val_str_output(num_SelfEmpHealthIns_cred) +
    '\n' + sPrompt_Job_Moving_cred + money_val_str_output(num_Job_Moving_cred) +
    '\n' + sPrompt_Education_cred + money_val_str_output(num_Education_cred) +
    '\n' + sPrompt_Childcare_cred + money_val_str_output(num_Childcare_cred) +
    '\n' + sPrompt_Adoption_cred + money_val_str_output(num_Adoption_cred) +
    '\n' + sPrompt_Contrib_cred + money_val_str_output(num_Contrib_cred) +
    '\n' + sPrompt_CasualtyTheft_cred + money_val_str_output(num_CasualtyTheft_cred) +
    '\n' + sPrompt_QualBus_cred + money_val_str_output(num_QualBus_cred) +
    '\n' + sPrompt_MedExp_cred + money_val_str_output(num_MedExp_cred))
    
    sAdjusted_income = money_val_str_output(adjusted_income)
    print('\nYour adjusted Gross income = ${}'.format(sAdjusted_income))
   
    if adjusted_income > int(0):
        if adjusted_income >= int(0) and adjusted_income < int(13350):
            income_tax_owed = round(adjusted_income**.1, 2)
        elif adjusted_income >= int(13350) and adjusted_income < int(50800):
            income_tax_owed = round(adjusted_income**.15, 2)
        elif adjusted_income >= int(50800) and adjusted_income < int(131200):
            income_tax_owed = round(adjusted_income**.25, 2)
        elif adjusted_income >= int(131200) and adjusted_income < int(212500):
            income_tax_owed = round(adjusted_income**.28, 2)
        elif adjusted_income >= int(212500) and adjusted_income < int(416700):
            income_tax_owed = round(adjusted_income**.33, 2)
        elif adjusted_income >= int(416700) and adjusted_income < int(444550):
            income_tax_owed = round(adjusted_income**.35, 2)
        else:
            income_tax_owed = round(adjusted_income**.396, 2)
        print('\nThis is your taxable income: ${}'.format(adjusted_income) +
                '\nYou owe us money!!! Send a check for ${}'.format(income_tax_owed))
    elif adjusted_income == int(0):
        print('You neither owe taxes nor will receive a tax refund.  Have a nice day!')
    else:
        print('You are eligible for a refund of ${}'.format(adjusted_income * -1))
        print(sPrompt_CheckOrDD)
        yn_check = input(sYNcheck)
        if str(yn_check) == 'N':
            print(sDDinfo)
            input_BankAcctNum = input(sPrompt_BankAcctNum) 
            num_BankAcctNum = is_number(input_BankAcctNum)
            input_BankRtgNum = input(sPrompt_BankRtgNum) 
            num_BankRtgNum = is_number(input_BankRtgNum)
        else: 
            print('You will receive your refund check by mail.')

    print('Thank your for using Forum Generator!')

main()





