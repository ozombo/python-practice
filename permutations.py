# A Python program to print all  
# permutations of given length 
from itertools import permutations 
  
# Get all permutations of length 2 
# and length 2 
perm = permutations([13, 4, 2], 2) 
  
# Print the obtained permutations 
for i in list(perm): 
    print (i)