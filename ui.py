from tkinter import *
from datetime import datetime


class WorkoutUI:

    def __init__(self, nutritionix_client, sheety_client):
        self.scrollbar = None
        self.response_text = None
        self.workout_image = None
        self.workout_entry = None
        self.nutritionix_client = nutritionix_client
        self.sheety_client = sheety_client
        self.window = Tk()
        self.window.title("Workout Logger")
        self.window.config(padx=50, pady=50)
        self.setup_ui()

    def setup_ui(self):
        # Canvas
        canvas = Canvas(height=200, width=200)
        self.workout_image = PhotoImage(file="workout.png")  # Make sure 'workout.png' exists in your project directory
        canvas.create_image(100, 100, image=self.workout_image)
        canvas.grid(row=0, column=0, columnspan=2)

        # Labels
        Label(text="workout:").grid(row=2, column=0)

        # Entries
        self.workout_entry = Entry(width=21)
        self.workout_entry.grid(row=2, column=1, columnspan=1, pady=10)
        self.workout_entry.focus()

        # Buttons
        submit_button = Button(text="Submit", width=20, command=self.submit_workout)
        submit_button.grid(row=3, column=1)

        self.response_text = Text(self.window, height=10, width=40)
        self.response_text.grid(row=4, column=0, columnspan=2, pady=10)
        self.scrollbar = Scrollbar(self.window, orient=VERTICAL, command=self.response_text.yview)
        self.scrollbar.grid(row=4, column=3, sticky='ns')
        self.response_text.configure(yscrollcommand=self.scrollbar.set)

    def submit_workout(self):
        exercise_text = self.workout_entry.get()
        result = self.nutritionix_client.query_exercise(exercise_text)

        # Clear the entry widget after getting the input
        self.workout_entry.delete(0, END)

        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%X")

        for exercise in result["exercises"]:
            workout_data = {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise['duration_min'],
                "calories": exercise["nf_calories"]
            }
            sheety_response = self.sheety_client.post_workout(workout_data)
            response_message = f"Sheety Response: \n {sheety_response}\n"
            self.response_text.insert(END, response_message + "\n")
            self.response_text.see(END)

    def run(self):
        self.window.mainloop()
