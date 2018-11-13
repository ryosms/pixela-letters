# noinspection PyPep8Naming
class AlphabetUppercase(object):
    @staticmethod
    def A():
        """
        . . # . .
        . # . # .
        . # . # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        """
        return [
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
        ]

    @staticmethod
    def B():
        """
        # # # # .
        # . . . #
        # . . . #
        # # # # .
        # . . . #
        # . . . #
        # # # # .
        """
        return [
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0],
        ]

    @staticmethod
    def C():
        """
        . # # # .
        # . . . #
        # . . . #
        # . . . .
        # . . . #
        # . . . #
        . # # # .
        """
        return [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0],
        ]

    @staticmethod
    def D():
        """
        # # # . .
        # . . # .
        # . . . #
        # . . . #
        # . . . #
        # . . # .
        # # # . .
        """
        return [
            [1, 1, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 0, 0],
        ]

    @staticmethod
    def E():
        """
        # # # #
        # . . .
        # . . .
        # # # #
        # . . .
        # . . .
        # # # #
        """
        return [
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
        ]

    @staticmethod
    def F():
        """
        # # # #
        # . . .
        # . . .
        # # # #
        # . . .
        # . . .
        # . . .
        """
        return [
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ]

    @staticmethod
    def G():
        """
        . # # # .
        # . . . #
        # . . . #
        # . . . .
        # . # # #
        # . . . #
        . # # # .
        """
        return [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0]
        ]

    @staticmethod
    def H():
        """
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        """
        return [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
        ]

    @staticmethod
    def I():
        """
        # # #
        . # .
        . # .
        . # .
        . # .
        . # .
        # # #
        """
        return [
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 1],
        ]

    @staticmethod
    def J():
        """
        . # # # #
        . . . # .
        . . . # .
        . . . # .
        # . . # .
        # . . # .
        . # # . .
        """
        return [
            [0, 1, 1, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0],
        ]

    @staticmethod
    def K():
        """
        # . . . #
        # . . # .
        # . # . .
        # # . . .
        # . # . .
        # . . # .
        # . . . #
        """
        return [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1],
        ]

    @staticmethod
    def L():
        """
        # . . .
        # . . .
        # . . .
        # . . .
        # . . .
        # . . .
        # # # #
        """
        return [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
        ]

    @staticmethod
    def M():
        """
        # . . . #
        # # . # #
        # . # . #
        # . # . #
        # . # . #
        # . # . #
        # . . . #
        """
        return [
            [1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
        ]

    @staticmethod
    def N():
        """
        # . . . #
        # # . . #
        # . # . #
        # . # . #
        # . # . #
        # . . # #
        # . . . #
        """
        return [
            [1, 0, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 0, 1],
        ]

    @staticmethod
    def O():
        """
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """
        return [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0],
        ]

    @staticmethod
    def P():
        """
        # # # # .
        # . . . #
        # . . . #
        # # # # .
        # . . . .
        # . . . .
        # . . . .
        """
        return [
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
        ]

    @staticmethod
    def Q():
        """
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        # . # . #
        # . . # .
        . # # . #
        """
        return [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 1],
        ]

    @staticmethod
    def R():
        """
        # # # # .
        # . . . #
        # . . . #
        # # # # .
        # . . . #
        # . . . #
        # . . . #
        """
        return [
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
        ]

    @staticmethod
    def S():
        """
        . # # # .
        # . . . #
        # . . . .
        . # # # .
        . . . . #
        # . . . #
        . # # # .
        """
        return [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0],
        ]

    @staticmethod
    def T():
        """
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """
        return [
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ]

    @staticmethod
    def U():
        """
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """
        return [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0],
        ]

    @staticmethod
    def V():
        """
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        . # . # .
        . # . # .
        . . # . .
        :return:
        """
        return [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
        ]

    @staticmethod
    def W():
        """
        # . . . . . #
        # . . # . . #
        # . . # . . #
        . # . # . # .
        . # . # . # .
        . . # . # . .
        . . # . # . .
        """
        return [
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
        ]

    @staticmethod
    def X():
        """
        # . . . #
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        # . . . #
        """
        return [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
        ]

    @staticmethod
    def Y():
        """
        # . . . #
        # . . . #
        . # . # .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """
        return [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ]

    @staticmethod
    def Z():
        """
        # # # # #
        . . . . #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
        # # # # #
        """
        return [
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ]
