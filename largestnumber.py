

num_of_elements = input('\nEnter the number of elements you want to work with \n')
num_of_elements = int(num_of_elements)
my_arr = []

for index in range(num_of_elements):
    user_num = input(f'Enter number {index + 1} : ')
    my_arr.append(int(user_num))

my_arr.sort(reverse = True)
print(my_arr[0])