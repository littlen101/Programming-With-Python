#Instantiate variables for use later
sInitialPrompt = '\nPress ENTER to begin.'
sAdjListPrompt = '\nEnter 4 adjectives, separated by commas: '
sVerbListPrompt1 = 'Enter a past tense verb: '
sVerbListPrompt2 = 'Enter a present tense verb: '
sVerbListPrompt3 = 'Enter two -ing ending verbs, separated by a comma: '
sNounPrompt1 = 'Enter a singular noun: '
sNounPrompt2 = 'Enter a plural noun: '
sNounPrompt3 = 'Enter a type of liquid: '
sNounPrompt4 = 'Enter the name of a room in a house: '
sFinalPrompt = '\nAll done! Press Enter to see your Mad Lib Results!'



#Below int definitions will be used only if have time to count the number of entries entered in a comma separated list
#by the end user and re-prompt for additional, missing entries.
#intNumAdj = int(4)
#intNumNoun = int(3)
#intNumVerb = int(2)

def Main():
# Print introductory remarks to screen
    print('Mad Libs Project - Written by Travis Thomas'
          '\n\n\t *** Title: COPING WITH CHILDHOOD FEARS ***'
          '\n\nWelcome to Mad Libs!'
          '\n\nYou will be given a series of prompts for which to enter values.'
          '\nWhen you finish, your entries will be inserted into a pre-made paragraph.'
          '\nHopeully the results will be funny! Enjoy!')

    #Kickoff User Prompts
    KickoffPrompt = input(sInitialPrompt)

#Obtain user's adjective list and use input to define list variable
    sAdjsEntered = input(sAdjListPrompt)
    StrSplit_Adj = sAdjsEntered.split(',',4)
    lstAllAdjsEntered: List = StrSplit_Adj
    #cntlst = count.lstAdjsEntered #need to figure out this syntax

#Obtain user's mutiple verb entries, and form list for indexing later
    lstVerb1 = [input(sVerbListPrompt1)]

    lstVerb2 = [input(sVerbListPrompt2)]
    #Parse string variable into comma-separated list
    # StrSplit_slstVerb2 = slstVerb2.split(',',2)
    #Instantiate variable with new comma-separated list for readability
    # lstVerb2: List = StrSplit_slstVerb2

    slstVerb3 = input(sVerbListPrompt3)
    # Parse string variable into comma-separated list
    StrSplit_slstVerb3 = slstVerb3.split(',',2)
    #Instantiate variable with new comma-separated list for readability
    lstVerb3: List = StrSplit_slstVerb3

    #Place ALL verbs entered into 1 list
    lstAllVerbsEntered = lstVerb1 + lstVerb2 + lstVerb3

#Obtain user's mutiple noun entries, and form list for indexing later
    lstNoun1 = [input(sNounPrompt1)]
    lstNoun2 = [input(sNounPrompt2)]
    lstNoun3 = [input(sNounPrompt3)]
    lstNoun4 = [input(sNounPrompt4)]

    # Place ALL nouns entered into 1 list
    lstAllNounsEntered = lstNoun1 + lstNoun2 + lstNoun3 + lstNoun4

#test input structure. comment all below entries out from final output.
#    print('\t* lstAdjsEntered = ', lstAllAdjsEntered)
#    print('\t* lstAllVerbsEntered = ', lstAllVerbsEntered)
#    print('\t* lstAllNounsEntered = ', lstAllNounsEntered)

#Final Mad Libs Output
    FinalPrompt = input(sFinalPrompt)

#    sFinalOutPut: str = '\nWhen I was little, I was afraid of ' + lstAllNounsEntered[1] + '.'
    print('\nWhen I was little, I was afraid of {}.'.format(lstAllNounsEntered[1]),
        'I found them to be simply {}.'.format(lstAllAdjsEntered[0]),
        '\nNone of my{} classmates could understand, and they'.format(lstAllAdjsEntered[1]),
        lstAllVerbsEntered[0], 'about it constantly.\nBut what can you expect from{}'.format(lstAllAdjsEntered[1]),
        'people?\nNowadays, I cope by {}'.format(lstAllVerbsEntered[2]), 'loudly and{} {}'.format(lstAllVerbsEntered[3],
        lstAllNounsEntered[2]), 'all around my {}.'.format(lstAllNounsEntered[3]), '\nIt’s surprisingly '
        'therapeutic! You wouldn’t think it would work since it sounds\nso{}.'.format(lstAllAdjsEntered[2]),
        'I guess it just goes to show that even a(n){} {}'.format(lstAllAdjsEntered[3], lstAllNounsEntered[0]),
        'can {},'.format(lstAllVerbsEntered[1]), 'too!'
    )

Main()