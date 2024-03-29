# -*- coding: utf-8 -*-
from model.group import Group
import pytest


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('I add a new group with %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('I add a new group with %s to the list' % group):
    new_groups = db.get_group_list()
    old_groups.append(group)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


