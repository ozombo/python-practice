


sum_of_numbers = 0
average = 0

num_of_elements = input('\n Enter the number of elements you want to work with \n')
num_of_elements = int(num_of_elements)

for index in range(num_of_elements):
    user_num = input(f'Enter number {index + 1} : ')
    sum_of_numbers = sum_of_numbers + int(user_num)

print('The average of the numbers entered is : '  + str(sum_of_numbers/num_of_elements))
