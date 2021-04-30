




""" STRUCTURED ENGLISH
create a list to store 24 number (float)
capture user's input 24 times
each time we capture the users input, we append the number to the list
sort the list ascending, then splice the items starting at index
once we have all numbers inputed in the list, we sum them up and divide by 24
output a message to the user
The program displays the number of grades
The average grade
The percentage of grades that are above the avergae grade
end
"""


"""
# main():
    enter code Testscores = input("Enter 24 student grades on a final exam seperated by commas:")
    listScores = scores.split(",")`enter code here`
    determine_grade(listScores)
    calc_average(listScores)

# determine_grade(grades):
    for num in grades:
        if int(num) >= 90 and int(num) <= 100:
            print("A")
        elif int(num) >=80 and int(num) <= 89:
            print("B")
        elif int(num) >=70 and int(num) <= 79:
            print("C")
        elif int(num) >=60 and int(num) <= 69:
            print("D")
        else:
            print("F")


# calc_average(grades):
    total = 
    for num in grades:
        total += int(num)
    average = total / 24
    print(average)

# show_letters(values):
main()
"""

def main():
    scores = input("Enter 24 exam scores separated by commas: ")
    return [int(num) for num in scores.split(",")]


def determine_grade(num):
    if 90 <= num <= 100:
        letter_grade = "A"
    elif 80 <= num <= 89:
        letter_grade = "B"
    elif 70 <= num <= 79:
        letter_grade = "C"
    elif 60 <= num <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


def calc_average(grades):
    average = sum(grades) / len(grades)
    grade = determine_grade(average)
    print("The average is: {:.1f} which is {}".format(average, grade))


def show_letters(num, letter_grade):
    print("{:.1f} is {}\n".format(num, letter_grade))


lst = main()
for n in lst:
    show_letters(n, determine_grade(n))
calc_average(lst)

def above_average(results, average_score):
    above_average_no=0
    for  Test_score in results:
        if Test_score > average_score:
            above_average_no = above_average_no + 1
            print(" the above average score is ", above_average_no)
    return above_average_no

