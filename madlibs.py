
# Mad Libs Generator 🚀

# Ask user for inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
food = input("Enter a type of food: ")
animal = input("Enter an animal: ")

# Story template
story = f"""
Once upon a time, {name} went to {place}. It was a very {adjective} day.
Suddenly, {name} decided to {verb}. Out of nowhere, a wild {animal} appeared
and stole {name}'s {food}! It was the craziest day ever!
"""

# Print the completed story
print("\nHere is your Mad Libs story: ")
print(story)
