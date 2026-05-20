import random
choices = {
    1: "Rock",
    0: "Paper",
    -1: "Scissors"
}


print("Welcome to ROCK, PAPER, SCISSORS GAME!!!")
print("Please select one option: ")
print("Rock: 1")
print("Paper: 0")
print("Scissors: -1")
C = int(input("Enter your choice: "))


computer = random.randint(-1, 1)


you = choices[C]


print(f"You chose {you} and the computer chose {choices[computer]}")


if computer == C:
    print("It's a draw!")
elif (computer == 1 and C == 0) or (computer == 0 and C == -1) or (computer == -1 and C == 1):
    print("You win!")
else:
    print("You lose!")
