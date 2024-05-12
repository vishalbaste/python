import re
import requests

def extract_emails_from_webpage(url):
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code == 200:
        # Extract email addresses using regex
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', response.text)
        return emails
    else:
        print("Failed to fetch webpage:", response.status_code)
        return []

# Example usage
url = "https://example.com"
emails = extract_emails_from_webpage(url)
if emails:
    print("Email addresses found on the webpage:")
    for email in emails:
        print(email)
else:
    print("No email addresses found on the webpage.")

