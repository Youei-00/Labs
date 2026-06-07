# ---------------------------------------------------------
# Name: Youssef Omer
# Course: CMPSC 472 (Spring 2026)
# Program: Decimal Base Converter
#
# Description:
# This program converts a decimal number into Binary,
# Octal, and Hexadecimal using the division method.
# ---------------------------------------------------------

def convertDecimal(decimalVal, destBase):
    """
    Converts a decimal number to another base using
    the division method.

    Returns a string containing the converted value,
    or 'error' if something goes wrong.
    """

    if decimalVal < 0 or destBase not in [2, 8, 16]:
        return "error"

    if decimalVal == 0:
        return "0"

    digits = "0123456789ABCDEF"
    result = ""

    tempValue = decimalVal

    while tempValue > 0:
        remainder = tempValue % destBase
        result = digits[remainder] + result
        tempValue = tempValue // destBase

    return result


def main():
    userInput = 0

    while userInput != -1:
        userInput = int(input("Enter a decimal number (0 - 2,000,000) or -1 to exit: "))

        while (userInput < -1) or (userInput > 2000000):
            userInput = int(input("Invalid input. Enter a value between 0 and 2,000,000 or -1 to exit: "))

        if userInput != -1:
            binaryValue = convertDecimal(userInput, 2)
            octalValue = convertDecimal(userInput, 8)
            hexValue = convertDecimal(userInput, 16)

            print("\nDecimal:", userInput)
            print("Binary :", binaryValue)
            print("Octal  :", octalValue)
            print("Hex    :", hexValue)
            print()


main()
