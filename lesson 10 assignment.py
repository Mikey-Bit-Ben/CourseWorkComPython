def main():
    print("-" * 20)
    print("Welcome to the string replacement tool.")
    print("-" * 20)

    original_string = input("please enter a string: ")
    search_string = input("please enter the string to search for: ")
    print("Searching for the substring...")
    print("-" * 20)
    modify_string(original_string, search_string)

def modify_string(original_string, search_string):
    if find_substring(original_string, search_string) != -1:
        replacement_string = input("would you like to replace this part of the string (yes/no): ").strip().lower()
        if replacement_string == "yes":
            new_string = input("please enter the new part of the string: ")
            # replaces the portion the user tried to search with the new string that the user entered.
            modified_string = original_string.replace(search_string, new_string)
            print(f"The modified string is: {modified_string}")
            print("thank you for using the string replacement tool.")
            print("completed by, John Benites")
        if replacement_string == "no":
            print("No changes made to the original string.")
            print(f"unchanged string: {original_string}")
            print("thank you for using the string replacement tool.")
            print("completed by, John Benites")
        elif replacement_string != "yes" and replacement_string != "no":
            print("Invalid input. Please enter 'yes' or 'no'.")
            modify_string(original_string, search_string)        
#grabs the variables and checks if the search string is in the original string then it checks witth the .find() and will print out the specific part of the index.
def find_substring(original_string, search_string):
    index = original_string.find(search_string)
    if index != -1:
        print(f"The substring '{search_string}' was found at index {index}.")
        print("-" * 20)
    else:
        print(f"The substring '{search_string}' was not found in the original string.")
        return -1
    

if __name__ == "__main__":
    main()