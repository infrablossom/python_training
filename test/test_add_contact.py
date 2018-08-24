# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.add_new_contact()
    app.fill_contact_fields(Contact(firstname="Name", middlename="QA", lastname="Lastname", nick="Nick", title="Title", company="OOO", home="3434", mobile="3434", work="3434", fax="3434",
                                 email="example@ex.com", phone2="home"))
    app.logout()


def test2_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.add_new_contact()
    app.fill_contact_fields(Contact(firstname="Tanya", middlename="", lastname="Ohlsen", nick="Blossom", title="", company="", home="999", mobile="888", work="", fax="",
                                 email="example@cats.com", phone2="111"))
    app.logout()
