# !/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Nov. 25, 2022
# This program uses a for loop and an
# if statement to print integers ranging
# from 1000 to 2000.

# initializes the counter
counter = 1000


# function determines the integer amount
def main():
    # loops from 1000 - 2000
    for counter in range(1000, 2001):
        # makes the loop in a row of 5
        if counter % 5 == 0:
            print(" ")
        print(counter, end=" ")


if __name__ == "__main__":
    main()
