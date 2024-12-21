import os
print("WARNING! THIS PROGRAM IS IN DEVELOPMENT. WE ARE NOT RESPONSIBLE FOR ANY DAMAGES THAT MAY OCCUR TO FILES OR YOUR BOPIMO ACCOUNT")
path = input("path to app.asar: ")
backup = input("path to backup vanilla app.asar to: ")
print(path)
print(backup)
os.system("copy " + path + " " + backup + r"\app.asar.backup")
# os.system("xcopy " + path + "%appdata%\Bopimo!\Client")
