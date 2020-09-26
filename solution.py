import argparse
parser = argparse.ArgumentParser(description='Testing healthy lifestyle index')

parser.add_argument('--name', type=str, help='Write your name')
parser.add_argument('--gender', choices=["male", "female", "other"], help='Choose your gender')
parser.add_argument('height', type=float, help='Write your height')
parser.add_argument('weight', type=float, help='Write your weight')
parser.add_argument('sleep', type=int, help='How much do you usually sleep')
parser.add_argument('meals', type=int, help='How many meals does your daily diet include')
parser.add_argument('veggie', type=int, help='How many fresh fruits and vegetables do you eat during the day?')
parser.add_argument('steps', type=int, help='How many steps do you walk on average per day')
parser.add_argument('medicine', choices=["Not", "Yes, I have been undergoing medical examination in the last 3 years", "Yes, but I do not see a doctor"], help='Do you monitor your health')
parser.add_argument('mood', choices=["Good", "Neutral", "Bad"], help='What is your mood today')
parser.add_argument('happiness', choices=["During the week", "During the month", "During the year"], help='What is your mood today')

args = parser.parse_args()
# print(args.indir)

point = 0
BMI = (args.weight / (args.height * args.height))*10000
if 18.5 <= BMI <= 24.9:
    point += 1
if 7 <= args.sleep <= 8:
    point += 1
if args.meals == 4 or args.meals == 5:
    point += 1
if args.veggie >= 500:
    point += 1
if args.steps >= 10000:
    point += 1
if args.medicine == "Yes, I have been undergoing medical examination in the last 3 years":
    point += 1
if args.mood == "Good":
    point += 1
if args.happiness == "During the week":
    point += 1
if point == 8:
    print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
elif 5 <= point <= 7:
    print("Your health index is {}/8, which means that you are on the right track!".format(point))
else:
    print("Your healthy lifestyle index is {}/8, you need to rethink your healthy lifestyle!".format(point))
