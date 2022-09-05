#RANDOM PASSWORD GENERATOR
import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
randigit1=chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
randigit2=chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
randcharacter1=chr(random.randint(34,152)) #Generate a random character (based on ASCII code)
randcharacter2=chr(random.randint(35,152)) #Generate a random character (based on ASCII code)


#Generate password using all the characters, in random order
password = uppercaseLetter1 + lowercaseLetter1 + uppercaseLetter2 + randigit1+ lowercaseLetter2 + randigit2 + randcharacter1 + randcharacter2
password = shuffle(password)

#Ouput
print(password)