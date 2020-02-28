

num_of_elements = input('\nEnter the number of elements you want to work with \n') # gets the input the user enters
num_of_elements = int(num_of_elements) # parse user's input from string to integer
my_arr = [] # declare an array to hold every number the user enters

for index in range(num_of_elements):
    user_num = input(f'Enter number {index + 1} : ')
    my_arr.append(int(user_num)) # append each number to the array

my_arr.sort(reverse = True) # sort array in descending order
print( 'The largest number is ' + str(my_arr[0])) # print out the largest number which is the 1st element of the sorted array