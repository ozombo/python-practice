def odd_even():
   print('Enter a number')
   num = int(input())
   if (num % 2) == 0:
        print("{0} is Even".format(num))
   else:
        print("{0} is Odd".format(num))
    
odd_even()