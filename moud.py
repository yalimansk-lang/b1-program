import string
import random

#check min lenght

def check_min_length(password, min_len=8):
    return len(password)>=min_len

#check upper cases

def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)

#check for lower case char
def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)

#check for digits
def has_digit(password):
    return any(char in string.digits for char in password) 


def has_special_char(password):
    return any(char in string.punctuation for char in password)

def validate_password(password):
    results = {
        'min_length': check_min_length(password),
        'has_uppercase': has_uppercase(password),
        'has_lowercase': has_lowercase(password),
        'has_digit': has_digit(password),
        'has_special': has_special_char(password)
        }
    
    #overall valide password 
    results['is_valid'] = all(results.values())

    return results

# User Interface and Testing
def main():
    print("=" * 50)
    print("PASSWORD STRENGTH VALIDATOR")
    print("=" * 50)
    print("\nPassword Requirements:")
    print("Minimum 8 characters")
    print("At least one uppercase letter")
    print("At least one lowercase letter")
    print("At least one digit")
    print("At least one special character (!@#$%^&* etc.)")

#get password from user
password=input("Enter password:")

#validate password
results=validate_password(password)

# Display results using 'print()' and f-strings for formatted output
print("\n" + "=" * 50)
print("VALIDATION RESULTS")
print("=" * 50)

# Individual criteria results
#Using' 'and' 'forclearvisualfeedback
check_symbol="\u2713" if results['min_length']else" "
print(f"{check_symbol} Minimum length (8+ chars): {results['min_length']}")

check_symbol="\u2713"if results['has_lowercase']else" "
print(f"{check_symbol} Contains lowercase: {results['has_lowercase']}")

check_symbol="\u2713"if results['has_digit']else" "
print(f"{check_symbol} Contains digit: {results['has_digit']}")

check_symbol="\u2713"if results['has_special']else" "
print(f"{check_symbol} Contains special char: {results['has_special']}")

# Overall result
print("\n" + "=" * 50)
if results['is_valid']:
    print(" PASSWORD IS STRONG!")
else:
    print(" PASSWORD IS WEAK - Please address failed requirements") 
    print("=" * 50)

    # Run the program only when the script is executed directly 
if __name__ == "__main__":
    main()




    