import re

def check_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None  # \W is any non-alphanumeric character, including _

    # Feedback messages
    feedback = []

    if length_criteria:
        feedback.append("✔ Password length is good (8 or more characters).")
    else:
        feedback.append("✘ Password is too short (less than 8 characters).")

    if uppercase_criteria:
        feedback.append("✔ Contains uppercase letters.")
    else:
        feedback.append("✘ Missing uppercase letters.")

    if lowercase_criteria:
        feedback.append("✔ Contains lowercase letters.")
    else:
        feedback.append("✘ Missing lowercase letters.")

    if number_criteria:
        feedback.append("✔ Contains numbers.")
    else:
        feedback.append("✘ Missing numbers.")

    if special_char_criteria:
        feedback.append("✔ Contains special characters.")
    else:
        feedback.append("✘ Missing special characters.")

    # Determine password strength
    strength = 0
    if length_criteria: strength += 1
    if uppercase_criteria: strength += 1
    if lowercase_criteria: strength += 1
    if number_criteria: strength += 1
    if special_char_criteria: strength += 1

    # Output the feedback
    print("\n".join(feedback))

    # Password strength evaluation
    if strength == 5:
        print("\nPassword Strength: Strong")
    elif 3 <= strength < 5:
        print("\nPassword Strength: Medium")
    else:
        print("\nPassword Strength: Weak")


def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ")
    check_password_strength(password)


if __name__ == "__main__":
    main()
