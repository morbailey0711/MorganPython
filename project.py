import sys

# pip install datetime
from datetime import date

# pip install word2number
from word2number import w2n

# pip install regex
import re

# pip install tabulate
from tabulate import tabulate


def main():
    userinput = input("How many years experience? ").strip().lower()
    format_table(experience(format_input(userinput)))


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
        ",",
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
            elif re.search("^[a-z ]+$", userinput, re.IGNORECASE):
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


def format_table(level):
    fullbody1 = [
    ["Knee Push-Ups", "3", "8-12"],
    ["Tricep Extensions", "3", "8-12"],
    ["Australian Pull-Ups", "3", "8-12"],
    ["Australian Chin-Ups", "3", "8-12"],
    ["Explosive Squats", "3", "8-12"],
    ["Lunges", "3", "8-12 (Each Leg)"],
    ]
    fullbody2 = [
        ["Pike Push-Ups", "3", "8-12"],
        ["Supported Dips", "3", "8-12"],
        ["Australian Pull-Ups", "3", "8-12"],
        ["Negative Pull-Ups", "3", "8-12"],
        ["Squats", "3", "8-12"],
        ["Sumo Squats", "3", "8-12"],
    ]
    fullbody3 = [
        ["Box Jumps", "3", "8-12"],
        ["Lunges", "3", "8-12 (Each Leg)"],
        ["Negative Pull-Ups", "3", "8-12"],
        ["Boat Holds", "3", "12-15s"],
        ["Leg Flutters", "3", "8-12 (Each Leg)"],
        ["Knee Push-Ups", "3", "8-12"],
    ]
    push = [
        ["Bench Press", "3", "6-8"],
        ["Push-Ups", "4", "15-20"],
        ["Shoulder Press", "3", "6-8"],
        ["Chest Flies", "3", "8-12"],
        ["Tricep Dips", "3", "8-12"],
        ["Tricep Extensions", "3", "8-12"],
    ]
    pull = [
        ["Pull-Ups", "3", "8-10"],
        ["Bent Over Rows", "4", "8-12"],
        ["Deadlifts", "4", "4-6"],
        ["Lateral Pull Downs", "4", "8-12"],
        ["Chin-Ups", "3", "8-12"],
        ["Hammer Curls", "4", "8-12 (Each Arm)"],
    ]
    lower = [
        ["Squats", "4", "8-10"],
        ["Lunges", "3", "8-12"],
        ["Bulgarian Split Squats", "3", "4-6 (Each Leg)"],
        ["Hamstring Curls", "4", "8-12"],
        ["Calf Raises", "4", "8-12 (Each Leg)"],
        ["Wall Shin Raises", "3", "6-8 (Each Leg)"],
    ]
    fitness = [
        ["Burpees", "3", "45"],
        ["Plank", "3", "60-120"],
        ["Push-ups", "3", "45"],
        ["Explosive Lunges", "3", "45"],
        ["Pull-Ups", "3", "45"],
        ["Mountain Climbers", "3", "45"],
    ]
    chesttri = [
        ["Bench Press", "4", "6-8"],
        ["Push-Ups", "4", "20-25"],
        ["Incline Bench Press", "4", "6-8"],
        ["Chest Flies", "3", "8-12"],
        ["Tricep Dips", "3", "8-12"],
        ["Skull Crushers", "3", "8-12"],
    ]
    backbi = [
        ["Pull-Ups", "4", "10-12"],
        ["Bent Over Rows", "4", "8-12"],
        ["Deadlift", "6", "4-6"],
        ["Front Lever Raises", "4", "8-12"],
        ["Chin-Ups", "3", "8-12"],
        ["Hammer Curls", "4", "8-12 (Each Arm)"],
    ]
    legs = [
        ["Squats", "4", "8-10"],
        ["Front Squats", "3", "8-12"],
        ["Bulgarian Split Squats", "3", "4-6 (Each Leg)"],
        ["Hamstring Curls", "4", "8-12"],
        ["Lunges", "4", "8-12 (Each Leg)"],
        ["Wall Shin Raises", "3", "6-8 (Each Leg)"],
    ]
    shoulderabs = [
        ["Shoulder Press", "4", "6-8"],
        ["Wall Handstand Press", "3", "4-6"],
        ["Lateral Raises", "3", "8-12"],
        ["Toes-To-Bar", "3", "12-15"],
        ["Leg Flutters", "4", "8-12 (Each Leg)"],
        ["L-Sit Hold", "3", "30 Seconds"],
    ]
    mobility = [
        ["Hands, Fingers and Wrists", "1", "60"],
        ["Squat Internal Rotations", "1", "60"],
        ["Hamstring Stretch", "1", "60"],
        ["Spider Crawl Stretch", "1", "60"],
        ["Cat-Cow Stretch", "1", "60"],
        ["Child's Pose", "1", "60"],
    ]
    novice = {
    "Monday": fullbody1,
    "Tuesday": "Rest",
    "Wednesday": fullbody2,
    "Thursday": "Rest",
    "Friday": fullbody3,
    "Satuday": "Rest",
    "Sunday": "Rest",
    }

    intermediate = {
        "Monday": push,
        "Tuesday": "rest",
        "Wednesday": pull,
        "Thursday": "rest",
        "Friday": lower,
        "Satuday": "rest",
        "Sunday": fitness,
    }

    advanced = {
        "Monday": chesttri,
        "Tuesday": backbi,
        "Wednesday": fitness,
        "Thursday": legs,
        "Friday": shoulderabs,
        "Satuday": "rest",
        "Sunday": mobility,
    }

    plan_dict = {"novice": novice, "intermediate": intermediate, "advanced": advanced}
    plan = plan_dict[level]

    week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    week_day = week[date.today().weekday()]

    if (plan == advanced and week_day == ("Wednesday" or "Sunday")) | (
        plan == intermediate and week_day == "Sunday"
    ):
        col_names = ["Exercise", "Sets", "Time (s)"]
        table = tabulate(plan[week_day], headers=col_names, tablefmt="fancy_grid")
        print(f"Today's {level} workout:\n{table}")
    elif (
        (
            plan == novice
            and week_day == ("Tuesday" or "Thursday" or "Saturday" or "Sunday")
        )
        | (plan == intermediate and week_day == ("Tuesday" or "Thursday" or "Saturday"))
        | (plan == advanced and week_day == "Saturday")
    ):
        print(f"Today is a rest day for the {level} routine.")
    else:
        col_names = ["Exercise", "Sets", "Reps"]
        table = tabulate(plan[week_day], headers=col_names, tablefmt="fancy_grid")
        print(f"Today's {level} workout:\n{table}")


if __name__ == "__main__":
    main()