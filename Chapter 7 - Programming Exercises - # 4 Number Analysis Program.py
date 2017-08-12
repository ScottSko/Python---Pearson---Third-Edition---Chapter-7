def main():

    list = []

    total = 0

    size = 5

    for x in range(size):

        value = int(input("What is the number you would like to enter? "))

        list.append(value)

        total += value

    highest = max(list)
    lowest = min(list)

    average = total / size

    print(list)

    print("The highest value in the list is", highest)
    print("The lowest value in the list is", lowest)
    print("The total of the numbers in the list is", total)
    print("The average of the numbers in the list is", average)

main()