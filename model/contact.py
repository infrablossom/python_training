from sys import maxsize


class Contact:

    #def __init__(self, firstname=None, middlename=None, lastname=None, nick=None, title=None, company=None, home=None, mobile=None, work=None, fax=None,
     #                       email=None, phone2=None, id=None):
      #  self.firstname = firstname
       # self.middlename = middlename
        #self.lastname = lastname
        #self.nick = nick
        #self.title = title
        #self.company = company
        #self.home = home
        #self.mobile = mobile
        #self.work = work
        #self.fax = fax
        #self.email = email
        #self.phone2 = phone2
        #self.id = id

    def __init__(self, firstname=None, middlename=None, lastname=None, nick=None, homephone=None, company=None,
                 title=None, mobilephone=None, workphone=None, secondaryphone=None, home=None, phone2=None, work=None,
                 email=None, email2=None, email3=None, fax=None, mobile=None, id=None, address=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.nick = nick
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.title = title
        self.company = company
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.phone2 = phone2
        self.id = id
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

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

# middlename="QA", lastname="Lastname", nick="Nick", title="Title", company="OOO", home="3434", mobile="3434", work="3434", fax="3434",
                                   # email="example@ex.com", phone2="home")