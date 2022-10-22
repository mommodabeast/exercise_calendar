import data_functions

# This file is intended to write initial contents to the json files in this project.

schedules = [
            #[("Pull-ups", ["sets", "reps", "weight"]), ("Squats", ["sets", "reps", "weight"]), ("Bench press", ["sets", "reps", "weight"])],
]
schedule_calendar = {}
user_performance = {}

data_functions.save_json("json_files/schedule_calendar.json", schedule_calendar)
data_functions.save_json("json_files/schedules.json", schedules)
data_functions.save_json("json_files/user_performance.json", user_performance)
