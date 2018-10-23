# -*- coding: utf-8 -*-

from model.contact import Contact


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.input_list(contact)
    new_contacts = app.contact.get_contact_list()
    # assert len(old_contacts) + 1 == app.contact.count_contacts()
    old_contacts.append(contact)
    # на строке ниже появляется ошибка, не получилось выявить проблему
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


