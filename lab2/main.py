# Rock, Paper, Scissors Game

# 1. Define the Choices Array
choices = ["Rock", "Paper", "Scissors"]

# 2. Get Player Input
playerChoice = input("Select your weapon: (1=Rock, 2=Paper, 3=Scissors): ")

# 3. Convert to Integer
playerChoice = int(playerChoice)

# 4. Error Handling
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    # 5. Get Computer's Choice (simulated input for now)
    cpuChoice = input("Enter opponent's choice (1-3): ")
    cpuChoice = int(cpuChoice)

    if cpuChoice < 1 or cpuChoice > 3:
        print("Error: Choice must be between 1 and 3.")
    else:
        # 6. Array Indexing - subtract 1 for 0-indexed array
        playerChoiceName = choices[playerChoice - 1]
        cpuChoiceName = choices[cpuChoice - 1]

        print("You chose: " + playerChoiceName)
        print("Computer chose: " + cpuChoiceName)

        # 7. Determine the Winner
        if playerChoice == cpuChoice:
            print("It's a tie!")
        elif playerChoice == 1 and cpuChoice == 3:
            print("Rock beats Scissors - You win!")
        elif playerChoice == 2 and cpuChoice == 1:
            print("Paper beats Rock - You win!")
        elif playerChoice == 3 and cpuChoice == 2:
            print("Scissors beats Paper - You win!")
        else:
            print("You lose!")

        # 8. String Comparison
        if playerChoiceName != "Rock":
            print("You didn't pick the classic Rock...")
