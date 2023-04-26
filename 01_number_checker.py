# checks that users enter a float / integer that is more than zero
def num_check(question, error, num_type):
    while True:

        try:
            response = num_type(input(question))

            # check response is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


my_int = num_check("Enter an integer: ",
                   "Please enter an integer that is more than zero",
                   int)
print(f'You chose {my_int}')
print()

my_float = num_check("Enter a float: ",
                     "Please enter a float that is more than zero",
                     float)
print(f'You chose {my_float}')
print()