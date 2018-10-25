
from fixture.contact import Contact


# переписать
def test_check_all_contacts(app, db):
    ui_contacts = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip())
    db_contacts = map(clean, db.get_contact_list())
    assert sorted(db_contacts, key=Contact.id_or_max) == sorted(ui_contacts, key=Contact.id_or_max)

