class SymbolLetters(object):
    symbol_table = {
        ' ': 'space',
        '!': 'exclamation'
    }

    @staticmethod
    def space():
        return [0, 0, 0, 0, 0, 0, 0]

    @staticmethod
    def exclamation():
        return [1, 1, 1, 1, 1, 0, 1]
