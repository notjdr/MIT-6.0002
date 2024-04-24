###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

# from ps1_partition.py import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================


# Problem 1
def load_cows():
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    path = 'ps1_cow_data.txt'
    file = open(path, 'r')  
    lst_pre = file.readlines() # output. ['Maggie,3\n', 'Herman,7\n', 'Betsy,9\n', 'Oreo,6\n', 'Moo Moo,3\n', 'Milkshake,2\n', 'Millie,5\n', 'Lola,2\n', 'Florence,2\n', 'Henrietta,9']
    lst_pre_len = len(lst_pre)

    lst_post = [lst_pre[x].split(",") for x in range(lst_pre_len)]
    lst_names = [lst_pre[x][ 0 : lst_pre[x].index(",")] for x in range(lst_pre_len)] # output. ['Maggie','Herman','Betsy','Oreo','Moo Moo','Milkshake','Millie','Lola','Florence','Henrietta']
    lst_values = [int(lst_post[x][1].replace('\n','')) for x in range(lst_pre_len)]
    
    cows = dict(zip(lst_names, lst_values)) 
    # output. [['Maggie': 3], ['Herman': 7], ...]. # NOTE: ensure that names are string's and values are int's.
    
    return cows

# Problem 2
def greedy_cow_transport(cows=load_cows(), limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    arr_names = list(load_cows().keys())
    arr_values = list(load_cows().values())

    lst = list(zip(arr_names,arr_values))
    lst = sorted(lst, key = lambda cow: cow[1], reverse=True)
    arr_names, arr_values = zip(*lst)

    arr_values = [[arr_values[x], 1] for x in range(len(arr_values))]

    maxUnits = limit
    space = []

    def greedy():
        result = []
        totalCost = 0.0
        for i in range(len(arr_values)):
            if (totalCost+arr_values[i][0]) <= maxUnits and arr_values[i][1]:
                result.append(arr_names[i])
                arr_values[i][1] = 0
                totalCost += arr_values[i][0]   
        return result
    
    def available_checker():
        total = 0
        for i in range(len(arr_values)):
            total += arr_values[i][1]
        return bool(total)

    while available_checker():
        space.append(greedy())
     
    return space

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips Use the given get_partitions function in ps1_partition.py to help you!  
    2. Select the allocation that minimizes the number of trips without making any trip that does not obey the weight limitation Does not mutate the given dictionary of cows.
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


if __name__ == '__main__':
    print(load_cows())
    print(greedy_cow_transport())