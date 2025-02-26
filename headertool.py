import requests
import random
from termcolor import colored
from itertools import cycle

# List of simple pyfiglet fonts
SIMPLE_FONTS = ['slant', 'small', 'banner', 'digital', 'block']

# List of common security headers
SECURITY_HEADERS = [
    "Strict-Transport-Security", 
    "Content-Security-Policy", 
    "X-Content-Type-Options", 
    "X-Frame-Options", 
    "X-XSS-Protection", 
    "Referrer-Policy", 
    "Feature-Policy", 
    "Permissions-Policy"
]

# ASCII Art Banner as per user request
BANNER = """
   _____                      _ __           __  __               __         
  / ___/___  _______  _______(_) /___  __   / / / /__  ____ _____/ /__  _____
  \__ \/ _ \/ ___/ / / / ___/ / __/ / / /  / /_/ / _ \/ __ `/ __  / _ \/ ___/
 ___/ /  __/ /__/ /_/ / /  / / /_/ /_/ /  / __  /  __/ /_/ / /_/ /  __/ /    
/____/\___/\___/\__,_/_/  /_/\__/\__, /  /_/ /_/\___/\__,_/\__,_/\___/_/     
                                /____/                                       

                                                          
"""

# Function to check headers and print results
def check_security_headers(domain):
    try:
        # Send a GET request to the domain
        response = requests.get(f"http://{domain}", timeout=10)
        
        # Extract response headers
        headers = response.headers

        existing_headers = []
        missing_headers = []

        # Check if each security header is in the response
        for header in SECURITY_HEADERS:
            if header in headers:
                existing_headers.append(header)
            else:
                missing_headers.append(header)

        # Display results
        if existing_headers:
            print(colored("\nExisting Security Headers (Green):", 'green', attrs=['bold']))
            for header in existing_headers:
                print(colored(f"  - {header}", 'green', attrs=['bold']))
        if missing_headers:
            print(colored("\nMissing Security Headers (Red):", 'red', attrs=['bold']))
            for header in missing_headers:
                print(colored(f"  - {header}", 'red', attrs=['bold']))
        if not existing_headers and not missing_headers:
            print("No security headers found.")

    except requests.RequestException as e:
        print(colored(f"\nFailed to access {domain}. Please try again. Error: {str(e)}", 'red', attrs=['bold']))

# Function to generate a rainbow banner
def print_rainbow_banner(text):
    # Create a rainbow color cycle
    colors = cycle(['red', 'yellow', 'green', 'cyan', 'blue', 'magenta'])
    
    # Print the banner with rainbow colors
    for line in BANNER.split('\n'):
        print(colored(line, next(colors), attrs=['bold']))

# Main loop to ask for user input
def main():
    # ASCII Art Banner with rainbow colors
    print_rainbow_banner("Security Header Check by GodXcipher")
    
    while True:
        domain = input("Enter the domain (e.g., example.com): ").strip()
        if domain:
            check_security_headers(domain)
            break
        else:
            print(colored("Please enter a valid domain name.", 'red', attrs=['bold']))

    print("\n" + colored("Copyrights GodXcipher", 'yellow', attrs=['bold']))

if __name__ == "__main__":
    main()
