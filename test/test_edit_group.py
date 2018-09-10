from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="111", header="111", footer="111"))
    app.session.logout()

