# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # добавляем новую группу в новый список
    assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    # добавляем новую группу в старый список
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


