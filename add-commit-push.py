import os
import sys

print("testing")
numOfArgs = len(sys.argv)
print("Total Arguments Passed: ", numOfArgs)
message = "Update files"
if numOfArgs == 3:
    if sys.argv[1] == "-m":
      print("Number of Args = 3 and p2 == -m")
    message = sys.argv[2]

print(message)



print("Add Commit Push")
print("\ngit status")
os.system("git status")

#w3c schools code.
print("Do you want continue with add commit push? (y):")
confirm = input()
if confirm != "y":
    print("Canceling ", confirm)
    quit()

print("\ngit add -A")
os.system("git add -A")
print('\ngit commit -m "Update files"')
os.system('git commit -m "Update files"')
print("\ngit push")
os.system("git push")
