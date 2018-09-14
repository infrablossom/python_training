from model.group import Group


def test_edit_group(app):
    app.group.edit_first_group(Group(name="111", header="111", footer="111"))

