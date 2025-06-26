"""
Email Breach Checker using HaveIBeenPwned API
Author: Your Name
"""

import requests
import time

# Replace with your actual API key from https://haveibeenpwned.com/API/Key
API_KEY = "YOUR_API_KEY_HERE"
API_URL = "https://haveibeenpwned.com/api/v3/breachedaccount/{}"

HEADERS = {
    "hibp-api-key": API_KEY,
    "user-agent": "email-breach-checker"
}

def check_email(email):
    """Check a single email for breaches."""
    try:
        response = requests.get(API_URL.format(email), headers=HEADERS, params={"truncateResponse": "false"})
        if response.status_code == 200:
            breaches = response.json()
            print(f"[!] {email} was found in the following breaches:")
            for breach in breaches:
                print(f"    - {breach['Name']} ({breach['BreachDate']})")
        elif response.status_code == 404:
            print(f"[+] {email} was NOT found in any breach.")
        else:
            print(f"[!] Error checking {email}: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Network error for {email}: {e}")
    time.sleep(1.6)  # Rate limit: max 1 request per 1.5 seconds

def main():
    print("=== Email Breach Checker ===")
    print("Enter email addresses to check, separated by commas:")
    emails = input(">> ").strip().split(',')

    if API_KEY == "YOUR_API_KEY_HERE":
        print("[X] ERROR: Please add your HaveIBeenPwned API key in the script.")
        return

    for email in map(str.strip, emails):
        if email:
            check_email(email)

if __name__ == "__main__":
    main()
