def main():

    #For this program, you can do it one of two ways. If you initialize the second list to be the same length
    #as the first list, by creating it and multiplying by the constant, then you can use the
    #numbers2[index] = num
    #code to populate the second, by placing it in the loop and reading from the first.
    #alternatively, you can intilialize the second list as empty, and then use the
    #numbers2.append(num)
    #code to populate it. The key difference is that the first method works if you know the length
    #the second method works regardless of the whether or not you know the length

    index = 0

    constant = 100

    numbers1 = [2] * constant

    #numbers2 = [0] * constant
    numbers2 = []

    print("Before copying, the second list is:", numbers2)

    for num in numbers1:
        #numbers2[index] = num
        numbers2.append(num)

        index += 1

    print("After copying, the second list is:", numbers2)

main()