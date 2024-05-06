#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given integer.

    Function Description:
    ----------------------
    This function calculates the factorial of a given non-negative integer n.
    The factorial of a non-negative integer n, denoted as n!, is the product
    of all positive integers less than or equal to n.

    Parameters:
    -----------
    n : int
        The non-negative integer for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input integer n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)

f = factorial(num)
print(f)
