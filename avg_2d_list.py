#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program calculates average of all numbers in a 2D list.

import random


def avg_of_numbers(passed_in_2D_list):
    # this function calculates the average of all elements in 2D array.

    # variables
    avg_list = 0

    for row_value in passed_in_2D_list:
        total = 0
        for single_element in row_value:
            total += single_element
        avg_list += (total/len(row_value))

    return (round(avg_list, 2))


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = int(input("How many rows would you like: "))
    columns = int(input("How many columns would you like: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 10)
            temp_column.append(a_random_number)
            print("{0}, ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    average = avg_of_numbers(a_2d_list)
    print("The average of all the numbers is: {0} ".format(average))


if __name__ == "__main__":
    main()
