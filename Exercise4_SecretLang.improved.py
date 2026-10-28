import random


class SentenceGame:
    def __init__(self):
        self.sentences = [
            "What is your name",
            "What are you doing",
            "How can this be possible",
            "What a joke",
            "I think you can level up"
        ]
        self.max_index = len(self.sentences) - 1

    def get_random_sentence(self):
        """
        Select a random sentence from the list.
        """
        return self.sentences[random.randint(0, self.max_index)]

    def scramble_sentence(self, sentence):
        """
        Scramble the given sentence by manipulating its characters.
        :param sentence: The sentence to scramble.
        :return: The scrambled version of the sentence.
        """
        lst = list(sentence.lower())
        if len(lst) < 8:
            raise ValueError("Sentence is too short to scramble.")
        lst[3], lst[7] = lst[7], lst[3]
        lst.append(lst[1])
        lst.append(lst[2])
        lst.insert(0, lst[3])
        lst.reverse()
        return "".join(lst)

    def play(self):
        """
        Main method to play the guessing game.
        """
        original_sentence = self.get_random_sentence()
        scrambled_sentence = self.scramble_sentence(original_sentence)
        print("Guess the sentence:")
        print(scrambled_sentence)
        user_guess = input("")

        if self.validate_guess(user_guess, original_sentence):
            print("You guessed it right!!!")
        else:
            print("Ohh no... your guess was wrong")
            self.offer_decoding(original_sentence)

    def validate_guess(self, guess, original):
        """
        Validate the user's guess against the original sentence.
        :param guess: The user's guess.
        :param original: The original sentence.
        :return: True if the guess is correct, False otherwise.
        """
        return guess.strip().lower() == original.lower()

    def offer_decoding(self, original_sentence):
        """
        Offer the user the option to decode the original sentence.
        :param original_sentence: The original sentence to decode.
decode_choice = input("Want to decode? (Type Yes or No): ").strip().lower() if decode_choice in ["yes", "no"] else "no"
        decode_choice = input("Want to decode? (Type Yes or No): ").strip().lower()
        if decode_choice == "yes":
            print(original_sentence)


if __name__ == '__main__':
    game = SentenceGame()
    game.play()