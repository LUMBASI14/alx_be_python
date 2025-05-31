task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
  case "high":
    print("Reminder: " + task + " is a high priority task that requires immediate attention today!")
  case "medium":
    print("Reminder: " + task + " is a medium priority task that requires  attention today!")
  case "low":
    print("Note: " + task + " is a low priority task. Consider completing it when you have free time.")
  case _:
    print("priority is of unknown")
