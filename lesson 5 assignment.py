import random
# This program will take in grades from the user and store them in a list
def main():
    grade = []
    while True:
        get_grade = input("please enter a grade or -1 to stop: ")
        get_grade = int(get_grade)
        if get_grade == -1:
            break
        else:
            grade.append(get_grade)

    print("Grades entered:", grade)
    return grade
# this will remove the lowest grade from the list
# it will return the updated list of grades
def lowest(grade):
    print("removing the lowest grade. ")
    lowest_grade = min(grade)
    lowest_index = grade.index(lowest_grade)
    grade.pop(lowest_index)
    return grade
# this will remove a random grade from the list
# it will return the removed grade
def random_remove(grade):
    print("Randomly removing a grade.")
    if grade:
        random_index = random.randint(0, len(grade) - 1)
        removed_grade = grade.pop(random_index)
        print(f"Removed grade: {removed_grade}")
        return removed_grade  # Return the removed grade
    return None
# this will edit a grade in the list the user will imput a number to edit from the list 1 to what ever the length of the list is
# it will then ask for the new grade and update the list
def edit(grades):
    print("Edit a grade")
    #if user doesn't input any grades, it will return an empty list
    if not grades:
        print("No grades to edit.")
        return grades
    print("Current grades:")
    for i, grade in enumerate(grades, start=1):
        print(f"{i}: {grade}")
        #this will let my program run without errors if the user doesn't input any grades
    try:
        index = int(input(f"Enter the number (1 to {len(grades)}) of the grade to edit: ")) - 1
        if 0 <= index < len(grades):
            new_grade = int(input("Enter the new grade: "))
            grades[index] = new_grade
            print("Updated grades:", grades)
        else:
            print("please enter a valid number between 1 and", len(grades))
            return edit(grades)
            #this will handle any non-integer inputs and return the prompt to put in a number
    except ValueError:
        print("Please enter a valid number.")
        return edit(grades)
    else:
        return grades
def sortingandreversing(grades):
    print("Sorting and reversing the grades.")
    grades.sort()
    print("Sorted grades:", grades)
    grades.reverse()
    print("Reversed grades:", grades)
    return grades    
def gradetotalavarage(grades):
    total = sum(grades)
    average = total / len(grades)
    print("Total:", total, "Average:", average)
    return total, average



grades = main()
updated_grades = lowest(grades)
print(updated_grades)
removed_grade = random_remove(updated_grades)
print(updated_grades)
edit(updated_grades)
sortingandreversing(updated_grades)
gradetotalavarage(updated_grades)
print("completed by, John Benites")