# Creator: Lusemar Oliveira 
# Description: Project 2 - Time to Retire
# Date: 09/30/2020 
# Class: COP1000
 
# This is where we invoke the Class and the function 
from datetime import date
today = date.today()

# This function will Output a formatted header
def outputWelcomeMessage():
  welcomeMessage = "This Program will Calculate How Long It Will Be Until Retirement\n"
  print(len(welcomeMessage) * "." + "\n")
  print(welcomeMessage)
  print(len(welcomeMessage) * "." + "\n\n")

# This function will calculate How Long It Will Be Until Retirement
def calculateUntilRetirement(AGE):
  workLeft = 65 - AGE
  retirementYear = today.year + workLeft
  return (workLeft, retirementYear)

# This function will determinate what message will according with the range
def outputMessage(workLeft, retirementYear):
  print()
  if workLeft < 5:
    almostThere = ", you are almost there"
  elif workLeft > 5 and workLeft < 15:
    almostThere = ", you are not too far"
  else:
    almostThere = ", much work remained to be done"
  print("\nHello", NAME,", There will be", workLeft,"years left until you are eligible to retire in", str(retirementYear), almostThere, ".\n")

# Here is where we call the function
outputWelcomeMessage()

# Here is where we get the input from the user and store into a constant
NAME = input("Please Enter Your Name: ")
AGE = int(input("Please Enter Your Age: "))

# Here is where we call the function
workLeft, retirementYear = calculateUntilRetirement(AGE)
outputMessage(workLeft, retirementYear)