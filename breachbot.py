#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm BreachBot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since Facebook Data Breach!")




#Introduces breach
print("Would you like to learn about the Facebook Data Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains details of breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(A) breach details, (B) organization's response, (C) I would like to hear your reflection") 
  topic = input()
  
  if topic.lower() == "a":
    print("It involved Facebook, 533 million users and an unnamed intruder. Personal information including phone numbers, full names, locations, some email addresses, and other details from user profiles were leaked.The intruders had scraped the data by exploiting a vulnerability in a now-defunct feature of the platform that allowed users to find each other by phone numbers.")
  
  elif topic.lower() == "b":
    print("Facebook found and fixed the issue that caused the breach to make sure the same route can no longer be used to scrape that data.")
  
  elif topic.lower() == "c":
    break
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?") 
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(A) Whether or not you agree with the organization's response, (B) My reaction, (C) My advice, (D) None") 
  topic = input()
  
  if topic.lower() == "a":
    print("It relates to confidentiality in the CIA Triad. Hackers gained access to user profiles in Facebook through a vulnerability, and had access to data meant to be private.")
  
  elif topic.lower() == "b":
    print("We agree with the organization's response because they managed to resolve the problem and make sure that the attackers cannot take the same path to perform a data breach again.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by changing their passwords, credit card information, phone numbers to make sure that these information cannot be used by attackers.")
    
  elif topic.lower() == "d": 
    break 
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation


print("\nWould you like to hear some advice on how to better protect yourself?")
total = input() 
if total.lower() == "yes":
  print("See if your data has been in a data breach, have secure password and be careful of phishing emails")

print("Thanks for chatting with me, and I hope you learned something new!")
