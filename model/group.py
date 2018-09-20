# вспомогательный класс для хранения свойств группы


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # определила функцию сравнения самих объектов, а не их физического расположения в памяти
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

