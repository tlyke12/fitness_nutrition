import requests


class NutriConnect:

    def __init__(self):
        self.app_id = '5d876c5e'
        self.app_key = 'a1321eed2d1a1ef5e946e4b782c52e46'
        self.header = {
            'x-app-id': self.app_id,
            'x-app-key': self.app_key,
            'x-remote-user-id': '0'
        }
        self.endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
        self.gender = 'male'
        self.weight_kg = 95.3
        self.height_cm = 185
        self.age = 62

    def calc_workout(self, workout):
        response = requests.post(url=self.endpoint,
                                 json={
                                     'query': workout,
                                     'gender': self.gender,
                                     'weight_kg': self.weight_kg,
                                     'height_cm': self.height_cm,
                                 },
                                 headers=self.header)
        response.raise_for_status()
        return response.json()['exercises'][0]
