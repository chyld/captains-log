class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return other.__class__ == Dog and hash(self) == hash(other)


def symmetric_point(p, q):
    return [q[0] - p[0] + q[0], q[1] - p[1] + q[1]]


def add_length(s):
    return ['{} {}'.format(w, len(w)) for w in s.split()]
