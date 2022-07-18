import string 
# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""
lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits 
symbols = string.punctuation 
possibleCharacters = lettersLower + lettersUpper + numbers + symbols
runProgram = "yes"

# Define the function called encryptOrDecrypt
def encryptOrDecrypt():
  global shiftedPosition 
  if mode.lower() == 'encrypt': 
    shiftedPosition = initialPosition + key 
  elif mode.lower() == "decrypt": 
    shiftedPosition = initialPosition - key
  

# Define the function called wraparound
def wraparound(): 
  global shiftedPosition 
  if shiftedPosition >= len(possibleCharacters): 
    shiftedPosition = shiftedPosition - len(possibleCharacters)
  elif shiftedPosition < 0: 
    shiftedPosition = shiftedPosition + len(possibleCharacters)

# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters + "\n\nLet's get started!\n")

# Receive user input
initialMessage = input("What is your message? ")
key = int(input("What is the key? Choose a number from 0 to 93. "))
mode = input("Do you want to encrypt or decrypt? ")

# Encrypt or decrypt the message
for character in initialMessage:
  if character in possibleCharacters:
    initialPosition = possibleCharacters.find(character)
    encryptOrDecrypt() 
    wraparound() 

    shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
  else: 
    shiftedMessage = shiftedMessage + character

# Print the shifted message
if mode.lower() == "encrypt": 
  print("Your " + mode.lower() + "ed message is: " + shiftedMessage)
elif mode.lower() == "decrypt": 
  print("Your " + mode.lower() + "ed message is: " + shiftedMessage)
else: 
  print("Try again, and make sure you type either 'encrypt' or 'decrypt'.")
