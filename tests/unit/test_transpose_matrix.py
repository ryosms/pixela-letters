from pixela_letters.letters import Letters


def test_can_transpose():
    sut = Letters()
    actual = sut.transpose_matrix([[1, 4, 7],
                                   [2, 5, 8],
                                   [3, 6, 9]])
    expected = [1, 2, 3,
                4, 5, 6,
                7, 8, 9]
    assert actual == expected
