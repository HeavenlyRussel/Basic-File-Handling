from os import system

system("cls")

print("Hello and welcome to my program where even if you exit this program, your data is stored")
print("\n")

file = open("Data Storage.txt", 'r')
lastData = file.read()

if lastData == "":
    pass
else:
    print(f"Last data entered is {lastData}")
    
file.close()

print("\n")
print("Now enter a string for example: ", end = "")
exampleNumber = input()

file = open("Practice Data Storage.txt", 'w')
file.write(exampleNumber)
file.close()
