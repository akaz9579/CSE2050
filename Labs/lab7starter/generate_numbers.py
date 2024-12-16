# This program generates a list of numbers and writes them to a file.
import random

##### Generate list of numbers #####
n = 1000 # Max is 2000 due to memory constraints on the gradescope
         # containers that run your submissions
L_rand = [random.randint(0, n) for i in range(n)]

L_sorted = sorted(L_rand)
#use sorted to get best time for bubble, and see if there is an 
# alg that is o(n) in sorted and  o(n^2) reversed

# use to find selection, should have same time as rand 

L_reversed = L_sorted[::-1]
# use reverse to get worst time for quick, then we can 
# compare to merge will see if alg b or d slows down. slower is quick



##### Create file to write to #####
f = open(f"/Users/amankazi/CSE2050/Labs/lab7starter/numbers.txt", "w")

##### Write numbers to file #####
#for item in L_rand:
#    f.write(str(item))
#    f.write(" ")


#f.write("\n")

#for item in L_sorted:
#    f.write(str(item))
#    f.write(" ")
#f.write("\n")

for item in L_reversed:
    f.write(str(item))
    f.write(" ")


#### Close the file ####
f.close()


