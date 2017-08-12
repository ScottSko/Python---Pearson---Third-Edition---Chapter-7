def main():

    student_test = open("student_test.txt", 'w')

    counter = 0

    test_number = 0

    while counter < 20:
        test_number += 1
        print(test_number, ".", sep='', end='')
        response = input(" Enter your answer: ")
        response = response + "\n"
        counter += 1
        student_test.write(response)

    print("Thank you. Your test results will be graded shortly.")

    #numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    #numbers.insert(3, 9)
    #numbers.sort()
    #numbers.reverse()
    #print(numbers[-4:])

    #def test():
    #    return "hello"

    #message = test()
    #print(message)

    #names = ["John", "Matt", "Tony"]

    #search = names[1:2]
    #search2 = names[55]
    #print(search)
    #print(search2)

    #names.append("Wendy")

    #print(search)

    #numbers = [[1, 2],
    #          [10, 20],
    #          [100, 200],
    #          [1000, 2000]]
    #print(numbers)

main()