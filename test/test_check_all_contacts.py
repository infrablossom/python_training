
from fixture.contact import Contact


# переписать
def test_check_all_contacts(app, db):
    ui_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    assert sorted(db_contacts, key=Contact.id_or_max) == sorted(ui_contacts, key=Contact.id_or_max)

