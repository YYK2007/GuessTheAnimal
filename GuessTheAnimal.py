import random

# Create a list of animals
animals = ["dog", "cat", "elephant", "lion", "tiger", "monkey", "zebra", "giraffe", "hippopotamus", "crocodile", "snake"]

# Create a list of possible questions
possible_questions = ["Does it have fur?", "Does it have four legs?", "Does it live in the jungle?", "Is it warm-blooded?", "Is it a predator?", "Is it endangered?"]

# Choose a random animal
animal = random.choice(animals)

# Start the game
print("Welcome to the animal guessing game!")
print("I'm thinking of an animal. You can ask me yes-or-no questions to try to guess it.")

# Print the possible questions
print("\nHere are the possible questions you can ask:")
for i, question in enumerate(possible_questions):
    print(f"{i + 1}. {question}")
print("\nMake sure to write the questions exactly how they are written \n")

# Start the loop for the game
while True:
    # Ask the user a question
    question = input("Ask me a yes-or-no question: ")

    # Validate the question
    if question not in possible_questions:
        print("Invalid question. Please choose a question from the list above.")
        continue

    # Answer the question based on the animal's features
    if question == "Does it have fur?":
        if animal in ["dog", "cat", "monkey", "zebra", "giraffe", "tiger", "lion"]:
            print("Yes")
        else:
            print("No")
    elif question == "Does it have four legs?":
        if animal not in ["snake"]:
            print("Yes")
        else:
            print("No")
    elif question == "Does it live in the jungle?":
        if animal in ["monkey", "tiger", "elephant"]:
            print("Yes")
        else:
            print("No")
    elif question == "Is it warm-blooded?":
        if animal in ["dog", "cat", "elephant", "lion", "tiger", "monkey", "zebra", "giraffe", "hippopotamus"]:
            print("Yes")
        else:
            print("No")
    elif question == "Is it a predator?":
        if animal in ["lion", "tiger", "crocodile", "snake"]:
            print("Yes")
        else:
            print("No")
    elif question == "Is it endangered?":
        if animal in ["elephant", "rhino", "tiger", "panda"]:
            print("Yes")
        else:
            print("No")

    # Check if the user guessed the animal
    guess = input("Do you think you know the animal? (y/n): ")
    if guess == "y":
        guess = input("What animal is it? ")
        if guess == animal:
            print("Correct! You win!")
            break
        else:
            print("Incorrect. Try again.")
