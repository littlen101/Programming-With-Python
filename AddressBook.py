##Address Book Program

import sys

sWelcomePrompt = ('Welcome to Little Black Book! This program will allow you to add'
'\nan unlimited number contacts and the associated information for each.'
'\nIf you do not want to enter anything for a given field, just press ENTER'
'\nor follow field-specific prompts.'
'\n\n**Press ENTER to begin entering your contact information!**\n')

lb = '\n'
sName = 'Name: '
sPhone = 'Phone Number: '
sPhoneType = 'Enter "H" if this is a HOME number or W if this is a WORK number: '
sEmail = 'Email Address'
sEmailType = 'Enter "H" if this is a HOME email or W if this is a WORK email: '
sAddress = 'Physicial Address: '
sBirthday = 'Brithday: '
sNickname = 'Nickname(s): '
sOccupation = 'Occupation: '
sCompany = 'Company: '
sAddMore = ('Your file has been updated.'
'\nIf you wish to add more contacts, enter "Y".'
'\nPress "N" to stop and view your contact list.'
'\nPress ENTER to exit the program: ')
lstTypes = ['H','h','W','w']

def homeVSwork(x,sInputVerbiage,sPrompt):
    while x not in lstTypes:
        x = input('Please enter a valid response.\n' + sPrompt)
    if x == 'H' or x == 'h':
        y = sInputVerbiage + ' (Home)'
    elif x == 'W' or x == 'w':
        y = sInputVerbiage + ' (Work)'
    return(y)

def Main():
    input_welcome = input(sWelcomePrompt)
    #Throw this all into a While loop for as long as the user wants to add more entries
    input_sAddMore = 'Y'
    cntAddition = 0
    while input_sAddMore == 'Y' or input_sAddMore == 'y':
        lb
        lb
        input_sName = input(sName)
        input_sPhone = input(sPhone)
        if input_sPhone != '':
            input_sPhoneType = input(sPhoneType)
            input_sPhone = homeVSwork(input_sPhoneType,input_sPhone,sPhoneType)         
        cntEmail = 1      
        while cntEmail <= 2:
            input_sEmail = input(sEmail + ' #{}: '.format(cntEmail))
            if cntEmail == 1:
                input_1st_email = input_sEmail        
            cntEmail = cntEmail + 1
            input_2nd_email = ''
            exists2ndEmail = False
            if input_sEmail != '' and cntEmail == 3:
                input_sEmailType = input(sEmailType)      
                input_2nd_email = homeVSwork(input_sEmailType,input_sEmail,sEmailType)
                if input_2nd_email != '':
                    input_sEmail = str(' #1: ' + input_1st_email + lb + sEmail + ' #2: ' + input_2nd_email)
                    exists2ndEmail = True
            if exists2ndEmail is False or input_2nd_email == '':
                input_sEmail = input_1st_email + ':'
        input_sAddress = input(sAddress)
        input_sBirthday = input(sBirthday)
        input_sNickname = input(sNickname)
        input_sOccupation = input(sOccupation)
        input_sCompany = input(sCompany)
        fileInput = (sName + input_sName + lb + sPhone + input_sPhone + lb +
            sEmail + input_sEmail + lb + sAddress + input_sAddress + lb +
            sBirthday + input_sBirthday + lb + sNickname + input_sNickname + lb +
            sOccupation + input_sOccupation + lb + sCompany + input_sCompany + lb)
        if fileInput != '':
            cntAddition = cntAddition + 1
            if cntAddition == 1:
                f = open('AddressBook.txt','w+')
            else:
                f = open('AddressBook.txt','a')
            for i in fileInput:
                f.write(i)
            f.close
        input_sAddMore = input(sAddMore)
    if input_sAddMore == 'N' or input_sAddMore == 'n':
        r = open('AddressBook.txt','r')
        content = r.read()
        r.close()
        print(content)
Main()
