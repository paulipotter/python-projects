from q import *


def q_round(source: Q, dest: Q, original_q: str):
    """
    1. Take the top card off the deck and set it on the table
    2. Take the next off the top and put it on the bottom of the deck in your hand.
    3. Continue steps 1 and 2 until all cards are on the table. This is a round.
    4. Pick up the deck from the table and repeat steps 1-3 until the deck is in original order.

    :param source: the original deck with N cards
    :param dest: the empty deck
    :param original_q: a string that holds the original order to later compare to the deck
    """
    number_of_rounds = 0
    source_q = ""

    # while original q does not match the source
    while original_q != source_q:
        # while holding the deck, aka deck is not empty
        while not source.is_empty():
            # Take the top card off the deck and set it on the table
            dest.push(source.pop())

            if source.is_empty():
                break
            else:
                # Take the next off the top and put it on the bottom of the deck in your hand.
                source.push(source.pop())
        # Continue steps 1 and 2 until all cards are on the table. AKA until the holding deck is empty
        # This is a round.

        # swap variables
        tmp = source
        source = dest
        dest = tmp

        # keep track of the number of rounds
        number_of_rounds += 1

        # set deck order to a string variable to compare to original order string var
        source_q = str(deck)

        # Write results to standard output.
        print("-----------")
        print("round number:", number_of_rounds)
        print("is the deck the same as before?", source_q == original_q)
        print("original", original_q)
        print("deck    ", deck)
        print("table   ", table)
    print("-----------")
    print("Total Number of rounds:", number_of_rounds)


def get_user_input() -> int:
    """
    The function will get the number N to generate the deck
    and will throw an error if the value provided is not an integer
    :return: the valid N value to be used to generate the deck
    """
    while True:
        num = input("Please enter a number: ")
        try:
            val = int(num)
            print("Input is an integer number.")
            print("Input number is: ", val)
            return val
        except ValueError:
            print("Your input was not a valid integer. Please enter a valid integer")


if __name__ == '__main__':
    # The program should take the number of cards in the deck as a command line argument
    n = get_user_input()

    deck = Q()
    table = Q()

    # Populate the deck containing n cards
    for i in range(n):
        deck.push(i)

    # Make a copy of the deck to check the original order
    original_order = str(deck)

    q_round(source=deck, dest=table, original_q=original_order)
