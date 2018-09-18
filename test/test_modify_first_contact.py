from model.contact import Contact


def test_modify_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New contact"))