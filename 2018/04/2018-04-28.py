def mango(quantity, price):
    return ((quantity // 3) * 2 * price) + (quantity % 3 * price)


def remove_every_other(l):
    return [e for i, e in enumerate(l) if not i & 1]


class Cube(object):
    def __init__(self, n=0):
        self._side = abs(n)

    def get_side(self):
        return self._side

    def set_side(self, new_side):
        self._side = abs(new_side)
