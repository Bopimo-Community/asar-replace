import os
print("WARNING! THIS PROGRAM IS IN DEVELOPMENT. WE ARE NOT RESPONSIBLE FOR ANY DAMAGES THAT MAY OCCUR TO FILES OR YOUR BOPIMO ACCOUNT")
path = input("path to app.asar (vanilla): ")
backup = input("path to backup app.asar to: ")
print(path)
print(backup)
input("Continue? ")
os.system("copy " + path + " " + backup + r"\app.asar.backup")
