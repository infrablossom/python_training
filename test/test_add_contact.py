# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.fill_fields(Contact(firstname="Name", middlename="QA", lastname="Lastname", nick="Nick", title="Title", company="OOO", home="3434", mobile="3434", work="3434", fax="3434",
                                    email="example@ex.com", phone2="home"))
    app.session.logout()


def test2_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.fill_fields(Contact(firstname="Tanya", middlename="", lastname="Ohlsen", nick="Blossom", title="", company="", home="999", mobile="888", work="", fax="",
                                    email="example@cats.com", phone2="111"))
    app.session.logout()
