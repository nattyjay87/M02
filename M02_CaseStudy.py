'''
Nathan Johnson
M02_CaseStudy
This program will prompt the user to enter a students Last and First name, as well as the student's GPA. The program will then output
the student's full name and whether or not they made the dean's list, honor roll or neither.
'''


def main():
    while True:
        
        last_name = input("Enter the student's last name (enter 'ZZZ' to quit): ")

        
        if last_name == 'ZZZ':
            break

        
        first_name = input("Enter the student's first name: ")

        
        gpa = float(input("Enter the student's GPA: "))

        
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")

        
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")

        
        else:
            print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()
