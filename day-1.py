#for each item in num_list, divide by 3, round down, and subrtact 2. Append the new number to a list
#return the sum on all the numbers. 
# What is the sum of the fuel requirements for all of the modules on your spacecraft?

import urllib.request


#Helper functions:
def make_dataset(filename):
    """Reads txt file and create a list of nums for our dataset"""

    #initiate and empty list
    dataset = []

    #read text file
    f = open(filename, "r")

    for num in f:
        num = num.rstrip()
        dataset.append(num)

    return dataset

#Main function:
def calculate_fuel():
    """Calculate fuel needed for each num in the list"""

    #create dataset with helper function
    dataset = make_dataset('day-1.txt')

    #New list keeps fuel needed
    fuel_needed = []

    for num in dataset: 
        num = (int(num) // 3) - 2
        fuel_needed.append(num)

    total_fuel = sum(fuel_needed)

    return total_fuel

#Print main function 
print(calculate_fuel())