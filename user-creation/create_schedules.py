import requests
import random

# Session setup
session = requests.Session()

# Define the session ID (replace with your actual session ID)
session_id = 'session_id'
session.cookies.set('sessionid', session_id)

# URL for creating the schedule
url = 'http://localhost:8000/schedules/new/'

# Randomly select a week day, day-time, and frequency
def generate_schedule_data():
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_day = random.choice(week_days)
    
    # Generate random time between 7:00 a.m. and 11:00 a.m.
    hour = random.randint(7, 11)
    minute = random.choice([0, 15, 30, 45])
    day_time = f'{hour:02d}:{minute:02d}'
    
    # Randomly select frequency
    frequency = random.choice(['Weekly', 'Monthly'])

    return {
        'week_day': week_day,
        'day_time': day_time,
        'frequency': frequency
    }

# Create 50 schedules
for _ in range(10):
    schedule_data = generate_schedule_data()
    response = session.post(url, data=schedule_data)
    
    if response.status_code == 200:
        print(f'Successfully created schedule: {schedule_data}')
    else:
        print(f'Failed to create schedule: {response.status_code} - {response.text}')
