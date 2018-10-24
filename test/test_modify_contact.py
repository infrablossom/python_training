from model.contact import Contact
from random import randrange


''' def test_modify_firstname(app, json_contacts):
    contact = json_contacts
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New contact")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count_contacts()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)'''


def test_contact_edit(app, db, json_contacts):
    if len(db.get_contact_list()) == 0:
        app.contact.input_list(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="example", middlename="example",lastname="example", nick="example", title="example",
                      company="example", address="example", homephone="+678678786", mobilephone="75675675",
                      workphone="+89787898", fax="+89789789", email="example@k.k")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, json_contacts)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

