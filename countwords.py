
word = 'I love writing code, I used to work with javascript but now I am loving python more! Do you code in python'
word_array = word.split(' ') # split string into array by passing empty space as delimiter ' '
word_count = word_array.__len__() # use __len__ to get the number of words

for index in range(word_count):
    print(f'{index} => {word_array[index]}')


print(f'There are {word_count} characters in the defined string. ') #count lenght of string