import os

# User Configuration
GENDER = "MALE"
WEIGHT_KG = "100"
HEIGHT_CM = "100"
AGE = "50"

# API Credentials
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]
SHEET_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]
SHEETY_USERNAME = os.environ.get("ENV_SHEETY_USERNAME", "")
SHEETY_PASSWORD = os.environ.get("ENV_SHEETY_PASSWORD", "")
SHEETY_TOKEN = os.environ.get("ENV_SHEETY_TOKEN", "")

# API Endpoints
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GOOGLE_SHEET_NAME = "workout"
