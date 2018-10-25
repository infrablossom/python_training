from model.group import Group
from random import randrange


def test_modify_group_name(app, db, json_groups, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Test")
    group.id = old_groups[index].id
    if app.group.count_groups() == 0:
        app.group.create(Group(name="new name"))
    app.group.modify_group_by_id(group.id, json_groups)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


