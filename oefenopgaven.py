from helper import devider

devider()

#Function with 1 parameter
#The function will double the parameter and give the result once the function is called.
def mijn_functie(mijn_int):
    return mijn_int * 2

devider()

#Function with 1 parameter
#The function will go through the list (parameter), and returns the sum of all elements in the list once the function is called.
def mijn_functie2(mijn_lijst):
    totaal = 0
    for nr in mijn_lijst:
        totaal += nr
    return totaal

devider()

#Function with 2 parameters
#The function will return the letters of string1 with the conditions that those letters are also present in string2.
def mijn_functie3(string1, string2):
    uitvoer = ""
    for c in string1:
        if c in string2:
            uitvoer += c
    return uitvoer

devider()
