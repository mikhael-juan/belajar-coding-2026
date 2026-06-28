print(" 📲 Welcome to the daily health calculator! 📲")
print("Enter your health data to get a complete analysis.")
name=input("What's your name? ").strip().title()
print(f"Hello {name}! Let's begin your health check.")

#Part 1: Using if, elif, and else for Body Mass Index (BMI) classification.
print(f"\n PART 1: Body Mass Index (BMI)")
weight = float(input("Enter your weight (kg)"))
height=float(input("Enter your height (cm)"))

#Convert height from cm to m
height_m=height/100
bmi=weight/ (height_m**2)
print(f"\n Your BMI is {bmi:.1f}")
#underweight, normal weight, overweight, obese
#Classifying BMI using if, elif, and else
if bmi<18.5:
    bmi_categories="Underweight"
    bmi_recommendations="Increase your calorie and protein intake."
elif bmi<25.0:
    bmi_categories="Normal weight"
    bmi_recommendations="Maintain your current diet and physical activity."
elif bmi<30.0:
    bmi_categories="Overweight"
    bmi_recommendations="Reduce your daily calorie intake and increase physical activity"
else:
    bmi_categories="Obese"
    bmi_recommendations="Consult a doctor regarding a weight loss program."

print(f" Category:{bmi_categories}")
print(f" Suggestion: {bmi_recommendations}")

# Blood pressure classification using if/elif/else with AND.
print("Part 2: Blood Pressure")
systolic=int(input("Enter your upper blood (systolic, example:120) "))
diastolic=int(input("Enter your lower blood pressure (diastolic, for example 80) "))
if systolic<120 and diastolic <80:
    bp_categories="Normal"
    bp_advice="Your blood pressure is ideal. Keep it up!"
elif systolic<=129 and diastolic <80:
    bp_categories="Elevated"
    bp_advice="Your blood pressure is elevated. It is advisable to exercise regularly (at least 150 minutes of aerobic activity per week) and modify your diet (limit salt intake to a maximum of one teaspoon per day)."
elif systolic<=139 and diastolic <=89:
    bp_categories="Stage 1 hypertension"
    bp_advice="Your blood pressure falls into the stage 1 hypertension category. Consult a doctor promptly for cardiovascular disease risk screening, non-pharmacological therapy, or consideration of medication."
elif systolic>=140 and diastolic >=90:
    bp_categories="Stage 2 hypertension"
    bp_advice="Your blood pressure falls into the stage 2 hypertension category. Consult a doctor promptly for cardiovascular disease risk screening, non-pharmacological therapy, or consideration of medication."
else:
    bp_categories="Hypertensive crisis"
    bp_advice="Your blood pressure falls into the hypertensive crisis category. Wait 5 minutes before measuring it again. If the reading remains the same, do not take any medication and immediately call an ambulance to go to the nearest emergency department!"

print(f"\n Results: {bp_categories} ")
print(f"Suggestion : {bp_advice}")

# PART 3: Age Verification (SKIPPPP DULU)
print("PART 3: Age Verification")
age=int(input("How old are you (in years)? "))

# PART 4: Daily calorie target Calculate calorie target
def calculate_calorie_target(bmi,age):
    if bmi <18.5:
        target=2500

    elif bmi <25.0:
        target=2000
    else:
        target=1700

    if age>50:
        target=target-200
    return target

# Check whether your calorie intake has exceeded your target.
def check_calorie_goal(today_calories, calculate_calori_target ):
    return True if today_calories>=calculate_calori_target else False
def excess_calories (today_calories, calculate_calori_target ):
    return True if today_calories*120/100>calculate_calori_target else False

check_calorie_goal = calculate_calorie_target (bmi, age)
today_calories=(input(f"How many calories have you consumed today? "))
fulfilled=check_calorie_goal (today_calories, calculate_calorie_target)
