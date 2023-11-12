#First 3 lines in this example form together the function
#Start with "def" to create a name for the desired function
#Then create the code for the function
def print_10():
    for i in range(10):
        print(i + 1)

#This command calls to the function to be initiated
print_10()

'''
Functies kunnen handig zijn als je de gemaakte code vaker wilt gebruiken.
In plaats van de gehele code opnieuw te moeten typen, kun je eenvoudig enkel de functie aanroepen.
'''

#Another example
#devider() is the name for this function and can also be initiated by calling this name
#This function creates a dividing line
def devider():
    print()
    print("---------------------")
    print()

devider()
print("Dit is mijn eerste code")
devider()
print("Dit is mijn tweede code")
devider()
print("Dit is mijn derde code")
devider()

#Another example
def ongeveer_pi():
    return 3.1415

print(ongeveer_pi())

devider()

#The a and b between (), we call "parameters".
#We can give values to these parameters. These values we call "arguments".
def tel_op(a,b):
    return a + b

totaal = tel_op(1,1)

print(totaal)

devider()

#Example
def info(naam, leeftijd, in_dienst):
    if in_dienst:
        text_1 = "en nog altijd in dienst van onze firma."
    else:
        text_1 = "en niet meer bij ons in dienst."

    uitvoer = f"Beste {naam}, u bent {leeftijd} jaar {text_1}"
    return uitvoer

print(info("Harry", 54, True))
print(info("Magda", 73, False))

devider()

#It is possible to immediately assign arguments to the parameters
def tel_op(a=1,b=2):
    return a + b

print(tel_op())

devider()

#When you assign a different argument with the below statement, it will replace the first argument
print(tel_op(20))

devider()

