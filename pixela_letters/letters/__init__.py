class Letters(object):

    def transpose_matrix(self, matrix):
        result = []
        for line in zip(*matrix):
            result.extend(line)
        return result
