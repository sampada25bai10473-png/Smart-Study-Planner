from planner import generate_study_plan

print("=== Personalized Study Recommendation System ===")

subjects = {}

try:
    total_subjects = int(input("Enter number of subjects: "))
except:
    print("Invalid input. Please enter a valid number.")
    exit()

for i in range(total_subjects):
    subject_name = input(f"Enter subject {i+1} name: ")
    level = input("Enter difficulty (weak/medium/strong): ").lower()

    if level not in ["weak", "medium", "strong"]:
        print("Invalid level entered. Setting default as 'medium'.")
        level = "medium"

    subjects[subject_name] = level

try:
    days_left = int(input("Enter number of days left for exam: "))
except:
    print("Invalid input. Setting default days as 5.")
    days_left = 5

plan = generate_study_plan(subjects, days_left)

print("\n--- Your Personalized Study Plan ---")
total_hours = 0

for subject, hours in plan.items():
    print(f"{subject}: Study {hours} hours per day")
    total_hours += hours

print(f"\nTotal study hours per day: {total_hours}")

# small suggestion feature
if total_hours > 8:
    print("Tip: Try to take short breaks to avoid burnout.")
elif total_hours < 4:
    print("Tip: You can increase your study time for better preparation.")

print("\nStay consistent and all the best for your exams!")