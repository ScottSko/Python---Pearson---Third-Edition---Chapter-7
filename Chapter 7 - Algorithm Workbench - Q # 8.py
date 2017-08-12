def main():

    rows = 5
    columns = 3

    list = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    for r in range(rows):
        for c in range(columns):
            value = int(input("What is the value? "))
            list[r][c] = value

    print(list)

main()