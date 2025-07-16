"""
Summary of task
"""
# Write a program that asks the user to enter a series of single-digit numbers with nothing
# separating them.
# The program should display the sum of all the single digit numbers in the
# string. For example, if the user enters 2514, the method should return 12, which is the sum
# of 2, 5, 1, and 4.

def get_string():
    """
    This function asks the user to enter in a string of single-digit numbers, 
    with nothing separating them:
    i.e: user_string = [123456789]
    Input: user_string:str
    Output: user_string:str
    """
    user_string = input("Enter a series of single-digit numbers with nothing separating them: ")
    return user_string

def get_sum(user_string=str):
    """
    This function get the sum of user_string from get_string above. 
    Input: user_string:str
    Output: sum_string:int, non_ints:list, good_ints:list
    """
    sum_string = 0
    non_ints = []
    good_ints = []

    for i in user_string:
        if i.isdigit():
            sum_string+=int(i)
            good_ints.append(i)
        elif not i.isdigit():
            non_ints.append(i)
    return sum_string, non_ints, good_ints

def print_sum(user_string, sum_string, non_ints, good_ints):
    """
    This function prints the values of: user_string, sum_string, good_ints, and non_ints.
    The function takes the length of non_ints, and good_ints
    and appropriately uses grammar for good/non-integer inputs.
    Input: user_string:str, sum_string:int, non_ints=list, good_ints:list
    Output: sum_string:int, non_ints:list, good_ints:list
    """
    sum_message = f"You entered {user_string}, and the sum is {sum_string}."
    print(sum_message)
    print("=" * len(sum_message))
    if non_ints:
        print(
            f"Please note that: {", ".join(non_ints)} "
            f"{'is' if len(non_ints)==1 else 'are'} "
            f"{'not a digit' if len(non_ints)==1 else 'not digits'}.\n"
            f"While: {", ".join(good_ints)} "
            f"{'is' if len(good_ints)==1 else 'are'} "
            f"{'not a digit' if len(good_ints)==1 else ' digits'}."
            )

def main():
    """
    Main Function
    """
    user_string = get_string()
    sum_string, non_ints, good_ints = get_sum(user_string)
    print_sum(user_string, sum_string, non_ints, good_ints)

if __name__ == '__main__':
    main()
