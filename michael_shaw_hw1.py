#!/usr/bin/env python3
import sys
import re

# Print correct pin message
def correct_pin():
    """
        prints pin is ocrrect if user pin input equals
        stored_user_pin
        user_pin == stored_user_pin
    """
    print ("Your PIN is correct: ")
    print ("")
    
# Checking fuction
def check_pin():
    """
        Function stores in what would usually be a database the users pin
        Also, the if statements check conditions such as:
            Pin length
            Pin is only 4 characters long
            Pin is has only integer type characters
            If Pin has been entered to many times exit(1) and print message
            If Pin is correct displays correct message by calling correct_pin() fucntion
            If/When an incorrect entry is made, an error message is displayed and 
                incorrect_count is incremented and user us prompted to input PIN again.
    """
    # Argument list
    stored_user_pin = {"user":"1234"}
    # Count variable initilization to zero
    incorrect_count = 0

    # Welcome user and prompt for PIN number
    print ("Welcome user! ")
    user_pin = input("Please enter your PIN number: ")
    print ("")

    # If user input is equal to arg list stored_user_pin at user position
    #   Then, call correct_pin() fuction
    if (user_pin == stored_user_pin["user"]):
       correct_pin()
    
    # While loop with conditional if statments for error checking
    # While loop has error attempt limits set to 3 tries, if tries
    #   hits the three mark card is held and program exits
    while(user_pin != stored_user_pin["user"]):
        
        # Check if user input is chars from 0 through 9 and does not equal the correct Pin length.
        #   If not print error message and increment incorrect_count.
        if (not re.match("^[0-9]*$", user_pin) and (len(user_pin) != 4)):
            print ("Invalid PIN character and length. Correct format is: <9876> ")
            incorrect_count += 1
            print ("")
            user_pin = input("Please enter your pin number: ")
        
        # If Pin length does not equal 4, print error message and increment incorrect_count.
        elif  (len(user_pin) != 4):
            print ("Invalid PIN length. Correct format is: <9876> ")
            incorrect_count += 1
            print("")
            user_pin = input("Please enter your pin number: ")

        # Check if user input is chars from 0 through 9, if not print message and increment incorrect_count
        elif (not re.match("^[0-9]*$", user_pin)):
            print ("Invalid PIN character. Correct format is: <9876> ")
            incorrect_count += 1
            print ("")
            user_pin = input("Please enter your pin number: ")

        # If user pin is integer type and correct length, but not correct PIN, prints error message
        #   and increments incorrect count
        elif (user_pin != stored_user_pin["user"]):
            print ("Your PIN is incorrect: ")
            incorrect_count += 1
            print ("")
            user_pin = input("Please enter your pin number: ")
        
        # If user enters incorrectly too many times the message is displayed card blocked and program exits.
        if (incorrect_count == 3):
            print("")
            print("Too many tries:")
            print ("Your bank card is blocked!")
            print ("")
            exit(1)
        # If pin is correct before incorrect_count = 3 tries, correct_pin fucntion is called and displayes
        #   appropiate message
        if (user_pin == stored_user_pin["user"]):
            correct_pin()
            break

# Main function
def main():
    """
    Main calls the check user pin function
    check_pin()
    """
    # Call checking fucntion
    check_pin()

    pass

if __name__== "__main__":
    #call main
    main()

    exit(0)
