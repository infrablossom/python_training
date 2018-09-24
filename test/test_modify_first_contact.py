from model.contact import Contact


def test_modify_firstname(app):

    #if app.contact.count_contacts() == 0:
     #   app.contact.add_new_contact(Contact(firstname="test"))
    #app.contact.modify_first_contact(Contact(firstname="New contact"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New contact")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count_contacts()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)