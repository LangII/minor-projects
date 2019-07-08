
import string



numbers = string.digits
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
specials = string.punctuation

email, password = '', ''
e_valid, p_valid = False, False

intro_conditions = """
CREATE AN ACCOUNT WITH A VALID EMAIL AND PASSWORD

EMAIL AND PASSWORD VALIDATION CONDITIONS ARE...
    - email must contain an '@' character
    - email must have only lowercase, uppercase, or numbers left of the '@' character
    - password must be at least 10 characters long
    - password must contain at least 1 lowercase, 1 uppercase, and 1 number character
    - password must not contain any of the following characters:  ''', '"', ':', or ';'
"""



def inputSetEmailPassword():
    """
    output: Set value to global variables 'email' and 'password' with user input.
    """
    global email, password

    print(intro_conditions)
    email = input("email:    ")
    password = input("password: ")



def validateEmail():
    """
    output: Verify that 'email' meets validation criteria.  If conditions are met return True,
            else return False.
    """

    # First validation...  'email' needs to have an '@'.
    if '@' not in email:  return False

    # Second validation...  'local' (left of '@') of 'email' needs to only contain letters or
    # numbers.
    local = email[:email.index('@')]
    alphanumeric = lowercase + uppercase + numbers
    valid = False
    for l in local:
        for a in alphanumeric:
            if l == a:
                valid = True
                break
        if not valid:  return False

    # If 'email' passes previous validations then return True.
    return True



def validatePassword():
    """
    output: Verify that 'password' meets validation criteria.  If conditions are met return True,
            else return False.
    """

    # First validation...  'password' needs to be at least 10 char long.
    if len(password) < 10:  return False

    # Second validation...  'password' needs to have at least 1 lowercase char, 1 uppercase char,
    # and 1 number char.
    low_valid, upp_valid, num_valid = False, False, False
    for l in password:
        for low in lowercase:
            if l == low:  low_valid = True
        for upp in uppercase:
            if l == upp:  upp_valid = True
        for num in numbers:
            if l == num:  num_valid = True
    if not low_valid or not upp_valid or not num_valid:  return False

    # Third validation...  'password' can not contain the char ''', '"', ':', or ';'.
    for l in password:
        if l == "'" or l == '"' or l == ':' or l == ';':  return False

    # If 'password' passes previous validations then return True.
    return True



########################################
#####   \/   FUNCTION CALLS   \/   #####
########################################



# In a while-loop to continuously request user to submit 'email' and 'password' until user submits
# a valid 'email' and valid 'password'.
while not e_valid or not p_valid:

    inputSetEmailPassword()

    e_valid = validateEmail()
    p_valid = validatePassword()

    if not e_valid or not p_valid:  print("\nvalidation conditions not met...")

print("\nemail and password submitted are valid...  you deserve a cookie")
