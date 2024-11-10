"""
Let's you play through the Monty Hall problem with three doors as often as you like.
Car is behind a uniformly random door. Monty deterministically chooses the last non-car
door if the player chose a non-car door and chooses a door uniformly at random if player 
chose the car door initially.
Demonstrates to those without faith in conditional probability that switching > staying.

Original R-code from:
Blitzstein; Hwang "Introduction to Probability." 2019. p. 82–83.
Their code only lets you play one round and does not give you your win/loss ratio,
but the code for getting the theoretical proportions (in my main() function) is theirs
almost verbatim.
"""

import numpy as np

DOORS = [1, 2, 3]


def main():
    """
    Starts the Monty Hall game loop, allowing the player to play multiple rounds.

    The game continues until the player decides to stop, tallies wins and rounds
    and shows the proportion of wins.
    Shows what would happen if you played 1000 rounds always/never switching.
    """
    num_wins = 0
    num_rounds = 0  # this is at least 1 since you're forced to play a round

    # counting wins and rounds; everything else catches errors
    while True:
        num_wins += monty_hall()
        num_rounds += 1
        while True:
            player_status = input("Keep playing (y/n)? ").strip().lower()
            if player_status[0] in ['y', 'n']:  # first letter
                break
            print("Illegitimate input\n")
        if player_status.startswith("n"):
            break

    # get theoretical proportions:
    # A vector 1000 long of numbers 1, 2, or 3.
    # W.l.o.g. we can assume player chooses 1; then staying only wins if we get a 1
    # and switching only loses when we get a 1.
    door_vector = np.random.choice(DOORS, 1000, replace=True)
    proportion_stay = np.sum(door_vector == 1) / 1000
    proportion_switch = 1 - proportion_stay

    # printing results
    print(f"Your win/loss ration: {num_wins/num_rounds:.3f}")
    print(f"Ratio if you always stay: {proportion_stay:.3f}")
    print(f"Ratio if you always switch: {proportion_switch:.3f}")


def monty_hall():
    """
    Let's You play exactly one round of Monty Hall with 3 doors.

    Picks a door of 1, 2, 3 at random, then lets player choose a door, catching input errors.
    Then chooses monty's door from the remaining doors (which may be only one).
    Then asks player whether they want to switch, again catching input errors.
    Returns integer 1 or 0 for win and loss respectively.
    """

    # pick where the car is
    car_door = np.random.choice(DOORS)

    # get player's door
    print("Monty Hall says, 'Pick a door!'")
    while True:
        try:
            chosen_door = int(input("Choose a door (1, 2, or 3): "))
            if chosen_door in DOORS:
                break
            print("Input must be 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter an integer (1, 2, or 3).")

    # get Monty's door (not player's door or the car door)
    if chosen_door == car_door:
        monty_door = np.random.choice(list(set(DOORS) - {chosen_door}))
    else:
        monty_door = list(set(DOORS) - {chosen_door, car_door})[0]
    print(f"Monty opens door {monty_door}!")

    # ask for switch
    while True:
        reply = input("Would you like to switch (y/n)? ").strip().lower()
        if reply[0] in ['y', 'n']:  # first letter
            break
        print("Illegitimate input")

    # if player chooses to switch, select other door
    if reply.startswith("y"):
        chosen_door = list(set(DOORS) - {chosen_door, monty_door})[0]

    # result of the game
    if chosen_door == car_door:
        print("You won!")
        return 1
    print("You lost!")
    return 0


if __name__ == "__main__":
    main()
