

from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.get_contact_list() == 0:
        app.contact.input_list(Contact(firstname="start"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="ed", middlename="ed",
                                    lastname="ed", nick="ed",
                                    title="ed", company="ed",
                                    address="ed", homephone="5656565",
                                    mobilephone="6565656", work="565656",
                                    fax="565656", email="ed",
                                    email2="ed", email3="ed",
                                    home="ed", phone2="56646")
    contact.id = old_contacts[index].id
    app.contact.edit_random_contact(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact

