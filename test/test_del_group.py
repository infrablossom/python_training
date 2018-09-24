from model.group import Group


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    # не удаляем строку проверки длины 2 списков для перестраховки
    # и более понятного эксепшена в случае отсутствия элементов
    assert len(old_groups) - 1 == app.group.count_groups()
    old_groups[0:1] = []
    assert old_groups == new_groups

