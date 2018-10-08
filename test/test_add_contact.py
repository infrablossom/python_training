# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nick="", title="", company="", home="", mobile="",
                    work="", fax="", email="", phone2="")] + [
    Contact(firstname=random_string("name", 10), middlename=random_string("header", 20),
            lastname=random_string("footer", 20), nick=random_string("footer", 10), title=random_string("title", 10),
            company=random_string("company", 10), home=random_string("home", 10), mobile=random_string("mobile", 10),
            work=random_string("work", 10), fax=random_string("fax", 10), email=random_string("email", 10),
            phone2=random_string("phone2", 10))
    for i in range(5)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.input_list(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    old_contacts.append(contact)
    # на строке ниже появляется ошибка, не получилось выявить проблему
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test2_add_contact(app):
 #   app.open_home_page()
  #  app.contact.add_new_contact(Contact(firstname="Tanya", middlename="", lastname="Ohlsen", nick="Blossom", title="", company="", home="999", mobile="888", work="", fax="",
                                    #email="example@cats.com", phone2="111"))
