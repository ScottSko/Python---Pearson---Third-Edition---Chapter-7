def main():

    rows_ = 3
    columns_ = 3

    lo_shu = [[4, 9, 2],
              [3, 5, 7],
              [8, 1, 6]]

    test_square = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

    for x in range(rows_):
        for y in range(columns_):
            print("What value would you like to place in row ", x, ", column ", y, "?", sep='')
            square_value = int(input())
            test_square[x][y] = square_value

    #index = 0

    #total = 0

    #tracker = 0

    def lo_shu_checker(a_list):

        tracker = 0
        index = 0
        total = 0
        rows = 3
        columns = 3

        for r in range(rows):
            for c in range(columns):
                total += a_list[r][c]

                if total == 15:
                    tracker += 1
                    total = 0

        for c in range(columns):
            for r in range(rows):
                total += a_list[r][c]

                if total == 15:
                    tracker += 1
                    total = 0

        for num in a_list:
            value = a_list[index][index]
            total += value
            index += 1

            if total == 15:
                tracker += 1
                total = 0

        index = 0

        for num in a_list:
            value_2 = a_list[2 - index][index]
            total += value_2
            index += 1

            if total == 15:
                tracker += 1
                total = 0

        return tracker

    final = lo_shu_checker(test_square)

    print(test_square)

    #print(tracker)
    #print(total)

    if final == 8:
        print("Congratulations, this is a Lo Shu Magic Square!")
    else:
        print("This is not a Lo Shu Magic Square.")

main()
