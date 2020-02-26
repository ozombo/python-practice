# boolean and conditions in python
print('What is your name') # ask for users name
person = input() # assign name to person
single = True # define single as True

if single: # if single is true then print a message saying the Name you chose is single
    print(person + ' is single')
else: # else say person is not single
        print(person + 'is not single')


employed = False

if employed:
    print(person + ' is employed')
else:
    print(person + ' is unemployed')


if single and employed: # if user is single and employed
    print(person + ' is single and employed')
else:
    print(person + ' is single and unemployed')

if single or employed: #single or employed
    print(person + ' is single or employed')
else:
    print(person + ' is not single and isunemployed')