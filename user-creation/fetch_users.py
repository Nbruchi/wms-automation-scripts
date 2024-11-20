import requests

BASE_URL = 'http://localhost:8000'  # Adjust this if your server runs elsewhere

def fetch_users():
    response = requests.get(f'{BASE_URL}/users/list/')
    if response.status_code == 200:
        try:
            users = response.json()  # Assuming this returns a list of users
            print("Fetched users:")
            for user in users:
                print(user)  # Print each user
        except ValueError:
            print(f"Response content is not valid JSON: {response.text}")
    else:
        print(f"Error fetching users: {response.status_code} - {response.text}")

if __name__ == '__main__':
    fetch_users()
