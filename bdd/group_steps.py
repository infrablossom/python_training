from pytest_bdd import given, when, then
from model.group import Group


# закончить
@given('a group list')
def group_list():
    return db.get_group_list()


@when('I add a new group with <name>, <header> and <footer>')
def add_new_group(app, name, header, footer):
    app.group.create(Group(name=name, header=header, footer=footer))


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list):
    old_groups = group_list
    new_groups = db.get_group_list()