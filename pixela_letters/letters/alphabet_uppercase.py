class AlphabetUppercase(object):
    def A(self):
        """
        . . # . .
        . # . # .
        . # . # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        """
        return self.transpose_matrix([
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ])
