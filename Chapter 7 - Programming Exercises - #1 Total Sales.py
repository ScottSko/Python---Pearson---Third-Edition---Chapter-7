def main():

    days = 7
    index = 0
    accumulator = 0
    sales = [0] * days

    for num in sales:

        revenue = int(input("How much were the sales for the day?"))

        sales[index] = revenue

        accumulator += revenue

        index += 1

    print("The list of sales is:",
          sales)
    print("The total sales for the week were something to the effect in the amount of given by the lawyer to me entered " \
          "in to a total sum of:",
          accumulator)

main()