from random import randrange
from fixture.contact import Contact
import re

# переписать
def test_check_all_contact(app, db):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(Contact(firstname="test"))
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert contact_from_home_page.id == contact_from_db.id
    assert contact_from_home_page.lastname == contact_from_db.lastname
    assert contact_from_home_page.firstname == contact_from_db.firstname
    # assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email2, contact.email3])))