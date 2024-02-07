from nutritionix import NutritionixClient
from sheety import SheetyClient
from config import GENDER, WEIGHT_KG, HEIGHT_CM, AGE
from ui import WorkoutUI


def main():
    nutritionix_client = NutritionixClient(GENDER, WEIGHT_KG, HEIGHT_CM, AGE)
    sheety_client = SheetyClient()
    workout_ui = WorkoutUI(nutritionix_client, sheety_client)
    workout_ui.run()


if __name__ == "__main__":
    main()
