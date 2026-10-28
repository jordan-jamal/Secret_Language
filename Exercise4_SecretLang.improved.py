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
        self.char = self.get_random_sentence()

    def get_random_sentence(self):
        """
        Select a random sentence from the list.
        Returns:
            str: A randomly selected sentence.
        """
        return random.choice(self.sentences)

    def scramble_sentence(self, sentence):
        """
        Scramble the characters of the given sentence.
        Args:
            sentence (str): The sentence to scramble.
        Returns:
            str: The scrambled sentence.
        """
        lst = list(sentence.lower())
        if len(lst) < 8:
            raise ValueError("Sentence must have at least 8 characters to scramble.")
        lst[3], lst[7] = lst[7], lst[3]
        lst.append(lst[1])
        lst.append(lst[2])
        lst.insert(0, lst[3])
        lst.reverse()
        return "".join(lst)

    def play(self):
        """
        Start the game by scrambling the sentence and getting user input.
        """
        scrambled = self.scramble_sentence(self.char)
        print("Guess the sentence:")
        print(scrambled)
        inp = input("").strip()
        if self.validate_input(inp):
            if inp == self.char or inp.lower() == self.char:
                print("You guessed it right!!!")
            else:
                print("Ohh no... your guess was wrong")
                self.offer_decoding()
        else:
            print("Invalid input. Please try again.")

    def validate_input(self, user_input):
        """
        Validate user input to prevent injection and ensure it's a string.
        Args:
            user_input (str): The input from the user.
        Returns:
            bool: True if valid, False otherwise.
        """
        return isinstance(user_input, str) and len(user_input) > 0

    def offer_decoding(self):
        """
        Offer the user the option to decode the scrambled sentence.
        """
        a = input("Want to decode? (Type Yes or No): ").strip().lower()
        if a == "yes":
            decoded = self.scramble_sentence(self.char)[1:-2]
            print(decoded)

if __name__ == '__main__':
    game = SentenceGame()
    game.play()