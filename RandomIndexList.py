import random


class RandomIndexList(list):
    def __init__(self, *args, **kwargs):
        iterable = args[0] if len(args) > 0 else []
        index = kwargs.get('index')

        super(RandomIndexList, self).__init__(iterable)

        if index is None:
            self.index = random.choice(range(0, 100))
        elif not isinstance(index, int):
            raise NonIntegerIndex("Index value {} is not a valid integer.".format(index))
        elif index < 0:
            raise NegativeIndexError()
        else:
            self.index = index

    def __getitem__(self, i):
        if isinstance(i, slice):
            i = slice(i.start - self.index, i.stop - self.index, i.step)
        else:
            i -= self.index

        return super(RandomIndexList, self).__getitem__(i)

    def __getslice__(self, start, stop):
        return super(RandomIndexList, self).__getslice__(start - self.index, stop - self.index)


class NonIntegerIndex(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    pass


class NegativeIndexError(Exception):
    def __str__(self):
        return "Starting indexes must be a positive integer."
    pass
