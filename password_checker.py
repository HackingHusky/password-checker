import re
import string
import random

# ------------------------------
# Password Complexity Checker
# ------------------------------

def check_password_complexity(password):
    
    criteria = {
        "length": len(password) >= 12,
        "lowercase": any(c.islower() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special_char": any(c in string.punctuation for c in password)
    }
    
    feedback = []
    
    if not criteria["length"]:
        feedback.append("- Password must be at least 12 characters long.")
    if not criteria["lowercase"]:
        feedback.append("- Must contain at least one lowercase letter.")
    if not criteria["uppercase"]:
        feedback.append("- Must contain at least one uppercase letter.")
    if not criteria["digit"]:
        feedback.append("- Must contain at least one digit.")
    if not criteria["special_char"]:
        feedback.append("- Must contain at least one special character.")

    if all(criteria.values()):
        return "Strong Password!", []
    else:
        return "Password does not meet requirements. Please follow the criteria below:", feedback


# ------------------------------
# Compliant Password Generator
# ------------------------------

def gen_pw(length=14):
    # Avoid ambiguous characters
    lowercase = ''.join(c for c in string.ascii_lowercase if c not in "l")
    uppercase = ''.join(c for c in string.ascii_uppercase if c not in "IO")
    digits = ''.join(c for c in string.digits if c not in "0")
    
    # Safer punctuation set
    safe_specials = "!@#$%^&*()-_=+[]{};:,.<>/?"

    # Ensure at least one of each category
    required = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(safe_specials)
    ]

    # Fill the rest
    all_chars = lowercase + uppercase + digits + safe_specials
    remaining = [random.choice(all_chars) for _ in range(length - len(required))]

    password_list = required + remaining
    random.shuffle(password_list)

    return ''.join(password_list)


# ------------------------------
# Main Program Loop
# ------------------------------

if __name__ == "__main__":
    while True:
        print("\n--- Password Tool ---")
        print("1. Check a password")
        print("2. Generate a compliant password")
        print("3. Exit")

        choice = input("\nChoose an option (1, 2, or 3): ").strip()

        if choice == "1":
            user_pw = input("\nEnter the password you want to check: ")
            strength_message, feedback_list = check_password_complexity(user_pw)

            print(f"\nPassword Strength: {strength_message}")
            if feedback_list:
                print("\nFeedback:")
                for item in feedback_list:
                    print(item)
            else:
                print("Your password meets all recommended criteria.")

        elif choice == "2":
            generated = gen_pw(14)
            print(f"\nGenerated Compliant Password: {generated}")

            strength_message, feedback_list = check_password_complexity(generated)
            print(f"\nPassword Strength: {strength_message}")

            if feedback_list:
                print("\nFeedback:")
                for item in feedback_list:
                    print(item)
            else:
                print("Password meets all recommended criteria.")

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")
