import random
import requests
import json

# Define the URL endpoints
BASE_URL = 'http://localhost:8000'
LOGIN_URL = f'{BASE_URL}/users/login/'
REPORT_URL = f'{BASE_URL}/reports/new/'

# Sample user credentials (replace with actual credentials or use environment variables)
user_credentials = {
    'username': 'adam5358@outlook.com',  # Replace with a valid username
    'password': 'rolls@royce'        # Replace with the corresponding password
}

# Function to log in and get the session cookies
def login():
    """Log in the user and return the session object."""
    session = requests.Session()
    login_response = session.post(LOGIN_URL, data=user_credentials)
    
    if login_response.status_code == 200:
        print("Login successful.")
        return session
    else:
        print(f"Login failed: {login_response.status_code} - {login_response.text}")
        return None

# Function to generate a random report
# Function to generate a random report
def generate_random_report(session):
    """Generate a random report and return the response data."""
    report_type = random.choice(['collection', 'recycling'])
    response = session.post(REPORT_URL, data={'report_type': report_type})
    
    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Error decoding JSON response.")
            print("Response content:", response.text)  # Print the raw response for debugging
            return None
    else:
        print(f"Failed to generate report: {response.status_code} - {response.text}")
        return None


# Main automation script
def main():
    """Main function to execute report generation."""
    session = login()
    if session:
        for _ in range(5):  # Adjust the range for the number of reports you want to generate
            report_data = generate_random_report(session)
            if report_data:
                print(f"Generated Report: {report_data}")
            else:
                print("Failed to generate report.")

if __name__ == '__main__':
    main()
