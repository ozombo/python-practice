def spam(divideBy): # define the division function
    try:
        return 42 / divideBy # divide 42 by passed parameter
    except ZeroDivisionError: # if zero is passed
        print('Error: Invalid argument.') # print error due to division by 0

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))