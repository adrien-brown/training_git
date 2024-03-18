"""This is a gentle program to help me cook"""

import time

# Define the recipe dictionaries for 2 recipes
chocolate_french_cake = {
    "ingredients": {
        "base": {
            "flour": "200 g",
            "cocoa powder": "100 g",
            "baking powder": "1 teaspoon",
            "salt": "a pinch"
        },
        "wet": {
            "eggs": 3,
            "butter": "70 g",
            "chopped vanilla from Madagascar,": 1,
            "sugar": "50 g"
        },
        "timing": {
            "cooking time": 25 # Time in minutes to bake 
        },
        "type of dish": {
            "cake": "French chocolate cake"
        }
    },
    "instructions": [
        "Preheat the oven to 250°C or thermostat 8-9.",
        "In a large mixing bowl, combine the dry ingredients.",
        "Add the wet ingredients to the bowl and mix well.",
        "Add butter to the baking tin",
        "Pour the batter into the baking tin.",
        "Bake for 25-30 minutes or until a knife inserted comes out clean."
    ]
}

shortbread_biscuit = {
   "ingredients": {
       "base": {
           "plain flour": "300 g",
           "granulated sugar": "100 g"
       },
       "wet": {
           "softened butter": "200 g",
           "vanilla": "1 tsp"
       },
       "timing": {
           "cooking time": 15,  # Time in minutes to bake 
       },

        "type of dish": {
            "cake": "shortbread biscuits"
        }
   },
   "instructions": [
       "Preheat the oven to 180°C (fan 160°C/gas mark 4).",
       "Line a baking tray with baking paper and grease with butter.",
       "Cream the butter and sugar in a mixing bowl until pale and light",
       "Sift the flour into the bowl and add the vanilla and mix well.",
       "Roll out the dough on a lightly floured surface.",
       "Cut out shapes using biscuit cutters or a sharp knife.",
       "Poke them with a fork to allow bubble to escape. ",
   ]
}

# Welcome message and lesson selection
print("\nWelcome to the new cooking lesson!\n")

time.sleep(2)

def get_user_choice():
    """Prompt the user to choose a recipe and handle invalid input."""
    while True:
        choice = input(
            "Which lesson would you like to do today?\n"
            "1. Chocolate French Cake\n"
            "2. Shortbread Biscuit\n"
            "Enter your choice (1 or 2): "
        )
        if choice in ("1", "2"):
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

def execute_recipe(recipe):
    """Execute the chosen recipe."""
    print("\nThe lesson will start now!\n")
    print(f"You are about to bake: {recipe['ingredients']['type of dish']['cake']}")
    time.sleep(2)

    for step_number, instruction in enumerate(recipe["instructions"], start=1):
        print(f"\n****** Step {step_number}: ******\n")
        print(instruction)
        time.sleep(1)

        if step_number == 1:
            print("\n -- Gather your ingredients: --\n")
            print("\n- Base ingredients:")
            for ingredient, amount in recipe["ingredients"]["base"].items():
                print(f"  - {ingredient} ({amount})")
                time.sleep(1)
            print("\n- Wet ingredients:")
            for ingredient, amount in recipe["ingredients"]["wet"].items():
                print(f"  - {ingredient} ({amount})")
                time.sleep(1)
            time.sleep(2)
            print("")

        input(f"\nPress a key when you're done with Step {step_number}...\n")
        time.sleep(2)

    alarm_reminder = recipe["ingredients"]["timing"]["cooking time"]
    print("\nYou are almost done, we just need to cook it!\n")
    print(f"Place your cake in the oven for {alarm_reminder} minutes.")
    time.sleep(alarm_reminder * 60)
    print("Your cake is ready, don't let it burn!")
    print("Enjoy your cake!")
    print("Congratulations, you've baked a lovely cake!")

# Welcome message and lesson selection
print("\nWelcome to the new cooking lesson!\n")
time.sleep(2)

# Get the chosen recipe and execute it
lesson_choice = get_user_choice()
chosen_recipe = chocolate_french_cake if lesson_choice == "1" else shortbread_biscuit
execute_recipe(chosen_recipe)