import random

def main():

    index = 0

    list = []

    for num in range(9):
        value = random.randint(0, 9)
        list.append(value)

    for num in list:
        print("The value of the", index + 1, "slot is:", list[index])

        index += 1

main()

