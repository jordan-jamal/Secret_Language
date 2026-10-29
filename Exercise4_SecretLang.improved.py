import random


def get_random_sentence(sentences):
    """
    Select a random sentence from a list of sentences.
    
    :param sentences: List of sentences to choose from.
    :return: A randomly selected sentence.
    """
    return random.choice(sentences)


def swap_characters(char_list, index1, index2):
    """
    Swap characters at two specified indices in a list.
    
    :param char_list: List of characters.
    :param index1: First index to swap.
    :param index2: Second index to swap.
    """
    if index1 < len(char_list) and index2 < len(char_list):
        char_list[index1], char_list[index2] = char_list[index2], char_list[index1]


def main():
    """
    Main function to run the guessing game.
    """
    list1 = [
        "What is your name",
        "What are you doing",
        "How can this be possible",
        "What a joke",
        "I think you can level up"
    ]

    char = get_random_sentence(list1)
    lst = list(char.lower())

    # Swap characters safely
    swap_characters(lst, 3, 7)
    lst.append(lst[1])
    lst.append(lst[2])
    lst.insert(0, lst[3])
    lst.reverse()

    char1 = "".join(lst)
    print("Guess the sentence:")
    print(char1)

    inp = input("")
    if inp.strip().lower() == char.lower():
        print("You guessed it right!!!")
    else:
        print("Ohh no... your guess was wrong")

    a = input("Want to decode? (Type Yes or No): ").strip().lower()
    if a == "yes":
        lst.reverse()
        lst1 = lst[1:-2]
        swap_characters(lst1, 3, 7)
        char2 = "".join(lst1)
        print(char2)
    else:
        print("Exiting the game.")


if __name__ == '__main__':
    main()