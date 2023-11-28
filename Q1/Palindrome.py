def is_palindrome_number(number):
    # Convert the number to a string for easy comparison of digits
    num_str = str(number)
    
    # Compare the original string with its reverse
    return num_str == num_str[::-1]

# Example usage:
num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
