import random
import string

def get_user_password_criteria():
    """Asks the user for password length and character types."""
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length <= 0:
                print("Length must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    use_letters = input("Include letters? (yes/no): ").lower().startswith('y')
    use_numbers = input("Include numbers? (yes/no): ").lower().startswith('y')
    use_symbols = input("Include symbols? (yes/no): ").lower().startswith('y')

    if not (use_letters or use_numbers or use_symbols):
        print("You must select at least one character type.")
        return get_user_password_criteria()
    
    return length, use_letters, use_numbers, use_symbols

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generates a random password based on the provided criteria."""
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&*() etc.

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to run the password generator."""
    print("Welcome to the Password Generator!")
    
    while True:
        length, use_letters, use_numbers, use_symbols = get_user_password_criteria()
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        print(f"\nGenerated Password: {password}")
        
        play_again = input("\nDo you want to generate another password? (yes/no): ").lower()
        if not play_again.startswith('y'):
            print("Thank you for using the password generator. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
