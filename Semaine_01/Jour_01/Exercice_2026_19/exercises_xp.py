#Exercise 1: Hello World

print("Hello World\n"*4, end="")

#Exercise 2: Some Math

resultat = (9**3)*8
print(resultat)

#Exercise 3: What is the output?


# Ma devinette : False
print(5 < 3)  

# Ma devinette : True
print(3 == 3)  

# Ma devinette : False
print(3 == "3")  

# Ma devinette : Erreur
#print("3" > 3) # (Ignorer l'erreur pour l'instant)

# Ma devinette : False
print("Hello" == "hello")  

#Exercise 4: Your Computer Brand

computer_brand = "hp"
print(f"I have a <{computer_brand}> computer.") 

#Exercise 5: Your Information
name = "Amos_Age"
age = 29
shoe_size = 43
print(f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}.")

#Exercise 6: A & B
a = 13
b = 8
if a > b:
    print("Hello world")

#Exercise 7: Odd or Even

number = int(input("Saisissez un nombre: "))
if number % 2 == 0:
    print(f"{number} est un nombre pair.")
else:
    print(f"{number} est un nombre impair.")

#Exercise 8: What’s Your Name?

name = input("Entrez votre nom? ")
if name == "Amos_Age":
    print(f"Hello twin {name}!")
else:    print("Hello stranger!")

#Exercise 9: Tall Enough To Ride A Roller Coaster?
height = int(input("Entrez votre taille en cm: "))
if height >= 145:
    print("Desolé, vous êtes trop grand pour utiliser cette attraction!")
else:   print("S'il vous plaît, grandissez un peu encore avant de venir cette attraction!")
