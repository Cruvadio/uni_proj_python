class WeAre():
    _count = 0
    def __init__(self):
        WeAre._count += 1

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        return

    @count.deleter
    def count(self):
        return

    def __del__(self):
        WeAre._count -= 1


