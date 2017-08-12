def main():

    answers_list = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

    student_file = open("student_test.txt", "r")

    student_list = []

    tally = 0

    index = 0

    for line_student in student_file:

        #You can do it like you have down below or alternatively, you can do it like this:
        #line_student = line_student.rstrip("\n")
        #Just remember when you use the .rstrip method that you need to save it to a variable, or after it has finished
        #it will simply revert back to what it was because you didn't save the new .rstrip string as anything
        student_list.append(line_student.rstrip("\n"))

    for line_answer in answers_list:
        if answers_list[index] == student_list[index]:
            tally += 1
        index += 1

    print("The total number of correct answers was ", tally, " out of 20.", sep='')

    if tally >= 15:
        print("Congratulations, you passed!")
    else:
        print("Unfortunately, you did not pass.")

main()