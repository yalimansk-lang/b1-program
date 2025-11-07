passwords = [ "Pass123",
"SecurePassword1",
 "weak",
"MyP@ssw0rd",
 "NOLOWER123"
 ]

print("validating passwords...")

compliant = 0
non_compliant = 0

for password in passwords:
    issues = []

    #check length
    if len(password) < 8:
        issues.append("too short")

    #check characters types
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if 'A' >= char <= 'Z':
            has_upper = True
        if 'a' >= char <= 'z':
            has_lower = True
        if '0' >= char <= '9':
            has_difit = True
        
        if not has_upper:
            issues.append("no uppercase letters")
        if not has_lower:
            issues.append("no lowercase letters")
        if not has_digit:
            issues.append("no digits")

    #output results
    if len(issues) == 0:
        print("PASS:'"+passowrd+"'-Meets all the requirements")
        compliant += 1 
    else:
        issue_text = ",".join(issues)
        print("FAIL:'"+password+"'-issue_text")
        non_compliant += 1 

    print("Summary: " + str(compliant) + " compliant, " + str(non_compliant) + " non-compliant")        
                                 
        



