def ask(question):
    return input(question + " (yes/no): ").strip().lower() == "yes"

def evaluate_employee():
    print("=== Employee Performance Evaluation System ===")

    punctual = ask("Is the employee punctual?")
    task_completion = ask("Does the employee complete tasks on time?")
    quality_work = ask("Does the employee produce quality work?")
    teamwork = ask("Does the employee collaborate well with others?")
    initiative = ask("Does the employee take initiative?")

    score = sum([punctual, task_completion, quality_work, teamwork, initiative])

    print("\n--- Evaluation Result ---")
    if score == 5:
        print("Outstanding Performance")
    elif score >= 3:
        print("Satisfactory Performance")
    else:
        print("Needs Improvement")

if __name__ == "__main__":
    evaluate_employee()
