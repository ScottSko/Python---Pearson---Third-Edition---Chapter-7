def main():

    the_num = int(input("What is your number? "))

    list = [1, 2, 3, 4, 5]

    def larger_than(a_list, a_num):
        for num in a_list:
            if num > a_num:

                print(num)

    larger_than(list, the_num)

main()
