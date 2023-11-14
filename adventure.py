import random
import time


def print_pause(message, wait_time):
    print(message)
    time.sleep(wait_time)


def fight(weapon_choice):
    print_pause(f"The {enemy} attacks you!", 2)
    if weapon_choice == "dagger":
        print_pause(f"You feel a bit under-prepared for this, what with only having a tiny {weapon_choice}.", 2)
    choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        if weapon_choice == "dagger":
            print_pause(f"You do your best...", 1)
            print_pause(f"but your {weapon_choice} is no match for the {enemy}.", 2)
            print_pause(f"You have been defeated!""", 2)
        elif weapon_choice == "sword":
            print_pause(f"As the {enemy} moves to attack, you unsheath your new sword.", 2)
            print_pause(f"The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.", 3)
            print_pause(f"But the {enemy} takes one look at your shiny new toy and runs away!", 3)
            print_pause(f"You have rid the town of the {enemy}. You are victorious!", 3)
    elif choice == '2':
        print_pause("You run back into the field. Luckily, you don't seem to have been followed.", 2)
        next_direction()

def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            print_pause("Thanks for playing! See you next time.", 2)
            return 'game_over'
        elif choice == 'y':
            print_pause("Excellent! Restarting the game ...", 2)
            weapon_choice = 'dagger'
            return 'running'


def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.", 3)
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause(f"In your hand you hold your trusty (but not very effective) {weapon_choice}.", 2)

def next_direction():
    print_pause("", 1)
    print_pause("Enter 1 to knock on the door of the house.", 2)
    print_pause("Enter 2 to peer into the cave.", 2)
    print_pause("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        house()
    elif choice == '2':
        cave()


def house():
    print_pause("You approach the door of the house.", 2)
    print_pause(f"You are about to knock when the door opens and out steps a {enemy}.", 2)
    print_pause(f"Eep! This is the {enemy}'s house!", 2)
    fight(weapon_choice)

def cave():
    global cave_visited
    global weapon_choice
    print_pause("You peer cautiously into the cave.", 2)
    if cave_visited:
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.", 2)
    elif cave_visited is False:
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause(f"You discard your silly old {weapon_choice} and take the sword with you.", 2)
        weapon_choice = "sword"
    cave_visited = True
    print_pause("You walk back out to the field.", 2)
    next_direction()


is_game_state = 'running'
while is_game_state == 'running':

    enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    weapon_choice = 'dagger'
    cave_visited = False

    intro()
    next_direction()

    is_game_state = play_again()
