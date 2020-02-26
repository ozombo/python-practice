print('Hi, What is your name') # say hi and ask user for name 
myName = input() # append inputed name to variable myName
print('It\'s good to meet you ' + myName) # say hello properly including the inputed name
print('The length of your name is ' + str(len(myName))) # count characters in user's name
print('How old are you?') # ask user for age
myAge = input() # append inputed age to myAge variable
print('You will be ' + str(int(myAge) + 1) + ' years old in a year') # calculate user's age in a year