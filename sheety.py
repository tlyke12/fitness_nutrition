import requests
import datetime


class SheetyConnection:
    def __init__(self):
        self.endpoint = 'https://api.sheety.co/f7749514f2cf978d092514d756e14ec2/myWorkouts/workouts'
        self.header = {'Authorization': 'Bearer s6T%fi*45@sfd62'}

# Details                           'name'     'duration_min'  'nf_calories'
# Row consists of   Date,   Time,   Exercise,   Duration,       Calories
    def add_row(self, details):
        current_date_time = datetime.datetime.now()
        date = current_date_time.strftime(f'%m/%d/%Y')
        time = current_date_time.strftime(f'%H:%M %p')
        sheety_data = {
            'workout': {
                'date': date,
                'time': time,
                'exercise': details['name'].title(),
                'duration': details['duration_min'],
                'calories': details['nf_calories']
            }
        }
        response = requests.post(url=self.endpoint, json=sheety_data, headers=self.header)
        response.raise_for_status()
        return response

    def get_all_records(self):
        response = requests.get(url=self.endpoint, headers=self.header).json()
        return response
