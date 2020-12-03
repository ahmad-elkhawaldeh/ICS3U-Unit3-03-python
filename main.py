# !/user/bin/env python3

# created by: Ahmad El-khawaldeh
# created on: Nov 2020
#  this program checks if u got the right random number

import random

random_number = random.randint(1, 3)


def main():
    # this function checks if the random number is 5

    # input
    user_input = int(input("enter a number from 1 to 9:"))
 
    #process
   if user_input == random_number:
       #output
       print("")
       print(" Correct   ")
   else:
     print(" incorrect ") 

if __name__ == "__main__":
   main()  
