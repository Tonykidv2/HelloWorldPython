winning_lotto_numbers = (5, 17, 31, 12, 6)

# Python crashes here tuples are immutable. They cant change after being set
# winning_lotto_numbers[0] = 21

my_list = []
my_list.append("some data")

# convert list to tuple with tuple() function
my_tuple = tuple(my_list)

print(my_tuple)