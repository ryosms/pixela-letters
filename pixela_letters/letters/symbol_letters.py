class SymbolLetters(object):
    symbol_table = {
        ' ': 'space',
        '!': 'exclamation',
        '?': 'question',
        '-': 'hyphen',
        '&': 'ampersand',
    }

    @staticmethod
    def space():
        return [0, 0, 0, 0, 0, 0, 0]

    @staticmethod
    def exclamation():
        return [1, 1, 1, 1, 1, 0, 1]

    @staticmethod
    def question():
        """
        . # # # .
        # . . . #
        # . . . #
        . . . # .
        . . # . .
        . . . . .
        . . # . .
        """
        return [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
        ]

    @staticmethod
    def hyphen():
        return [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

    @staticmethod
    def ampersand():
        """
        . # # . .
        # . . # .
        # . . # .
        . # # . .
        # . # . #
        # . . # .
        . # # . #
        """
        return [
            [0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 1],
        ]
