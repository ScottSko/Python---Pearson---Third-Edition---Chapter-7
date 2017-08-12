def main():

    index = 0
    months = 12
    total = 0

    list = []

    for x in range(months):
        value = int(input("What was the total rainfall for the month? "))

        list.append(value)

        total += value

    print("The total amount of rainfall was", total)
    print("The average rainfall was", total / 12)
    print("The lowest amount of rainfall during the year was", min(list))
    print("The highest amount of rainfall during the year was", max(list))

main()