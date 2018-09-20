from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nick=None, title=None, company=None, home=None, mobile=None, work=None, fax=None,
                            email=None, phone2=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nick = nick
        self.title = title
        self.company = company
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.phone2 = phone2
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    # определила функцию сравнения самих объектов, а не их физического расположения в памяти
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
