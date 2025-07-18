
def main():
    studentsInfo = {
	"John": {
        'ID': 1,
        'GPA': 3.5,
        'Credits-completed': 89,
        'grades': [95, 40, 98, 79, 100]
    },
	"Jane": {
        'ID': 2,
        'GPA': 3.8,
        'Credits-completed': 92,
        'grades': [88, 95]
    }
}
   
    print("student information", studentsInfo)
    #\n skips a line
    print("\nlist of students:")
    for name in studentsInfo.keys():
        print(name) 
    print("\nAccessing student information:")
    print("Name\tID\tGPA\tCredits-completed\tGrades")
    for name, info in studentsInfo.items():
        print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['Credits-completed']}\t\t\t{info['grades']}")
    print("\nJane has dropped out, removing from dictionary")
    studentsInfo.pop("Jane", None)
    print(studentsInfo)
    print("\naccesesing GPA for remaining students")
    for name, info in studentsInfo.items():
        print(f"{name}s GPA is '{info['GPA']}")     
    print("\nstudents have graduated, clearing the registry")
    studentsInfo.clear()
    print("Registry cleared:", studentsInfo)
    print("completed by, John Benites")

    
if __name__ == "__main__":
    main()
