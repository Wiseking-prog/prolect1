import random


game_running = True

computer_brain = [
    "james",
    "chloe",
    "lucas",
    "avery",
    "ethan",
    "hazel",
    "mason",
    "layla",
    "logan",
    "grace",
]

computer_seceret = random.choice(computer_brain)

no_attempts = 0
# we want to cmpare computer secret and the user guess.
while game_running is True:
    
    
    if no_attempts < 6:

        guess = input("Try Guessing the computers secret: ")

        # Correct letter in correct position
        no_correct = 0

        for char in computer_seceret:
            for let in guess:
                if char == let:
                    no_correct += 1
                    
            if no_correct == len(computer_seceret):
                print("Wow you guessed the computer secret right")
                game_running = False

        # Correct letter in wrong position
        for char in guess:
            if char in computer_seceret:
                print(
                    f"{char} is in Computer Secret but you put it in the wrong postion 🟨"
                )

        # Letter not in the word
        for char in guess:
            if char not in computer_seceret:
                print(f"This character {char} is not in computer secret ⬜")

        no_attempts = no_attempts + 1
    else:
        print("You have run out of attempts")
        game_running = False