##Address Book Program

import sys

filename = 'AddressBook.txt'

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
sBirthday = 'Birthday: '
sNickname = 'Nickname(s): '
sOccupation = 'Occupation: '
sCompany = 'Company: '
sAddMore = ('Your file has been updated.'
'\nIf you wish to add more contacts, type "Y" and press ENTER.'
'\nType "N" and press ENTER to stop and view your contact list.'
'\nOr, simply press ENTER to exit the program.' + lb)
lstTypes = ['H','h','W','w']

def homeVSwork(x,sInputVerbiage,sPrompt):
    while x not in lstTypes:
        x = input('Please enter a valid response.\n' + sPrompt)
    if x == 'H' or x == 'h':
        y = sInputVerbiage + ' (Home)'
    elif x == 'W' or x == 'w':
        y = sInputVerbiage + ' (Work)'
    return(y)

def storeInput(filename,enteredValues,cntNumEntries):
    if cntNumEntries == 1:
        f = open(filename,'w+')
    else:
        f = open(filename,'a')
    for i in enteredValues:
        f.write(i)
    f.close

def getInput(filename,read):
    fileOutput = open(filename,read)
    print(fileOutput.read())
    fileOutput.close()

def reqFld(x,sPrompt):
    while x == '':
        print('You must enter a value for this field.')
        x = input(sPrompt)
    return x

def Main():
    input(sWelcomePrompt)
    #Throw this all into a While loop for as long as the user wants to add more entries
    input_sAddMore = 'Y'
    cntAddition = 0
    while input_sAddMore == 'Y' or input_sAddMore == 'y':
        lb
        lb
        input_sName = reqFld(input(sName),sName)
        input_sPhone = input(sPhone)
        if input_sPhone != '':
            input_sPhoneType = input(sPhoneType)
            input_sPhone = homeVSwork(input_sPhoneType,input_sPhone,sPhoneType)         
        cntEmail = 1
        canEnterAdditionalEmail = True
        input_2nd_email = ''
        exists2ndEmail = False     
        while cntEmail <= 2:
            if canEnterAdditionalEmail is True:
                input_sEmail = input(sEmail + ' #{}: '.format(cntEmail))
            input_1st_email = ''
            if cntEmail == 1 and input_sEmail != '':
                input_1st_email = input_sEmail
                exists1stEmail = True
            elif cntEmail == 1 and input_sEmail == '':
                exists1stEmail = False
                canEnterAdditionalEmail = False 
            if exists1stEmail is True and cntEmail == 2:
                if input_sEmail != '':
                    input_sEmailType = input(sEmailType)      
                    input_2nd_email = homeVSwork(input_sEmailType,input_sEmail,sEmailType)
                if input_2nd_email != '':
                    input_sEmail = (' #1: ' + input_1st_email + lb + sEmail + ' #2: ' + input_2nd_email)
                    exists2ndEmail = True
            if exists1stEmail is True and (exists2ndEmail is False or input_2nd_email == ''):
                input_sEmail = input_1st_email + ':'
            cntEmail = cntEmail + 1 
        input_sAddress = input(sAddress)
        input_sBirthday = input(sBirthday)
        input_sNickname = input(sNickname)
        input_sOccupation = input(sOccupation)
        input_sCompany = input(sCompany)
        fileInput = (sName + input_sName + lb + sPhone + input_sPhone + lb +
            sEmail + input_sEmail + lb + sAddress + input_sAddress + lb +
            sBirthday + input_sBirthday + lb + sNickname + input_sNickname + lb +
            sOccupation + input_sOccupation + lb + sCompany + input_sCompany + lb +
            '-----------------------------------------------------------' + lb)
        if fileInput != '':
            cntAddition = cntAddition + 1
            storeInput(filename,fileInput,cntAddition)
        input_sAddMore = input(sAddMore)
    if input_sAddMore == 'N' or input_sAddMore == 'n':
        lb
        getInput(filename,'r')
Main()
