import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = string.punctuation

    def generate_password(self, length=12):
        """Generate a strong password of given length."""
        all_chars = self.lowercase + self.uppercase + self.digits + self.special_chars
        password = ''.join(random.choice(all_chars) for _ in range(length))
        return password

    def check_password_strength(self, password):
        """Check password strength based on various criteria."""
        strength = 0
        errors = []

        # Check length
        if len(password) < 8:
            errors.append("Password is too short. Minimum 8 characters required.")
        else:
            strength += 1

        # Check for uppercase letters
        if not any(char.isupper() for char in password):
            errors.append("Password should contain at least one uppercase letter.")
        else:
            strength += 1

        # Check for numbers
        if not any(char.isdigit() for char in password):
            errors.append("Password should contain at least one number.")
        else:
            strength += 1

        # Check for special characters
        if not any(char in self.special_chars for char in password):
            errors.append("Password should contain at least one special character.")
        else:
            strength += 1

        return strength, errors

def main():
    generator = PasswordGenerator()

    print("Password Generator and Strength Checker")
    print("----------------------------------------")

    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length (default=12): ") or 12)
            password = generator.generate_password(length)
            print("Generated Password:", password)
        elif choice == "2":
            password = input("Enter password to check strength: ")
            strength, errors = generator.check_password_strength(password)
            print("Password Strength:", strength, "/4")
            if errors:
                print("Errors:")
                for error in errors:
                    print("-", error)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()