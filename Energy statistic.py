"""
COMP.CS.100 Programming 1
Student ID: 050015443
Name: Janina Montonen
E-mail: janina.montonen@tuni.fi
Project 2: Energy statistic

This program prints a histogram of the energy consumption values entered by the
user, which can be used to illustrate different energy consumption amounts.

In this program I have made my own codes and functions and inputted them to a
prepared code template given by a lecturer. I have marked the codes and
functions, which have been given ready at the template, with comments.
"""


def main():
    # These three commands below, have been given by a lecturer.
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    user_inputs()


def user_inputs():
    """
    Ables a user to input different energy values until the user inputs
    nothing. If the user inputs negative values, function prints an error
    message. If the user inputs more than 0 values this function leads to
    another function, else it prints a comment.
    """

    input_data = []
    while True:
        value = (input("Enter energy consumption (kWh): "))
        if value == "":
            break
        else:
            right_value = int(value)
            if right_value < 0:
                print(f"You entered: {right_value}. "
                      f"Enter non-negative numbers only!")
            else:
                input_data.append(right_value)

    if len(input_data) == 0:
        print("Nothing to print. Done.")
    else:
        create_help_list(input_data)


def create_help_list(input_data):
    """
    Creates a list, which has information about how many values the user has
    inputted for different consumption categories.

    :param input_data: list, a list that includes values which the user has
    inputted.
    """

    calculate_list = [0, 0]
    for the_value_to_be_examined in input_data:
        class_number = 1
        while True:
            smallest_value = 10 ** class_number // 100 * 10
            largest_value = 10 ** class_number - 1
            if smallest_value <= the_value_to_be_examined <= largest_value:
                # In the if structure below, calculate_list is lengthened, if
                # otherwise the list would be too short for a new value.
                if len(calculate_list) - 1 < class_number:
                    calculate_list = calculate_list + \
                                     (((class_number + 1) -
                                       len(calculate_list)) * [0])
                calculate_list[class_number] += 1
                break
            class_number += 1

    largest_class_number = len(calculate_list) - 1
    c_number = 1
    count = calculate_list[c_number]
    amount = len(calculate_list)
    print_histogram(c_number, count, calculate_list, largest_class_number,
                    amount)


def class_minimum_value(class_number):
    """
    Calculates the minimum value of every energy consumption class.

    :param class_number: int, the class number of energy consumption
    :return: the minimum value
    """

    min_value = 10 ** class_number // 100 * 10
    return min_value


def class_maximum_value(class_number):
    """
    Calculates the maximum value of every energy consumption class.

    :param class_number: int, the class number of energy consumption
    :return: the maximum value
    """

    max_value = 10 ** class_number - 1
    return max_value


# This function has been given by the lecturer but the comments and the latest
# if structure, have been made by me.
def print_histogram(class_number, count, calculate_list, largest_class_number,
                    amount):
    """
    Prints a histogram of the correct shape.

    :param class_number: int, the class number of energy consumption which is
    1 at the beginning, but it increases in every loop
    :param count: int, the value in index that is class_number
    :param calculate_list: list, the list that was created in previous
    function
    :param largest_class_number: int, the last index in calculate_list
    :param amount: int, the length of the calculate_list
    """

    for num in range(1, amount):
        min_value = class_minimum_value(class_number)
        max_value = class_maximum_value(class_number)
        range_string = f"{min_value}-{max_value}"
        largest_width = 2 * largest_class_number + 1
        print(f"{range_string:>{largest_width}}: {'*' * count}")
        class_number += 1
        # This is in the if form, because otherwise in the last loop, index
        # would go out of range.
        if class_number <= len(calculate_list) - 1:
            count = calculate_list[class_number]


if __name__ == "__main__":
    main()