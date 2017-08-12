def main():
    
    list = [1] * 10

    def total_list(value_list):

        total = 0

        for num in value_list:
            total += num

        return total

    total_complete = total_list(list)

    print("The total is:", total_complete)

main()