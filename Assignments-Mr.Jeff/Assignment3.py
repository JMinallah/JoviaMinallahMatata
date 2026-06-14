#Real-world application of loops
# PROBLEM STATEMENT

# Scenario

# You are the manager of a national football team competing in the 2026 FIFA World Cup. Your task is to guide your team through:
# Pre-tournament preparation (training, friendlies, recovery)
# Group stage matches (3 matches)
# Knockout stages (Round of 16, Quarter-final, Semi-final, Final)
# Challenge
# Using loop control statements, create a simulation where:
# User choices affect team performance (morale, injuries, strength)
# Loop exits when tournament is won or lost (break)
# Certain conditions skip to next iteration (continue)
# Placeholders exist for future features (pass)

# Simulating the tournament

# Pre-tournament preparation
training_days = 30
for day in range(1, training_days + 1):
    print(f"Day {day}: Training session")
    if day % 7 == 0:
        print("Rest day for recovery")
        continue  # Skip training on rest days
    if day == 15:
        print("Injury during training! Skipping next 5 days.")
        for _ in range(5):
            print("Recovery day")
        continue  # Skip the next 5 days of training

# Group stage matches
group_stage_matches = 3
for match in range(1, group_stage_matches + 1):
    print(f"Group Stage Match {match}")
    # Simulate match outcome
    outcome = input("Enter match outcome (win/draw/loss): ").lower()
    if outcome == "win":
        print("Great job! Moving to the next match.")
    elif outcome == "draw":
        print("Not bad, but we need to improve.")
    elif outcome == "loss":
        print("Tough loss. We need to regroup.")
        break  # Exit the loop if the team loses a match
    else:
        print("Invalid input. Please enter win, draw, or loss.")
        continue  # Skip to the next iteration for invalid input
    
# Knockout stages
knockout_stages = ["Round of 16", "Quarter-final", "Semi-final", "Final"]
for stage in knockout_stages:
    print(f"Knockout Stage: {stage}")
    # Simulate match outcome
    outcome = input("Enter match outcome (win/loss): ").lower()
    if outcome == "win":
        print(f"Congratulations! You've advanced to the next stage.")
        if stage == "Final":
            print("You've won the World Cup!")
            break  # Exit the loop if the team wins the final
    elif outcome == "loss":
        print("Unfortunately, you've been eliminated from the tournament.")
        break  # Exit the loop if the team loses a match
    else:
        print("Invalid input. Please enter win or loss.")
        continue  # Skip to the next iteration for invalid input
    

    