######################################## ALGO ONE ##############################################
# TODO: Print all the integers from 1 to 255.

def print_1_to_255():
    for i in range(256):
        print(i)

print_1_to_255()

######################################## ALGO TWO ###############################################
# TODO: Print integers from 0 to 255, and with each integer print the sum so far.

def print_ints_and_sum_0_to_255():
    sum = 0
    for i in range(256):
        sum += i
        print(i, sum)

print_ints_and_sum_0_to_255()

######################################## ALGO THREE ###############################################
# # TODO: Given an array, find and print its largest element.

def print_max_of_array(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    print(largest)

print_max_of_array([4,5,34,23,56,42])

######################################## ALGO FOUR ###############################################
# # TODO: Create an array with all the odd integers between 1 and 255 (inclusive).

def return_odds_array_1_to_255():
    odds = []
    for i in range(1, 256):
        if i % 2 != 0:
            odds.append(i)
    return odds

print(return_odds_array_1_to_255())

######################################## ALGO FIVE ##############################################
# # TODO: Given an array and a value Y, count and print the number of array values greater than Y.

def return_array_count_greater_thanY(arr, y):
    count = 0
    for i in arr:
        if i > y:
            count += 1
    print(count)

return_array_count_greater_thanY(return_odds_array_1_to_255(), 163)

######################################## ALGO SIX ##################################################
# # TODO: Given an array, print the max, min and average values for that array.

def printMaxMin_average_array_vals(arr):
    pass

######################################## ALGO SEVEN ################################################
# # TODO: Replace any negative array values with 'Dojo'.

# def swapStringFor_array_negative_vals(arr):
#     pass

######################################## ALGO EIGHT ################################################
# # TODO: Print all odd integers from 1 to 255.

# def print_odds_1_to_255():
#     pass

######################################## ALGO NINE #################################################
# # TODO: Iterate through a given array, printing each value.

# def print_array_vals(arr):
#     pass

######################################## ALGO TEN ##################################################
# # TODO: Analyze an array’s values and print the average

# def print_average_of_array(arr):
#     pass

######################################## ALGO ELEVEN ###############################################
# # TODO: Square each value in a given array, returning that same array with changed values

# def square_array_vals(arr):
#     pass

######################################## ALGO TWELVE ###############################################
# # TODO: Return the given array, after setting any negative values to zero.

# def zero_out_array_negative_vals(arr):
#     pass

######################################## ALGO THIRTEEN #############################################
# # TODO: Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.

# def shift_array_vals_left(arr):
#     pass