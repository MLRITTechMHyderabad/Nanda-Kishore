import re


def extract_valid_emails(text):
    # Regex pattern for valid emails
    pattern = r'\b[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9-]+\.(?:[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?)\b'

    # Find all matching patterns
    valid_emails = re.findall(pattern, text)

    return valid_emails


# Example Input
text = "Contact us at support@example.com, john.doe123@company.org, or invalid-email@com. Also, try jane_doe@domain.co.uk."

# Function call
result = extract_valid_emails(text)
print(result)
