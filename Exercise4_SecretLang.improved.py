import random

class SentenceGuesser:
    """
    A class to handle the sentence guessing game.
    """
    def __init__(self):
        self.sentences = [
            "What is your name",
            "What are you doing",
            "How can this be possible",
            "What a joke",
            "I think you can level up"
        ]
        self.selected_sentence = self.select_random_sentence()

    def select_random_sentence(self):
        """
        Select a random sentence from the list.
        """
        return random.choice(self.sentences)

    def scramble_sentence(self, sentence):
        """
        Scramble the characters of the given sentence.
        """
        lst = list(sentence.lower())
        if len(lst) < 8:
            raise ValueError("Sentence must be at least 8 characters long to scramble.")
        lst[3], lst[7] = lst[7], lst[3]
        lst.append(lst[1])
        lst.append(lst[2])
        lst.insert(0, lst[3])
        lst.reverse()
        return "".join(lst)

    def play_game(self):
        """
        Main method to play the guessing game.
        """
        scrambled_sentence = self.scramble_sentence(self.selected_sentence)
        print("Guess the sentence:")
        print(scrambled_sentence)
        user_input = input("").strip()
        self.validate_input(user_input)
        self.check_guess(user_input)

    def validate_input(self, user_input):
        """
        Validate the user input for the guess.
        """
        if not user_input:
            raise ValueError("Input cannot be empty.")

    def check_guess(self, user_input):
        """
        Check if the user's guess is correct.
        """
        if user_input.lower() == self.selected_sentence.lower():
            print("You guessed it right!!!")
        else:
            print("Ohh no... your guess was wrong")
            self.offer_decoding()

    def offer_decoding(self):
        """
        Offer the user an option to decode the sentence.
        """
        a = input("Want to decode? (Type Yes or No): ").strip().lower()
        if a == "yes":
            print(self.selected_sentence)

if __name__ == '__main__':
    game = SentenceGuesser()
    game.play_game()