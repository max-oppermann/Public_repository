import sys
import csv
import random
from datetime import date, timedelta

def main():
    deck = load_flashcards('flashcards.csv')
    while True:
        action = input("Do you want to 'learn' or 'write' cards? Type l/w ")
        if action == 'w':
            write(deck)
        elif action == 'l' and not deck == None:
            learn(deck)
        elif action == 'l' and deck == None:
            print("Deck is empty. You first have to write cards.")
        else:
            print("Invalid action.")

def load_flashcards(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        flashcards = list(reader)

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
            new_card = {"front:" front, "back": back, "date": date.today(), "interval": timedelta(days=2)}
            flashcards.append(new_card)
        except EOFError:
            break
    
    save_flashcards('flashcards.csv', flashcards)
    sys.exit()
    

def learn(flashcards):
    due_cards = [card for card in flashcards if is_due(card)] # filter doesn't work here because shuffle() in the next line can't handle a filter object
    random.shuffle(due_cards)
    for card in due_cards:
        try:
            user_answer = input(f"{card['front']}\n")
            print(f"{card['back']}")
            user_correct = (input("Correct? type: y/n") == "y")
            update_time(card, user_correct)
        except EOFError:
            save_flashcards('flashcards.csv', flashcards)
            sys.exit()
    
    save_flashcards('flashcards.csv', flashcards)
    sys.exit()

def is_due(card):
    return datetime.today() >= card["date"]

def update_time(card, correct): 
    card["date"] += card["interval"]
    factor = 2.5 if correct else 0.2
    card["interval"] *= factor
    
if __name__ == "__main__":
    main()
