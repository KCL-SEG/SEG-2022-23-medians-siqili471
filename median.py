"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def median():
    while True:
        try:
            print("Enter a list of numbers separated by commas: ")
            numbers = [float(value) for value in input().split(",")]
            if len(numbers) == 0:
                return 0
            elif len(numbers) % 2 == 0:
                return (numbers[int(len(numbers)/2 -1)] + numbers[int(len(numbers)/2)]) / 2
            elif len(numbers) % 2 != 0:
                return numbers[int(len(numbers) // 2)]
        except ValueError:
            print("Some input could not be converted to a number!")

        else:
            break