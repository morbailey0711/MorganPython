import sys

# pip install datetime
from datetime import date

# pip install word2number
from word2number import w2n

# pip install regex
import re

# pip install tabulate
from tabulate import tabulate


class Novice_Workout:
    def __init__(self, day):
        self.day = day

    def workout(self):
        col_time = ["Exercise", "Sets", "Time (s)"]
        col_reps = ["Exercise", "Sets", "Reps"]

        if self.day == "monday":
            fullbody1 = [
                ["Knee Push-Ups", "3", "8-12"],
                ["Tricep Extensions", "3", "8-12"],
                ["Australian Pull-Ups", "3", "8-12"],
                ["Australian Chin-Ups", "3", "8-12"],
                ["Explosive Squats", "3", "8-12"],
                ["Lunges", "3", "8-12 (Each Leg)"],
            ]
            table = tabulate(fullbody1, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's novice workout:\n{table}")
        elif self.day == "wednesday":
            fullbody2 = [
                ["Pike Push-Ups", "3", "8-12"],
                ["Supported Dips", "3", "8-12"],
                ["Australian Pull-Ups", "3", "8-12"],
                ["Negative Pull-Ups", "3", "8-12"],
                ["Squats", "3", "8-12"],
                ["Sumo Squats", "3", "8-12"],
            ]
            table = tabulate(fullbody2, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's novice workout:\n{table}")
        elif self.day == "friday":
            fullbody3 = [
                ["Box Jumps", "3", "8-12"],
                ["Lunges", "3", "8-12 (Each Leg)"],
                ["Negative Pull-Ups", "3", "8-12"],
                ["Boat Holds", "3", "12-15s"],
                ["Leg Flutters", "3", "8-12 (Each Leg)"],
                ["Knee Push-Ups", "3", "8-12"],
            ]
            table = tabulate(fullbody3, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's novice workout:\n{table}")
        else:
            print(f"Today is a rest day for the novice routine.")


class Intermediate_Workout:
    def __init__(self, day):
        self.day = day

    def workout(self):
        col_time = ["Exercise", "Sets", "Time (s)"]
        col_reps = ["Exercise", "Sets", "Reps"]

        if self.day == "monday":
            push = [
                ["Bench Press", "3", "6-8"],
                ["Push-Ups", "4", "15-20"],
                ["Shoulder Press", "3", "6-8"],
                ["Chest Flies", "3", "8-12"],
                ["Tricep Dips", "3", "8-12"],
                ["Tricep Extensions", "3", "8-12"],
            ]
            table = tabulate(push, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's intermediate workout:\n{table}")
        elif self.day == "wednesday":
            pull = [
                ["Pull-Ups", "3", "8-10"],
                ["Bent Over Rows", "4", "8-12"],
                ["Deadlifts", "4", "4-6"],
                ["Lateral Pull Downs", "4", "8-12"],
                ["Chin-Ups", "3", "8-12"],
                ["Hammer Curls", "4", "8-12 (Each Arm)"],
            ]
            table = tabulate(pull, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's intermediate workout:\n{table}")
        elif self.day == "friday":
            lower = [
                ["Squats", "4", "8-10"],
                ["Lunges", "3", "8-12"],
                ["Bulgarian Split Squats", "3", "4-6 (Each Leg)"],
                ["Hamstring Curls", "4", "8-12"],
                ["Calf Raises", "4", "8-12 (Each Leg)"],
                ["Wall Shin Raises", "3", "6-8 (Each Leg)"],
            ]
            table = tabulate(lower, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's intermediate workout:\n{table}")
        elif self.day == "sunday":
            fitness = [
                ["Burpees", "3", "45"],
                ["Plank", "3", "60-120"],
                ["Push-ups", "3", "45"],
                ["Explosive Lunges", "3", "45"],
                ["Pull-Ups", "3", "45"],
                ["Mountain Climbers", "3", "45"],
            ]
            table = tabulate(fitness, headers=col_time, tablefmt="fancy_grid")
            print(f"Today's novice workout:\n{table}")
        else:
            print(f"Today is a rest day for the intermediate routine.")


class Advanced_Workout:
    def __init__(self, day):
        self.day = day

    def workout(self):
        col_time = ["Exercise", "Sets", "Time (s)"]
        col_reps = ["Exercise", "Sets", "Reps"]

        if self.day == "monday":
            chesttri = [
                ["Bench Press", "4", "6-8"],
                ["Push-Ups", "4", "20-25"],
                ["Incline Bench Press", "4", "6-8"],
                ["Chest Flies", "3", "8-12"],
                ["Tricep Dips", "3", "8-12"],
                ["Skull Crushers", "3", "8-12"],
            ]
            table = tabulate(chesttri, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's advanced workout:\n{table}")
        elif self.day == "tuesday":
            backbi = [
                ["Pull-Ups", "4", "10-12"],
                ["Bent Over Rows", "4", "8-12"],
                ["Deadlift", "6", "4-6"],
                ["Front Lever Raises", "4", "8-12"],
                ["Chin-Ups", "3", "8-12"],
                ["Hammer Curls", "4", "8-12 (Each Arm)"],
            ]
            table = tabulate(backbi, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's advanced workout:\n{table}")
        elif self.day == "wednesday":
            fitness = [
                ["Burpees", "3", "45"],
                ["Plank", "3", "60-120"],
                ["Push-ups", "3", "45"],
                ["Explosive Lunges", "3", "45"],
                ["Pull-Ups", "3", "45"],
                ["Mountain Climbers", "3", "45"],
            ]
            table = tabulate(fitness, headers=col_time, tablefmt="fancy_grid")
            print(f"Today's advanced workout:\n{table}")
        elif self.day == "thursday":
            legs = [
                ["Squats", "4", "8-10"],
                ["Front Squats", "3", "8-12"],
                ["Bulgarian Split Squats", "3", "4-6 (Each Leg)"],
                ["Hamstring Curls", "4", "8-12"],
                ["Lunges", "4", "8-12 (Each Leg)"],
                ["Wall Shin Raises", "3", "6-8 (Each Leg)"],
            ]
            table = tabulate(legs, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's advanced workout:\n{table}")
        elif self.day == "friday":
            shoulderabs = [
                ["Shoulder Press", "4", "6-8"],
                ["Wall Handstand Press", "3", "4-6"],
                ["Lateral Raises", "3", "8-12"],
                ["Toes-To-Bar", "3", "12-15"],
                ["Leg Flutters", "4", "8-12 (Each Leg)"],
                ["L-Sit Hold", "3", "30 Seconds"],
            ]
            table = tabulate(shoulderabs, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's advanced workout:\n{table}")
        elif self.day == "sunday":
            mobility = [
                ["Hands, Fingers and Wrists", "1", "60"],
                ["Squat Internal Rotations", "1", "60"],
                ["Hamstring Stretch", "1", "60"],
                ["Spider Crawl Stretch", "1", "60"],
                ["Cat-Cow Stretch", "1", "60"],
                ["Child's Pose", "1", "60"],
            ]
            table = tabulate(mobility, headers=col_reps, tablefmt="fancy_grid")
            print(f"Today's advanced workout:\n{table}")
        else:
            print(f"Today is a rest day for the advanced routine.")


def main():
    userinput = input("How many years experience? ").strip().lower()

    week = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    week_day = week[date.today().weekday()]

    if experience(format_input(userinput)) == "novice":
        Novice_Workout(week_day).workout()
    elif experience(format_input(userinput)) == "intermediate":
        Intermediate_Workout(week_day).workout()
    else:
        Advanced_Workout(week_day).workout()


def format_input(userinput):
    # remove words before or after the number of years in the input string
    ignore = [
        "i ",
        "have",
        "worked",
        "out",
        "for",
        "been",
        "working",
        "experience",
        "years",
        "year",
        "had",
        "trained",
    ]

    # remove full stops at the end to avoid issues with decimal numbers
    userinput = re.sub(",", "", userinput)
    if userinput.endswith("."):
        userinput = userinput[:-1]
    # remove words from toignore data, leaving just a number in written or number format
    for word in ignore:
        userinput = re.sub(word, "", userinput).strip()
    # to ensure that inputs such as 'cat' value error rather than value error within w2n function
    while True:
        try:
            # if the input if number
            if re.search("^[0-9. ]+$", userinput):
                years = float(userinput)
                return years
            # if the input in typed numbers (including decimals (i.e., 'point one'))
            elif re.search("^[a-z ]+$", userinput):
                years = w2n.word_to_num(userinput)
                return years
            # to return system exit for inputs such as '-1'
            else:
                sys.exit("Please input a valid number of years.")
        except ValueError:
            sys.exit("Please input a valid number of years.")


def experience(years):
    if 0 <= years <= 1:
        level = "novice"
        return level
    elif 1 < years <= 3:
        level = "intermediate"
        return level
    elif 3 < years <= 122:
        level = "advanced"
        return level
    else:
        sys.exit("You are older than the world's oldest person on record... 🧢")


if __name__ == "__main__":
    main()
