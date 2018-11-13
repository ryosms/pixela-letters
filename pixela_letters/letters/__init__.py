from pixela_letters.letters.alphabet_lowercase import AlphabetLowercase
from pixela_letters.letters.alphabet_uppercase import AlphabetUppercase
from pixela_letters.letters.symbol_letters import SymbolLetters


class Letters(AlphabetUppercase, AlphabetLowercase, SymbolLetters):
    def __init__(self):
        self.letters_dict = {}
        pass

    def create_quantities(self, poem: str) -> list:
        quantities = []
        for key in poem:
            if key not in self.letters_dict:
                # create quantities
                invoker = self.load_quantities(key)
                if invoker is not None:
                    self.letters_dict[key] = invoker()
                else:
                    self.letters_dict[key] = [key, key]
            quantities.extend(self.letters_dict[key])

        return self.transpose_matrix(quantities)

    def load_quantities(self, letter: str):
        print(f"called![{letter}]")
        try:
            return getattr(self, letter)
        except AttributeError:
            return None

    def transpose_matrix(self, matrix):
        result = []
        for line in zip(*matrix):
            result.extend(line)
        return result


if __name__ == '__main__':
    clazz = Letters()
    print(clazz.create_quantities('A'))
