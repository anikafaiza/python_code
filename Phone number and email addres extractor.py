import re

def extract_phone_numbers(text):
    # Regular expression to match phone numbers
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'

    # Find all matches in the text
    phone_numbers = re.findall(phone_pattern, text)
    
    return phone_numbers

def extract_email_addresses(text):
    # Regular expression to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    # Find all matches in the text
    email_addresses = re.findall(email_pattern, text)
    
    return email_addresses

# Example usage:
if __name__ == "__main__":
    input_text = """
    John Doe
    Phone: 123-456-7890
    Email: john@example.com

    Jane Smith
    Phone: 555.555.5555
    Email: jane.smith@email.co.uk
    """

    phone_numbers = extract_phone_numbers(input_text)
    email_addresses = extract_email_addresses(input_text)

    print("Phone Numbers:")
    for number in phone_numbers:
        print(number)

    print("\nEmail Addresses:")
    for email in email_addresses:
        print(email)
