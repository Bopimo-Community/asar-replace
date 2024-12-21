import os
print("WARNING! THIS PROGRAM IS IN DEVELOPMENT. WE ARE NOT RESPONSIBLE FOR ANY DAMAGES THAT MAY OCCUR TO FILES OR YOUR BOPIMO ACCOUNT")
path = input("path to app.asar (vanilla): ")
mod = input("path to modded app.asar: ")
print(path)
print(mod)
input("Continue? ")
os.system("copy " + mod + " " + path + "/Y")
