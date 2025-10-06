
import re

def check_password_strength(password: str):
    """
    check password strength against basic policy rules.
    returns a list of issues found (empty if strong).
    """

    issues = []

    if len(password) < 8:
        issues.append("Password too short (minimum 8 characters).")

    if not re.search(r"[A-Z]", password):
        issues.append("Password should contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        issues.append("Password should contain at least one lowercase letter.")

    if not re.search(r"[0-9]", password):
        issues.append("Password should contain at least one digit.")

    if not re.search(r"[@$!%*?&]", password):
        issues.append("Password should contain at least one special character (@$!%*?&).")

    return issues

    #test
if __name__ == "__main__":
    test_pw = input("Enter a password to check: ")
    problems = check_password_strength(test_pw)

    if problems:
        print("🔑 Password Issues:")
        for p in problems:
            print(" -", p)
    else:
        print("✅ Strong password!")
