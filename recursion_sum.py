
def find_sum(arr):
    '''
         using divide and conquer technique to recursively find the sum of a list of numbers
    '''
    result = 0
    if len(arr) == 1 :
        result = arr[0]
    else:        
        result = arr.pop() + find_sum(arr)
    return result
    
def count_list(arr):
    
    '''
        recursive counter 
    '''
    
    count = 0
    if len(arr) == 0:
        return count
    else:
        arr.pop()
        count = count + count_list(arr) + 1
    
    return count 


arr = list(range(1,11)) # generates a sequence of natural numbers

print(f'The sum of the array is {find_sum(arr)}') # expected answer is 55