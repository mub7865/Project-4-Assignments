"""
Program: add2numbers
--------------------
Another python program to get some practice with
variables.  This program asks the user for two
integers and prints their sum.
"""


def main():
    num1: str = input("Enter the first number: ")
    num1: int = int(num1)
    num2: str = input("Enter the second number: ")
    num2: int = int(num2)
    sum: int = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

if __name__ == "__main__":    
    main()