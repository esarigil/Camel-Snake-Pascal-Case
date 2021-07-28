def pascalize(inputSt):
    result = inputSt.replace('_',' ').title() #It removes the "_" and adds a space and capitalizes the first letter of the words after it.
    result = result.replace(' ','')  #removes spaces
    print(result)
    return result

def depascalize(inputSt):
    tempSt = [inputSt[0].lower()] #Converts the first letter to lowercase.
    for c in inputSt[1:]: #From the 2nd letter;
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): #Checking until it finds capital letters.
            tempSt.append('_')  #Adding '_' to the end of the word.
            tempSt.append(c.lower())
        else:
            tempSt.append(c)
    print(''.join(tempSt))
    return ''.join(tempSt)


def camelize(inputSt):
    tempSt = ''
    tempSt += inputSt[0].lower() #Converts the first letter to lowercase.
    for i in range(1, len(inputSt)): #It checks all the letters in the text.
        if (inputSt[i] == ' '):#finds the spaces
            tempSt += inputSt[i + 1].upper() #Capitalizes the first letter after a space
            i += 1  #Increasing the value of i by 1
        elif(inputSt[i - 1] != ' '):
            tempSt += inputSt[i]
    print(tempSt)
    return tempSt

def is_pascalize(inputSt): #It checks according to pascal case rules.
    return inputSt != inputSt.upper() and inputSt != inputSt.upper() and "_" not in inputSt and " " not in inputSt
    #It checks if the initials of the words are capitalized and if there are "_" and spaces in between.


def is_camelcase(inputSt): #It checks according to camel case rules.
    return inputSt != inputSt.lower() and inputSt != inputSt.upper() and "_" not in inputSt and inputSt[0] not in inputSt.upper() and " " not in inputSt
    #It checks whether the first word is lowercase and the other words are uppercase and whether there are "_" and spaces in between.


def is_snakecase(inputSt): #It checks according to snake case rules.
    return inputSt == inputSt.lower() and inputSt == inputSt.lower() and "_" in inputSt and " " not in inputSt
    #It checks whether the initials of the words are lowercase and whether there are "_" and spaces in between.
