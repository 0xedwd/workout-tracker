import requests
from config import APP_ID, API_KEY, NUTRITIONIX_ENDPOINT


class NutritionixClient:
    def __init__(self, gender, weight_kg, height_cm, age):
        self.gender = gender
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.age = age

    def query_exercise(self, exercise_text):
        headers = {
            "x-app-id": APP_ID,
            "x-app-key": API_KEY,
        }
        parameters = {
            "query": exercise_text,
            "gender": self.gender,
            "weight_kg": self.weight_kg,
            "height_cm": self.height_cm,
            "age": self.age
        }
        response = requests.post(NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
        return response.json()
