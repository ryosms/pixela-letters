from pixela_letters.letters.alphabet_lowercase import AlphabetLowercase
from pixela_letters.letters.alphabet_uppercase import AlphabetUppercase
from pixela_letters.letters.symbol_letters import SymbolLetters


class Letters(AlphabetUppercase, AlphabetLowercase, SymbolLetters):
    no_space_combination = {'T': 'A', 'A': 'T'}

    def __init__(self):
        self.letters_dict = {}
        pass

    def create_quantities(self, poem: str) -> list:
        quantities = []
        last_letter = ''
        for key in poem:
            if self.need_space(last_letter, key):
                quantities.extend(self.space())

            if key not in self.letters_dict:
                # create quantities
                invoker = self.load_quantities(key)
                if invoker is not None:
                    self.letters_dict[key] = invoker()
                else:
                    self.letters_dict[key] = [key, key]
            quantities.extend(self.letters_dict[key])

        if len(quantities) > 0:
            quantities.extend(self.space())

        return quantities

    def need_space(self, last: str, current: str) -> bool:
        if last == ' ' or current == ' ':
            return False
        if last in self.no_space_combination \
                and self.no_space_combination[last] == current:
            return False
        return True

    def load_quantities(self, letter: str):
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
