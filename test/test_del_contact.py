from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contacts() < 1:
        app.contact.add_new_contact(Contact(firstname="test"))
    app.contact.delete_first_contact()

