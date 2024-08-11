import random
import string


def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()
