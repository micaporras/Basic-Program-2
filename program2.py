# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

password = input("Password: ")
pass_length = len(password)
criteria_a = any(pass_length >= 16 for character in password)
criteria_b = any(character in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and 'abcdefghijklmnopqrstuvwxyz' for character in password)
criteria_c = any(character in '0123456789' for character in password) 
criteria_d = any(character in '!@#$%^&*()_+' for character in password)

if criteria_a == True and criteria_b == True and criteria_c == True and criteria_d == True:
    print("Valid Password")
else:
    print("Invalid Password")
    if criteria_a != True:
        print("Your password must be greater than 15 letters")
    if criteria_b != True:
        print("Your password must have at least one capital letter")
    if criteria_c != True:
        print("Your password must have at least one number")
    if criteria_d != True:
        print("Your password must have at least one special character")

print("Thank you!")