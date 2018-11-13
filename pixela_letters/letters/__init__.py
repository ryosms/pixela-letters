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
                self.letters_dict[key] = self.load_quantities(key)

            quantities.extend(self.transpose_matrix(self.letters_dict[key]))

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
        key = letter
        if key in self.symbol_table:
            key = self.symbol_table[key]

        try:
            return getattr(self, key)()
        except AttributeError:
            # TODO: handle
            return []

    @staticmethod
    def transpose_matrix(matrix):
        assert isinstance(matrix, list)
        if not isinstance(matrix[0], list):
            return matrix

        result = []
        for line in zip(*matrix):
            result.extend(line)
        return result


if __name__ == '__main__':
    clazz = Letters()
    print(clazz.create_quantities('A'))
