import requests
from config import SHEET_ENDPOINT, GOOGLE_SHEET_NAME, SHEETY_USERNAME, SHEETY_PASSWORD, SHEETY_TOKEN


class SheetyClient:
    def __init__(self):
        self.endpoint = SHEET_ENDPOINT

    def post_workout(self, workout_data, auth_type="basic"):
        if auth_type == "basic":
            response = requests.post(
                self.endpoint,
                json={GOOGLE_SHEET_NAME: workout_data},
                auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
            )
        elif auth_type == "bearer":
            headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
            response = requests.post(
                self.endpoint,
                json={GOOGLE_SHEET_NAME: workout_data},
                headers=headers
            )
        else:
            response = requests.post(self.endpoint, json={GOOGLE_SHEET_NAME: workout_data})
        return response.text
