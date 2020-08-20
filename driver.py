import requests

if __name__ == '__main__':
    dept = input("Enter code for the department offering the class (ex: MATH, CMSC): ")
    number = input("Enter the class number (ex: 216, 101): ")
    class_name = dept + number
    print(class_name)