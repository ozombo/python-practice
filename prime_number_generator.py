"""
    This code uses the seive of erastosthenes algorithm to generate N prime numbers,
    where N is the number of prime numbers

    check out https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""



def generate_numbers(limit):

    """
    @param:
        limit - length of the sequence of natural numbers to be generated
    
    @return:
        list_of_numbers - list of the generated sequence

    """
    if limit <= 0:
        raise ValueError('Invalid limit specified')
    
    list_of_numbers = list()
    for i in range(1,limit+1):
        list_of_numbers.append(False)
        
    return list_of_numbers



def get_multiples(number,number_set):  

    """
    get./
    @param:
        number - multiple
        number_set - list of numbers

    @return:
        number_set - a list of booleans that indicates multiples
                     (referenced by index) is a multiple of number
    """  
    
    for multiple, state in enumerate(number_set,1):
        if multiple == number:
            continue
        elif multiple % number == 0  and state is False:
           number_set[multiple-1] = True 
        else:
           continue
    return number_set

def next_prime(old_prime,values):

    """
        returns the next prime using as the first
        non-multiple obtained in the within the set of multiples

        @param:
            old_prime - prime number
            values - set of booleans that mark the multiples of 'old_prime'
    """
    
    for multiple,state in enumerate(values,1):
        if multiple > old_prime and state is False:
            return multiple       
        

def seive(number_set):

    """
        seive of eratosthenes
        prints out the prime number
    """    
    max_prime = 2
    values = number_set
    
    while max_prime is not None:
        print(max_prime, end=' ')
        values = get_multiples(max_prime,values)
        max_prime = next_prime(max_prime,values)
        




if __name__ == "__main__":
    
   a = generate_numbers(0)
       
   seive(a)

   
   
        
    
    
    
    
    
    
    