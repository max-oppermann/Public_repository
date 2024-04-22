 # We have Anki at home.
    #### Video Demo:  https://youtu.be/NZa-w8HLIPI
    #### Description:

    This is a dollar-store version of the flashcard-learning program Anki.
    A flashcard is simply something that shows you one piece of information (the front) and makes you guess another (the back), and one of the benefit of doing that digitally rather than with pen-and-paper flashcards is that the "flipping over" is much faster if it merely requires the press of a button.
    The other quality of a deck of flashcards is its scheduling. Physically, this would be accomplished via different boxes that the cards progress through when they are answered correctly. Digitally, a due-date is simply assigned to each card which allows for much more granularity.
    In this program the showing of front/back is done by the write() and learn() functions; the scheduling is done by the is_due() and update_date() functions. The flashcards.csv file is the deck that stores the information on the front/back, the due-date, and the interval that was last used to change the due-date (which will be used to construct the next due-date and interval).

    Originally this was planned much more object orientedly, using a class for flashcards and decks each. But the requirement is to have at least three functions outside of main() which wouldn't have been satisfied.
    Another, more self-directed choice was whether the user should be able to decide themselves if they answered a flashcard correctly or whether that should be decided for them by comparing an input to the back of the card in some way. But the latter would have penalized irrelevant differences. If the back of the card actually read "to walk" but the user typed in just "walk," that shouldn't be counted as incorrect; and what about simple mistypes like "walt" or "wakl?"

    ## The different functions:

      * load_flashcards() is the first thing that will happen when main() gets executed. It creates a list of dictionaries, one dict per line in the csv, i. e., per card. This originally used a for-loop that appended an empty list, but luckily Python can do that automatically, which is why the funciton is much shorter now than it used to be.

      * main() then keeps the user in an indefinite loop until they either ctrl+D out of the program (in the try-except block in main() itself or in the write() or learn() functions) or finish learning all due cards for that day.

      * save_flashcards() gets called at the end of either writing or learning flashcards, so whenever a card could have been changed. What may seem (and could actually be) overkill is that it rewrites the entire .csv everytime it saves. For write() that's probably true, since the file could also just be appended by every new card rather than rewriting the entire file just to include the new cards. But for learn() the alternative would have been to go through the entire file for each card learned and then rewrite the relevant line. That didn't seem much easier to me. And when I had the written the function to save learned flashcards it seemed easier to just also use it for newly written ones.
      Originally this function, too, used a for-loop. Again, Python is just more understanding about my needs.

      * learn() is relatively straight-forward. It shows the "front" of a (due) card, waits for the user to prompt it to show the back of the card, gets the user input on whether they were correct (user_correct is a boolean, it doesn't store or measure "correctness" in any sense) and calls a function to update the due-date for that particular card (in the list of dictionaries, which is saved to the csv file at the end). Instead of list-comprehension I tried to use a filter because it looks more intuitive to me, but the random.shuffle() function couldn't handle the filter-object.

      * write() is even easier. It just appends our list of dictionaries (created from the .csv) by a newly created dictionary until the user ctrl+D’s out of the program and then saves before actually sys.exiting. The default of "date" being date.today() just means that the first time you can learn new cards is the day you create them. The default value for the initial interval is somewhat arbitrary; in any case, the number corresponds to how many days will pass before you will see the card again after answering it the enxt time. After I answer a new card, I will see it again in two days.

      * is_due() involved a complication because I couldn't save date-objects to the csv file. Instead, when the dictionary created in write() gets saved to the .csv, a string of today’s date in ISO format gets saved. Whence the transformation into a date-object via date.fromisofromat(). is_due() returns a boolean used in the conditional in the list comprehension to create the list of due cards in learn().

      * update_date() is the heart of the program (in my opinion). Each "card" will be dictionary, the "correct" will be a boolean. The "factor" determines how much longer/shorter the interval before you next see the card will be depending on whether you marked it as correct. The values are somewhat arbitrary and depend on how high a percentage of "correct" answers you want and how much you are willing to learn per day. These values in particular are simply my personal settings from the actual Anki.
      Stored in the .csv seems to be a string, so the interval of the card needs to be converted into something that can be multiplied; the product should be rounded to the next day so that the updating of the due-date doesn't have odd results like scheduling a card for 9:43 PM (making it inaccesible on that day at 9:42). The math.ceiling() function ("rounding" 0.1 to 1, e. g.) is used instead of round() so that the interval never goes to 0; since the "factor" is multiplied in, the interval would never change subsequently.
      The interval is the transformed into timedelta-object to update the due-date of the card.
      Originally this funciton was much longer, but some variables along the way were actually only used once. I also went from saving the interval in the .csv as a timedelta to saving it as an int which made the funciton mcuh shorter; again, the timedelta didn't actually get saved as a timedelta-object but a complicated string I had to split. So instead of transforming a timedelta into string into a timedelta, the funciton now just transforms a string into a timedelta.
      Also, I do not care about the semantic redundancy of "up-date date."

