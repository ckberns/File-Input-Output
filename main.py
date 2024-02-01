"""
Program: file_input_output.py
Author: Brandon Kerns
Last Date Modified: 11/3/23
The purpose of this program is create three separate functions that will perform actions to a file. The first function
will append text to the entered file. The second function will accept a student name as an argument, prompt the user
to input as many test scores as they would like, and store the information within a tuple. Finally, the third function
will read each line of the file and print these lines individually in the output console.
"""


# Create a function used to prompt a student to enter their full name and as many test scores as they would like.
def get_student_info():
    """
    This function will prompt a student to enter their name and any amount of test scores. The input will then be
    converted to a tuple.
    :return: nothing is returned from this function. This function is only used for passing entered information to the
    write_to_file() function.
    """
    student_name = input("Please enter your first and last name: ")
    # Create an empty list used to store the values of student's entered test scores.
    test_scores = []
    # Set a value that will be used to exit the loop once the user has finished entering their scores.
    sentinel = "F"
    # Execute a loop for the student to enter the scores of their tests.
    while True:
        try:
            score_input = input("Please enter your test scores one at a time, or press \'F\' to finish entering: ")
            if score_input.upper() != sentinel:
                # If the entered test score is within the accepted range, append the entered score to the empty list.
                if 0 <= float(score_input) <= 100:
                    score_input = float(score_input)
                    test_scores.append(score_input)
                else:
                    raise ValueError("Invalid input. Your score must be a numeric value!")
            else:
                break
        # Prompt the user if the score entered is out of range.
        except ValueError:
            print("Your score must be between 0 and 100!")
    # Take the entered values and use them to create a tuple containing the student information.
    name_and_scores = {tuple(test_scores): student_name}
    # Call the write_to_file(*args) function, passing the student info as arbitrary arguments.
    write_to_file(name_and_scores)


# Create a function that will accept user input from the first function and write that info to a blank file.
def write_to_file(*args):
    """
    This function will be used to write the information entered in the get_student_info() function to a file titled
    student_info.txt
    :param args: will be the student's name and test scores entered from the initial function.
    :return: nothing is returned because this function is only used to write the information to a file.
    """
    # Open the blank file that will be used to store the gathered information.
    with open("student_info.txt", "w") as file:
        # Create variables for the information that is to be iterated over.
        for student_info in args:
            # Extract the data from the get_student_info() function and format the values on their own lines.
            for key, value in student_info.items():
                file.write(f"Student Name: {value}\n")
                file.write("Test Scores: ")
                # Create a separate variable for the individual test scores.
                scores = ", ".join(map(str, key))
                file.write(scores + "\n")
                # Close the file after the information has been written to it.
                file.close()


# Create a function that will be used to read the information that is printed to a blank file named student_info.txt.
def read_from_file():
    """
    This function will be used to read the contents of the student_info.txt that has been populated with the entered
    student information.
    :return: nothing is returned from this function since it will only be used to print the contents of the created file
    """
    # Open the file that is to be read by the program.
    with open("student_info.txt", "r") as read_file:
        # Create a variable that will allow the read content to be printed.
        content = read_file. read()
        print(content)


if __name__ == "__main__":
    # Use the open() function, followed by the close() function to ensure the file is blank before program is ran.
    open("student_info.txt", "w").close()
    # Call the function that will be used to gather the student's name and test scores.
    get_student_info()
    # Call the function that will be used to print out the student's information.
    read_from_file()
