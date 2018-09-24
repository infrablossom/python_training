# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Name", middlename="QA", lastname="Lastname", nick="Nick", title="Title", company="OOO", home="3434", mobile="3434", work="3434", fax="3434",
                                    email="example@ex.com", phone2="home")
    app.contact.input_list(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test2_add_contact(app):
 #   app.open_home_page()
  #  app.contact.add_new_contact(Contact(firstname="Tanya", middlename="", lastname="Ohlsen", nick="Blossom", title="", company="", home="999", mobile="888", work="", fax="",
                                    #email="example@cats.com", phone2="111"))
