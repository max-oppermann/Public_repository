import sys
import csv
import random
import math
from datetime import date, timedelta

def main():
    deck = load_flashcards('flashcards.csv')
    while True:
        try:
            action = input(f"You exit the Program via ctrl+D. \nDo you want to 'learn' or 'write' cards? Type (l/w) \n")
            print()
        except EOFError:
            sys.exit()
        if action == 'w':
            write(deck)
        elif action == 'l' and not deck == []:
            learn(deck)
        elif action == 'l' and deck == []:
            print("Deck is empty. You first have to write cards.")
        else:
            print("Invalid action.")

def load_flashcards(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_flashcards(csv_file, flashcard_list):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['front', 'back', 'date', 'interval'])
        writer.writeheader()
        writer.writerows(flashcard_list)

def write(flashcards):
    while True:
        try:
            front = input("Front: ")
            back = input("Back: ")
            new_card = {"front": front, "back": back, "date": date.today(), "interval": 2}
            flashcards.append(new_card)
        except EOFError:
            break

    save_flashcards('flashcards.csv', flashcards)
    sys.exit()


def learn(flashcards):
    due_cards = [card for card in flashcards if is_due(card)] # 'filter' doesn't work here because shuffle() in the next line can't handle a filter object
    random.shuffle(due_cards)
    for card in due_cards:
        try:
            print(f"{card['front']}\n")
            input(f"Press 'Enter' to continue \n")
            print(f"{card['back']}\n")
            user_correct = (input("Correct? Type (y/n): ") == "y") # liable to mistyping, but so what
            print()
            update_date(card, user_correct)
        except EOFError:
            save_flashcards('flashcards.csv', flashcards)
            sys.exit()
    print("Done with today's cards")
    save_flashcards('flashcards.csv', flashcards)
    sys.exit()

def is_due(card):
    return date.today() >= date.fromisoformat(card["date"])

def update_date(card, correct):
    factor = 2.5 if correct else 0.2
    card["interval"] = math.ceil(float(card["interval"]) * factor)
    card["date"] = date.fromisoformat(card["date"]) + timedelta(days=int(card["interval"]))


if __name__ == "__main__":
    main()
