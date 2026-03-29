def generate_study_plan(subjects, days_left):
    study_plan = {}

    for subject, level in subjects.items():

        # base hours based on difficulty
        if level == "weak":
            hours = 3
        elif level == "medium":
            hours = 2
        else:
            hours = 1

        # increase effort if exam is near
        if days_left <= 5:
            hours += 1
        if days_left <= 2:
            hours += 1

        # decrease load if enough time is available
        if days_left >= 10:
            hours -= 1
            if hours < 1:
                hours = 1

        # extra focus rule for weak subjects
        if level == "weak" and days_left < 4:
            hours += 1

        study_plan[subject] = hours

    return study_plan