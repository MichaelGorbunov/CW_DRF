import random

from random import randint as rnd

if __name__ == "__main__":

    step_next = 3
    step_actual = 0
    step_len = 1

    toys_varians = ["o", "O", "@", "0"]

    rows = int(input("Rows: "))
    freq = int(input("Frequency: "))

    for i in range(0, rows):

        br_row = "/" + "*" * (2 * step_len - 1) + "\\"
        if (len(br_row) > 1):
            for x in range(1, len(br_row) - 2):
                if (br_row[x + 1] == br_row[x - 1] and \
                        rnd(1, 10) <= freq):
                    br_row = br_row[:x] + toys_varians[rnd(0, 3)] + br_row[x + 1:]
        print(" " * (rows - step_len) + br_row)

        step_actual += 1
        step_len += 1

        if (step_actual == step_next):
            step_len -= 2
            step_actual = 0
            step_next += 1

    print("_" * (rows - 1) + "|||" + "_" * (rows - 1))