while True: #use a while loop to simulate access control
    print('Please enter your name') #ask for name
    name = input() #register input to variable name
    if name != 'Joe': #if name is not equal to Joe
        continue #continue the while loop which will ask for name again
    print('Hello Joe, what is the password? (Hugh Travolta)') #name is Joe so ask for the password
    password = input() #register input to variable password
    if password == 'swordfish': #if password equal to swordfish
        break #break the loop
    print('Acess granted') #tell user access is granted
    