###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################

def fizz_buzz(start, finish):
    """ Program prints numbers from start to finish, inclusive (both start and finish 
    should be printed). Replace multiples of 3 with "fizz", multiples of 5 with "buzz",
      and multiples of both with "fizzbuzz"."""

    # Make sure you add a docstring to this function.

    for x in range(start, finish + 1):
       # hasThree = '3' in str(x)

        if (x % 3 == 0 or '3' in str(x)) and (x % 5 == 0 or '5' in str(x)):
            print("fizzbuzz")
        elif x % 3 == 0 or '3' in str(x):
            print("fizz")
        elif x % 5 == 0 or '5' in str(x):
            print("buzz")
        else: 
            print(x)
    return

fizz_buzz(5,100)
