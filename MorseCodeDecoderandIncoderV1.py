# PROBLEM: Code will just fuckn skip some charecters that are obviously wrong when the string is complex
while True: 
    print("Welcome to my text to morse code translator!")
    print("Would you like to translate text to morse code, or from morse code to text?")
    TranslateOption = input("Please type 'to morse code' to translate to morse code, or please type 'to text' to translate morse code to text?   ")
    if TranslateOption == "to morse code":
        # Collects pre-translated text from user
        # FLAG: add a system which checks for incorrect puncuation and prints error, and restarts loop.
        print("*NOTE, SPECIAL CHARECTERS OTHER THAN ENGLISH PUNCUATION WILL RESULT IN AN ERROR")
        InitialText = input("Please enter the text you wish to translate into morse code:   ")
        # Makes InitialText upper case
        InitialText = str.upper(InitialText)
        MorseDict = {' ': ' / ', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}
        MorseList = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ', ', '.', '?', '/', '-', '(', ')']
    # Seperates initial text into list
        TempIndex = 0
        LtrList = []
        # Finds length of the InitialText so the while knows when to stop.
        StrLen = len(InitialText)
        # Appends each letter of the text into a list.
        while True:
            LtrList.append(InitialText[TempIndex])
            TempIndex = TempIndex + 1
            if TempIndex == StrLen:
                break
        ErrorNum = 0
        ErrorCheck = False
        for TempLtr in LtrList:
            TempNum = MorseList.count(TempLtr)
            if TempNum == 0:
                while True:
                    LtrList.remove(TempLtr)
                    ErrorNum = ErrorNum + 1
                    ErrorCheck = True
                    TempCheck = LtrList.count(TempLtr)
                    if TempCheck == 0:
                        break
        for TempLtr in LtrList:
            TempNum = MorseList.count(TempLtr)
            if TempNum == 0:
                while True:
                    LtrList.remove(TempLtr)
                    ErrorNum = ErrorNum + 1
                    ErrorCheck = True
                    TempCheck = LtrList.count(TempLtr)
                    if TempCheck == 0:
                        break
        if ErrorCheck == True:
            print("")
            print("ERROR: Found " + str(ErrorNum) + " non-supported charecters in text. Removed non-supported text.")
            print("*Note: due to unknown charecter morse output may not be the same as inputted.")
        MorseList = []
        print(LtrList)
        # Takes keys from the previous list and finds and appends values to a new list
        for TempLtr in LtrList:
            TempMorse = MorseDict[TempLtr]
            MorseList.append(TempMorse)
        # Condenses MorseList into a single string
        FinalMorse = ""
        for TempMorse in MorseList:
            FinalMorse = FinalMorse + " " + TempMorse
        print("")
        print("Here is your translated morse code:")
        print(FinalMorse)
        print("")
        print("Would you like to exit or go again?")
        BreakVar = input("Enter 'again' to go again, or type 'exit' to leave:   ")
        str.lower(BreakVar)
        if BreakVar == "again":
            print("Reseting Loop")
            print("___________________________")
            print(" ")
        elif BreakVar == "exit":
            break
        else:
            print("Did not recognize answer, restarting loop.")
    if TranslateOption == "to text":
        # FLAG: add failsafe to reset loop.
        # Collects user morse code and stores it in a var.
        print("*NOTE, PROGRAM ONLY ACCEPTS '.', '-', '/' AS FORMS OF MORSE CODE, INCLUDING SPACES. USING ANOTHER TYPE WILL RESULT IN AN ERROR")
        InitialMorse = input("Please enter your morse code that you wish to be translated:   ")
        TempIndex = -1
        InvMorseDict = {'/': ' ', '': '', ' ': ' ', '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',  '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')'}
        # Removes any spaces at the end of the morse.
        while True:
            if InitialMorse[TempIndex] != " ":
                break
            if InitialMorse[TempIndex] == " ":
                InitialMorse[TempIndex].replace(" ", "")
            TempIndex = TempIndex - 1
        TempIndex = 0
        while True:
            if InitialMorse[TempIndex] != " ":
                break
            if InitialMorse[TempIndex] == " ":
                InitialMorse[TempIndex].replace(" ", "")
            TempIndex = TempIndex + 1
        # seperates morse code into list
        MorseList = []
        MorseIndex = 0
        LtrList = []
        MorseList = list(InitialMorse.split(" "))
        for TempMorse in MorseList:
            LtrList.append(InvMorseDict[TempMorse])
        FinalStr = ""
        for TempLtr in LtrList:
            FinalStr = FinalStr + TempLtr
        print("")
        print("Your translated morse code is:   "+FinalStr)
        print("")
        print("Would you like to exit or go again?")
        BreakVar = input("Enter 'again' to go again, or type 'exit' to leave:   ")
        str.lower(BreakVar)
        if BreakVar == "again":
            print("Reseting Loop")
            print("___________________________")
            print(" ")
        elif BreakVar == "exit":
            break
        else:
            print("Did not recognize answer, restarting loop.")
            print("___________________________")
            print(" ")
        # FLAG: Add error function to failsafe in case user adds a non-morse letter or charecter.
        # FLAG: Maybe add a system that creates the dictionary regardless the type of morse used (eg. instead of dots and dashes, x's and y's)
    else:
        print("")
        print("Sorry, I didn't recognise that, please try again.")
        print("")
        print("________")
        print("")