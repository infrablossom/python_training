from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="1", middlename="11", lastname="22", nick="222", title="3", company="333",
                home="0", mobile="0", work="0", fax="88",
                email="example34343434@ex.com", phone2="777"))
    app.session.logout()