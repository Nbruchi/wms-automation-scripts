import random
import requests

# URL where the recycling log form is submitted
url = "http://localhost:8000/recycle-logs/new/"

# List of recyclable types from the model
RECYCLABLES = ['plastic', 'glass', 'metal', 'paper']

# Function to create a recycling log
def create_recycling_log(session):
    recyclable_type = random.choice(RECYCLABLES)  # Pick a random recyclable type
    quantity = round(random.uniform(0.5, 10.0), 2)  # Pick a random quantity between 0.5 and 10 kg

    # Data to be sent to the recycling log form
    data = {
        'recyclable_type': recyclable_type,
        'quantity': quantity,
    }

    # Submit the form
    response = session.post(url, data=data)

    if response.status_code == 200 or response.status_code == 302:  # Success
        print(f"Successfully logged: {recyclable_type} - {quantity} kg")
    else:
        print(f"Failed to create log: {response.status_code} - {response.text}")

# Example usage:
# Replace this with the actual session ID or login process
session_id = 'session_id'

# Set up the session with the session ID
session = requests.Session()
session.cookies.set('sessionid', session_id)

# Create 10 recycling logs
for _ in range(30):
    create_recycling_log(session)
