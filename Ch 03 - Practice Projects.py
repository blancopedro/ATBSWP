# The Collatz Squence
# Collazt sequence. Every number is possible to be reduce to 1. If is odd or even.
# Odd


# Collatz function

def collatz (number):

    index = 0

# Check if the number is equal or not to 1 in order to tell the user
    if number == 1:
        print("Please, introduce a new number differente than 1")

#
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            index += 1
            print(str(number) + " : " + str(index))
        else:
            number = number * 3 + 1
            index += 1
            print(str(number) + str(index))

number = int(input("Please, insert a number"))
collatz(number)